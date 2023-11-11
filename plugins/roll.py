from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent, GroupMessageEvent, Message
from nonebot.params import CommandArg
from services.log import logger
from configs.config import NICKNAME
import random
import asyncio
import re

__zx_plugin_name__ = "roll"
__plugin_usage__ = """
usage：
    随机数字 或 随机选择事件
    指令：
        roll: 随机 0-100 的数字
        roll *[文本]: 随机事件
        示例：roll 吃饭 睡觉 打游戏
""".strip()
__plugin_des__ = "犹豫不决吗？那就让我帮你决定吧"
__plugin_cmd__ = ["roll", "roll *[文本]"]
__plugin_version__ = 0.1
__plugin_author__ = "HibiKier"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["roll"],
}


roll = on_command("roll", priority=5, block=True)


@roll.handle()
async def _(event: MessageEvent, arg: Message = CommandArg()):
    msg = arg.extract_plain_text().strip().split()
    if not msg:
        await roll.finish(f"roll: {random.randint(0, 100)}", at_sender=True)
    if len(msg) == 1 and (res:=re.match(r"^(\d+)d(\d+)$", msg[0])):
        c = int(res.group(1))
        d = int(res.group(2))
        if c < 1 or c > 10:
            await roll.finish('骰子数量必须是1-10！')
        if d < 2 or d > 100:
            await roll.finish('骰子值必须是2-100！')
            return
        dres = []
        for _ in range(c):
            dres.append(random.randint(1,d))
        await roll.finish(str(dres))

    user_name = event.sender.card or event.sender.nickname
    await roll.send(
        random.choice(
            [
                "转动命运的齿轮，拨开眼前迷雾...",
                f"启动吧，命运的水晶球，为{user_name}指引方向！",
                "嗯哼，在此刻转动吧！命运！",
                f"在此祈愿，请为{user_name}降下指引...",
            ]
        )
    )
    await asyncio.sleep(1)
    x = random.choice(msg)
    await roll.send(
        random.choice(
            [
                f"让{NICKNAME}看看是什么结果！答案是：‘{x}’",
                f"根据命运的指引，接下来{user_name} ‘{x}’ 会比较好",
                f"祈愿被回应了！是 ‘{x}’！",
                f"结束了，{user_name}，命运之轮停在了 ‘{x}’！",
            ]
        )
    )
    logger.info(
        f"(USER {event.user_id}, "
        f"GROUP {event.group_id if isinstance(event, GroupMessageEvent) else 'private'}) 发送roll：{msg}"
    )
