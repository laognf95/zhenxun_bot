import asyncio
import os
import random
import time
from datetime import datetime
from typing import List, Tuple, Union

import nonebot
from tortoise.functions import Count

from configs.config import Config
from configs.path_config import IMAGE_PATH
from services.log import logger
from utils.http_utils import AsyncHttpx
from utils.image_utils import BuildImage
from utils.utils import broadcast_group, cn2py

from .build_image import generate_skin
from .config import CASE2ID, CASE_BACKGROUND, COLOR2NAME, NAME2COLOR
from .models.buff_skin import BuffSkin
from .models.buff_skin_log import BuffSkinLog
from .models.open_cases_user import OpenCasesUser

URL = "https://buff.163.com/api/market/goods"
# proxies = 'http://49.75.59.242:3128'


driver = nonebot.get_driver()

BASE_PATH = IMAGE_PATH / "csgo_cases"


class CaseManager:

    CURRENT_CASES = []

    @classmethod
    async def reload(cls):
        cls.CURRENT_CASES = (
            await BuffSkin.annotate().distinct().values_list("case_name", flat=True)  # type: ignore
        )


async def update_case_data(case_name: str) -> str:
    """更新皮肤数据

    Args:
        case_name (str): 箱子名称

    Returns:
        _type_: _description_
    """
    if case_name not in CASE2ID:
        return "未在当前指定武器箱捏"
    session = Config.get_config("open_cases", "COOKIE")
    if not session:
        return "BUFF COOKIE为空捏!"
    db_skin_list = await BuffSkin.filter(case_name=case_name).all()
    db_skin_name_list = [
        skin.name + skin.skin_name + skin.abrasion for skin in db_skin_list
    ]
    data_list, total = await search_skin_page(case_name, 1)
    if isinstance(data_list, str):
        return data_list
    for page in range(2, total + 1):
        rand_time = random.randint(10, 50)
        logger.debug(f"访问随机等待时间: {rand_time}", "开箱更新")
        await asyncio.sleep(rand_time)
        data_list_, total = await search_skin_page(case_name, page)
        if isinstance(data_list_, list):
            data_list += data_list_
    create_list: List[BuffSkin] = []
    update_list: List[BuffSkin] = []
    log_list = []
    case_name_py = cn2py(case_name)
    now = datetime.now()
    for skin in data_list:
        name = skin.name + skin.skin_name + skin.abrasion
        skin.create_time = now
        skin.update_time = now
        if name in db_skin_name_list:
            update_list.append(skin)
        else:
            create_list.append(skin)
        log_list.append(
            BuffSkinLog(
                name=skin.name,
                case_name=skin.case_name,
                skin_name=skin.skin_name,
                is_stattrak=skin.is_stattrak,
                abrasion=skin.abrasion,
                color=skin.color,
                steam_price=skin.steam_price,
                weapon_type=skin.weapon_type,
                buy_max_price=skin.buy_max_price,
                buy_num=skin.buy_num,
                sell_min_price=skin.sell_min_price,
                sell_num=skin.sell_num,
                sell_reference_price=skin.sell_reference_price,
                create_time=now,
            )
        )
        name = skin.name + "-" + skin.skin_name + "-" + skin.abrasion
        file_path = BASE_PATH / case_name_py / f"{cn2py(name)}.jpg"
        if not file_path.exists():
            logger.debug(f"下载皮肤 {name} 图片: {skin.img_url}...", "开箱更新")
            await AsyncHttpx.download_file(skin.img_url, file_path)
            rand_time = random.randint(1, 10)
            await asyncio.sleep(rand_time)
            logger.debug(f"图片下载随机等待时间: {rand_time}", "开箱更新")
        else:
            logger.debug(f"皮肤 {name} 图片已存在...", "开箱更新")
    if create_list:
        logger.debug(f"更新武器箱: [<u><e>{case_name}</e></u>], 创建 {len(create_list)} 个皮肤!")
        await BuffSkin.bulk_create(create_list, 10)
    if update_list:
        abrasion_list = []
        name_list = []
        skin_name_list = []
        for skin in update_list:
            if skin.abrasion not in abrasion_list:
                abrasion_list.append(skin.abrasion)
            if skin.name not in name_list:
                name_list.append(skin.name)
            if skin.skin_name not in skin_name_list:
                skin_name_list.append(skin.skin_name)
        db_data = await BuffSkin.filter(
            case_name=case_name,
            skin_name__in=skin_name_list,
            name__in=name_list,
            abrasion__in=abrasion_list,
        ).all()
        _update_list = []
        for data in db_data:
            for skin in update_list:
                if (
                    data.name == skin.name
                    and data.skin_name == skin.skin_name
                    and data.abrasion == skin.abrasion
                ):
                    data.steam_price = skin.steam_price
                    data.buy_max_price = skin.buy_max_price
                    data.buy_num = skin.buy_num
                    data.sell_min_price = skin.sell_min_price
                    data.sell_num = skin.sell_num
                    data.sell_reference_price = skin.sell_reference_price
                    data.update_time = skin.update_time
                    _update_list.append(data)
        logger.debug(f"更新武器箱: [<u><c>{case_name}</c></u>], 更新 {len(create_list)} 个皮肤!")
        await BuffSkin.bulk_update(
            _update_list,
            [
                "steam_price",
                "buy_max_price",
                "buy_num",
                "sell_min_price",
                "sell_num",
                "sell_reference_price",
                "update_time",
            ],
            10,
        )
    if log_list:
        logger.debug(f"更新武器箱: [<u><e>{case_name}</e></u>], 新增 {len(log_list)} 条皮肤日志!")
        await BuffSkinLog.bulk_create(log_list)
    if case_name not in CaseManager.CURRENT_CASES:
        CaseManager.CURRENT_CASES.append(case_name)  # type: ignore
    return f"更新武器箱: [{case_name}] 成功, 共更新 {len(update_list)} 个皮肤, 新创建 {len(create_list)} 个皮肤!"


async def search_skin_page(
    case_name: str, page_index: int
) -> Tuple[Union[List[BuffSkin], str], int]:
    """查询箱子皮肤

    Args:
        case_name (str): 箱子名称
        page_index (int): 页数

    Returns:
        Union[List[BuffSkin], str]: BuffSkin
    """
    logger.debug(
        f"尝试访问武器箱: [<u><e>{case_name}</e></u>] 页数: [<u><y>{page_index}</y></u>]", "开箱更新"
    )
    cookie = {"session": Config.get_config("open_cases", "COOKIE")}
    params = {
        "game": "csgo",
        "page_num": page_index,
        "page_size": 80,
        "itemset": CASE2ID[case_name],
        "_": time.time(),
        "use_suggestio": 0,
    }
    proxy = None
    if ip := Config.get_config("open_cases", "BUFF_PROXY"):
        proxy = {"http://": ip, "https://": ip}
    response = await AsyncHttpx.get(
        URL,
        proxy=proxy,
        params=params,
        cookies=cookie,  # type: ignore
    )
    logger.debug(f"访问BUFF API: {response.text}", "更新武器箱")
    json_data = response.json()
    update_data = []
    if json_data["code"] == "OK":
        data_list = json_data["data"]["items"]
        for data in data_list:
            obj = {"case_name": case_name}
            name = data["name"]
            try:
                logger.debug(
                    f"武器箱: [<u><e>{case_name}</e></u>] 页数: [<u><y>{page_index}</y></u>] 正在收录皮肤: [<u><c>{name}</c></u>]...",
                    "开箱更新",
                )
                obj["buy_max_price"] = data["buy_max_price"]  # 求购最大金额
                obj["buy_num"] = data["buy_num"]  # 当前求购
                goods_info = data["goods_info"]
                info = goods_info["info"]
                tags = info["tags"]
                obj["weapon_type"] = tags["type"]["localized_name"]  # 枪械类型
                if obj["weapon_type"] in ["音乐盒", "印花", "探员"]:
                    continue
                elif obj["weapon_type"] in ["匕首", "手套"]:
                    obj["color"] = "KNIFE"
                    obj["name"] = data["short_name"].split("（")[0].strip()  # 名称
                elif obj["weapon_type"] in ["武器箱"]:
                    obj["color"] = "CASE"
                    obj["name"] = data["short_name"]
                else:
                    obj["color"] = NAME2COLOR[tags["rarity"]["localized_name"]]
                    obj["name"] = tags["weapon"]["localized_name"]  # 名称
                if obj["weapon_type"] not in ["武器箱"]:
                    obj["abrasion"] = tags["exterior"]["localized_name"]  # 磨损
                    obj["is_stattrak"] = "StatTrak" in tags["quality"]["localized_name"]  # type: ignore # 是否暗金
                    if not obj["color"]:
                        obj["color"] = NAME2COLOR[
                            tags["rarity"]["localized_name"]
                        ]  # 品质颜色
                else:
                    obj["abrasion"] = "CASE"
                obj["skin_name"] = data["short_name"].split("|")[-1].strip()  # 皮肤名称
                obj["img_url"] = goods_info["original_icon_url"]  # 图片url
                obj["steam_price"] = goods_info["steam_price_cny"]  # steam价格
                obj["sell_min_price"] = data["sell_min_price"]  # 售卖最低价格
                obj["sell_num"] = data["sell_num"]  # 售卖数量
                obj["sell_reference_price"] = data["sell_reference_price"]  # 参考价格
                update_data.append(BuffSkin(**obj))
            except Exception as e:
                logger.error(
                    f"更新武器箱: [<u><e>{case_name}</e></u>] 皮肤: [<u><c>{name}</c></u>] 错误",
                    e=e,
                )
        logger.debug(
            f"访问武器箱: [<u><e>{case_name}</e></u>] 页数: [<u><y>{page_index}</y></u>] 成功并收录完成",
            "开箱更新",
        )
        return update_data, json_data["data"]["total_page"]
    else:
        logger.warning(f'访问BUFF失败: {json_data["error"]}')
    return f'访问失败: {json_data["error"]}', -1


async def build_case_image(case_name: str) -> Union[BuildImage, str]:
    """构造武器箱图片

    Args:
        case_name (str): 名称

    Returns:
        Union[BuildImage, str]: 图片
    """
    background = random.choice(os.listdir(CASE_BACKGROUND))
    background_img = BuildImage(0, 0, background=CASE_BACKGROUND / background)
    if case_name:
        log_list = (
            await BuffSkinLog.filter(case_name=case_name)
            .annotate(count=Count("id"))
            .group_by("skin_name")
            .values_list("skin_name", "count")
        )
        skin_list_ = await BuffSkin.filter(case_name=case_name).all()
        skin2count = {item[0]: item[1] for item in log_list}
        case = None
        skin_list: List[BuffSkin] = []
        exists_name = []
        for skin in skin_list_:
            if skin.color == "CASE":
                case = skin
            else:
                name = skin.name + skin.skin_name
                if name not in exists_name:
                    skin_list.append(skin)
                    exists_name.append(name)
        generate_img = {}
        for skin in skin_list:
            skin_img = await generate_skin(skin, skin2count[skin.skin_name])
            if skin_img:
                if not generate_img.get(skin.color):
                    generate_img[skin.color] = []
                generate_img[skin.color].append(skin_img)
        skin_image_list = []
        for color in COLOR2NAME:
            if generate_img.get(color):
                skin_image_list = skin_image_list + generate_img[color]
        img = skin_image_list[0]
        img_w, img_h = img.size
        total_size = (img_w + 25) * (img_h + 10) * len(skin_image_list)  # 总面积
        new_size = get_bk_image_size(total_size, background_img.size, img.size, 250)
        A = BuildImage(
            new_size[0] + 50, new_size[1], background=CASE_BACKGROUND / background
        )
        await A.afilter("GaussianBlur", 2)
        if case:
            case_img = await generate_skin(case, skin2count[f"{case_name}武器箱"])
            if case_img:
                A.paste(case_img, (25, 25), True)
        w = 25
        h = 230
        skin_image_list.reverse()
        for image in skin_image_list:
            A.paste(image, (w, h), True)
            w += image.w + 20
            if w + image.w - 25 > A.w:
                h += image.h + 10
                w = 25
        if h + img_h + 100 < A.h:
            await A.acrop((0, 0, A.w, h + img_h + 100))
        return A
    else:
        log_list = (
            await BuffSkinLog.filter(color="CASE")
            .annotate(count=Count("id"))
            .group_by("case_name")
            .values_list("case_name", "count")
        )
        name2count = {item[0]: item[1] for item in log_list}
        skin_list = await BuffSkin.filter(color="CASE").all()
        image_list: List[BuildImage] = []
        for skin in skin_list:
            if img := await generate_skin(skin, name2count[skin.case_name]):
                image_list.append(img)
        if not image_list:
            return "未收录武器箱"
        w = 25
        h = 150
        img = image_list[0]
        img_w, img_h = img.size
        total_size = (img_w + 25) * (img_h + 10) * len(image_list)  # 总面积

        new_size = get_bk_image_size(total_size, background_img.size, img.size, 155)
        A = BuildImage(
            new_size[0] + 50, new_size[1], background=CASE_BACKGROUND / background
        )
        await A.afilter("GaussianBlur", 2)
        bk_img = BuildImage(
            img_w, 120, color=(25, 25, 25, 100), font_size=60, font="CJGaoDeGuo.otf"
        )
        await bk_img.atext(
            (0, 0), f"已收录 {len(image_list)} 个武器箱", (255, 255, 255), center_type="center"
        )
        await A.apaste(bk_img, (10, 10), True, "by_width")
        for image in image_list:
            A.paste(image, (w, h), True)
            w += image.w + 20
            if w + image.w - 25 > A.w:
                h += image.h + 10
                w = 25
        if h + img_h + 100 < A.h:
            await A.acrop((0, 0, A.w, h + img_h + 100))
        return A


def get_bk_image_size(
    total_size: int,
    base_size: Tuple[int, int],
    img_size: Tuple[int, int],
    extra_height: int = 0,
):
    """获取所需背景大小且不改变图片长宽比


async def util_get_buff_img(case_name: str = "狂牙大行动") -> str:
    cookie = {"session": Config.get_config("open_cases", "COOKIE")}
    error_list = []
    case = cn2py(case_name)
    path = IMAGE_PATH / "cases/" / case
    path.mkdir(exist_ok=True, parents=True)
    case = case.upper()
    CASE_KNIFE = eval(case + "_CASE_KNIFE")
    CASE_RED = eval(case + "_CASE_RED")
    CASE_PINK = eval(case + "_CASE_PINK")
    CASE_PURPLE = eval(case + "_CASE_PURPLE")
    CASE_BLUE = eval(case + "_CASE_BLUE")
    for total_list in [CASE_KNIFE, CASE_RED, CASE_PINK, CASE_PURPLE, CASE_BLUE]:
        for skin in total_list:
            parameter = {"game": "csgo", "page_num": "1", "search": skin}
            if skin in [
                "蝴蝶刀 | 无涂装",
                "求生匕首 | 无涂装",
                "流浪者匕首 | 无涂装",
                "系绳匕首 | 无涂装",
                "骷髅匕首 | 无涂装",
            ]:
                skin = skin.split("|")[0].strip()
            logger.info(f"开始更新----->{skin}")
            skin_name = ""
            # try:
            response = await AsyncHttpx.get(url, proxy=Config.get_config("open_cases", "BUFF_PROXY"), params=parameter)
            if response.status_code == 200:
                data = response.json()["data"]
                total_page = data["total_page"]
                flag = False
                if (
                    skin.find("|") == -1
                ):  # in ['蝴蝶刀', '求生匕首', '流浪者匕首', '系绳匕首', '骷髅匕首']:
                    for i in range(1, total_page + 1):
                        res = await AsyncHttpx.get(url, params=parameter)
                        data = res.json()["data"]["items"]
                        for j in range(len(data)):
                            if data[j]["name"] in [f"{skin}（★）"]:
                                img_url = data[j]["goods_info"]["icon_url"]
                                skin_name = cn2py(skin + "无涂装")
                                await AsyncHttpx.download_file(img_url, path / f"{skin_name}.png")
                                flag = True
                                break
                        if flag:
                            break
                else:
                    img_url = (await response.json())["data"]["items"][0][
                        "goods_info"
                    ]["icon_url"]
                    skin_name += cn2py(skin.replace("|", "-").strip())
                    if await AsyncHttpx.download_file(img_url, path / f"{skin_name}.png"):
                        logger.info(f"------->写入 {skin} 成功")
                    else:
                        logger.info(f"------->写入 {skin} 失败")
    result = None
    if error_list:
        result = ""
        for err_skin in error_list:
            result += err_skin + "\n"
    return result[:-1] if result else "更新图片成功"


async def get_price(d_name):
    cookie = {"session": Config.get_config("open_cases", "COOKIE")}
    name_list = []
    price_list = []
    parameter = {"game": "csgo", "page_num": "1", "search": d_name}
    try:
        response = await AsyncHttpx.get(url, cookies=cookie, params=parameter)
        if response.status_code == 200:
            try:
                data = response.json()["data"]
                total_page = data["total_page"]
                data = data["items"]
                for _ in range(total_page):
                    for i in range(len(data)):
                        name = data[i]["name"]
                        price = data[i]["sell_reference_price"]
                        name_list.append(name)
                        price_list.append(price)
            except Exception as e:
                return "没有查询到...", 998
        else:
            return "访问失败！", response.status_code
    except TimeoutError as e:
        return "访问超时! 请重试或稍后再试!", 997
    result = f"皮肤: {d_name}({len(name_list)})\n"
    for i in range(len(name_list)):
        result += name_list[i] + ": " + price_list[i] + "\n"
    return result[:-1], 999


async def update_count_daily():
    try:
        users = await OpenCasesUser.get_user_all()
        if users:
            for user in users:
                await user.update(
                    today_open_total=0,
                ).apply()
        bot = get_bot()
        gl = await bot.get_group_list()
        gl = [g["group_id"] for g in gl]
        for g in gl:
            try:
                await bot.send_group_msg(group_id=g, message="[[_task|open_case_reset_remind]]今日开箱次数重置成功")
            except ActionFailed:
                logger.warning(f"{g} 群被禁言，无法发送 开箱重置提醒")
        logger.info("今日开箱次数重置成功")
    except Exception as e:
        logger.error(f"开箱重置错误 e:{e}")


@driver.on_startup
async def _():
    """
    将旧表数据移动到新表
    """
    # if not await BuffSkin.first() and await BuffPrice.first():
    #     logger.debug("开始移动旧表数据 BuffPrice -> BuffSkin")
    #     id2name = {1: "狂牙大行动", 2: "突围大行动", 3: "命悬一线", 4: "裂空", 5: "光谱"}
    #     data_list: List[BuffSkin] = []
    #     for data in await BuffPrice.all():
    #         logger.debug(f"移动旧表数据: {data.skin_name}")
    #         case_name = id2name[data.case_id]
    #         name = data.skin_name
    #         is_stattrak = "StatTrak" in name
    #         name = name.replace("（★ StatTrak™）", "").replace("（StatTrak™）", "").strip()
    #         name, skin_name = name.split("|")
    #         abrasion = "无涂装"
    #         if "(" in skin_name:
    #             skin_name, abrasion = skin_name.split("(")
    #             if abrasion.endswith(")"):
    #                 abrasion = abrasion[:-1]
    #         color = get_color(case_name, name.strip(), skin_name.strip())
    #         if not color:
    #             search_list = [
    #                 x
    #                 for x in data_list
    #                 if x.skin_name == skin_name.strip() and x.name == name.strip()
    #             ]
    #             if search_list:
    #                 color = get_color(
    #                     case_name, search_list[0].name, search_list[0].skin_name
    #                 )
    #             if not color:
    #                 logger.debug(
    #                     f"箱子: [{case_name}] 皮肤: [{name}|{skin_name}] 未获取到皮肤品质，跳过..."
    #                 )
    #                 continue
    #         data_list.append(
    #             BuffSkin(
    #                 case_name=case_name,
    #                 name=name.strip(),
    #                 skin_name=skin_name.strip(),
    #                 is_stattrak=is_stattrak,
    #                 abrasion=abrasion.strip(),
    #                 skin_price=data.skin_price,
    #                 color=color,
    #                 create_time=datetime.now(),
    #                 update_time=datetime.now(),
    #             )
    #         )
    #     await BuffSkin.bulk_create(data_list, batch_size=10)
    #     logger.debug("完成移动旧表数据 BuffPrice -> BuffSkin")
