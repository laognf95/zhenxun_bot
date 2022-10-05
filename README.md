<div align=center><img width="320" height="320" src="https://raw.githubusercontent.com/HibiKier/zhenxun_bot/main/logo.png"/></div>

![maven](https://img.shields.io/badge/python-3.8%2B-blue)
![maven](https://img.shields.io/badge/nonebot-2.0.0-yellow)
![maven](https://img.shields.io/badge/go--cqhttp-1.0.0-red)

# 绪山真寻Bot
****
此项目基于 Nonebot2 和 go-cqhttp 开发，以 postgresql 作为数据库的QQ群娱乐机器人
## 关于
用爱发电，某些功能学习借鉴了大佬们的代码，因为绪山真寻实在太可爱了因此开发了
绪山真寻bot，实现了一些对群友的娱乐功能和实用功能（大概）。

如果该项目的图片等等侵犯猫豆腐老师权益请联系我删除！  

是新手！希望有个地方讨论绪山真寻Bot，或者有问题或建议，可以发送issues或加入[ <strong>[是真寻酱哒(萌新版)](https://jq.qq.com/?_wv=1027&k=u8PgBkMZ) </strong>]

[//]: # (是老手！讨论插件开发，nonebot2开发，可以加入[ <strong>[真寻酱的技术群]&#40;https://jq.qq.com/?_wv=1027&k=u8PgBkMZ&#41; </strong>])

## 声明
此项目仅用于学习交流，请勿用于非法用途

# Nonebot2
<img style="height: 200px;width: 200px;" src="https://camo.githubusercontent.com/0ef71e86056da694c540790aa4a4e314396884d6c4fdb95362a7538b27a1b034/68747470733a2f2f76322e6e6f6e65626f742e6465762f6c6f676f2e706e67">

非常 [ **[NICE](https://github.com/nonebot/nonebot2)** ] 的OneBot框架

## 未完成的文档

# [传送门](https://hibikier.github.io/zhenxun_bot/)

## 真寻的帮助
请对真寻说: '真寻帮助' or '管理员帮助' or '超级用户帮助' or '真寻帮助 指令'

## 普通帮助图片
![x](https://github.com/HibiKier/zhenxun_bot/blob/0.0.8.2/docs_image/3238573864-836268675-E2FFBB2AC143EAF4DDDF150438508721.png)

## Web UI
[zhenxun_bot_webui](https://github.com/HibiKier/zhenxun_bot_webui)

## 一键安装脚本
[zhenxun_bot-deploy](https://github.com/AkashiCoin/zhenxun_bot-deploy)

## 提供符合真寻标准的插件仓库

[AkashiCoin/nonebot_plugins_zhenxun_bot](https://github.com/AkashiCoin/nonebot_plugins_zhenxun_bot)

## 来点优点？

  * 实现了许多功能，且提供了大量功能管理命令
  * 通过Config配置项将所有插件配置统计保存至config.yaml，利于统一用户修改
  * 方便增删插件，原生nonebot2 matcher，不需要额外修改，仅仅通过简单的配置属性就可以生成`帮助图片`和`帮助信息`
  * 提供了cd，阻塞，每日次数等限制，仅仅通过简单的属性就可以生成一个限制，例如：`__plugin_cd_limit__`
  * __..... 更多详细请通过`传送门`查看文档！__


## 功能列表
<details>
<summary>已实现的功能</summary>

### 已实现的常用功能
- [x] 昵称系统（群与群与私聊分开.）
- [x] 图灵AI（会把'你'等关键字替换为你的昵称），且带有 [AnimeThesaurus](https://github.com/Kyomotoi/AnimeThesaurus)，够味
- [x] 签到/我的签到/好感度排行/好感度总排行（影响色图概率和开箱次数，支持配置）
- [x] 发送某文件夹下的随机图片（支持自定义，默认：美图，萝莉，壁纸）
- [x] 色图（这不是基础功能嘛喂）
- [x] coser
- [x] 黑白草图生成器
- [x] 鸡汤/语录
- [x] 骂我（钉宫语音）
- [x] 戳一戳（概率发送美图，钉宫语音或者戳回去）
- [x] 模拟开箱/我的开箱/群开箱统计/我的金色/设置cookie（csgo，内置爬虫脚本，需要提前抓取数据和图片，需要session，可能需要代理，阿里云服务器等ip也许已经被ban了（我无代理访问失败），如果访问太多账号API调用可能被禁止访问api！）
- [x] 鲁迅说过
- [x] 构造假消息（自定义的分享链接）
- [x] 商店/我的金币/购买道具/使用道具
- [x] 8种手游抽卡 (查看 [nonebot_plugin_gamedraw](https://github.com/HibiKier/nonebot_plugin_gamedraw))
- [x] 我有一个朋友想问问..（借鉴pcrbot插件）
- [x] 原神黄历
- [x] 原神今日素材
- [x] 原神资源查询  (借鉴[Genshin_Impact_bot](https://github.com/H-K-Y/Genshin_Impact_bot)插件)
- [x] 原神便笺查询
- [x] 原神玩家查询
- [x] 原神树脂提醒
- [x] 原神签到/自动签到
- [x] 金币红包
- [x] 微博热搜
- [x] B站主播/UP/番剧订阅

- [x] pil对图片的一些操作
- [x] BUFF饰品底价查询（需要session）
- [x] 天气查询
- [x] 疫情查询
- [x] bt磁力搜索（咳咳，这功能我想dddd）
- [x] reimu搜索（上车） (使用[XUN_Langskip](https://github.com/Angel-Hair/XUN_Bot)的插件)
- [x] 靠图识番  (使用[XUN_Langskip](https://github.com/Angel-Hair/XUN_Bot)的插件)
- [x] 以图搜图 (使用[nonebot_plugin_picsearcher](https://github.com/synodriver/nonebot_plugin_picsearcher)插件)
- [x] 搜番
- [x] 点歌  [nonebot_plugin_songpicker2](https://github.com/maxesisn/nonebot_plugin_songpicker2)插件（删除了选歌和评论）
- [x] epic免费游戏
- [x] p站排行榜
- [x] p站搜图
- [x] 翻译（日英韩）
- [x] pix图库（一个自己的图库，含有增删查改，黑名单等命令）

- [x] 查看当前群欢迎消息
- [x] 查看该群自己的权限
- [x] 我的信息（只是为了看看什么时候入群）
- [x] 更新信息（如果继续更新的话）
- [x] go-cqhttp最新版下载和上传（不需要请删除）
- [x] 撤回
- [x] 滴滴滴-（用户对超级用户发送消息）
- [x] 金币红包/金币排行
- [x] 俄罗斯轮盘/胜场排行/败场排行/欧洲人排行/慈善家排行
- [x] 网易云热评
- [x] 念首古诗
- [x] 获取b站视频封面
- [x] 通过PID获取图片
- [x] 功能统计可视化
- [x] 词云
- [x] 关于

### 已实现的管理员功能
- [x] 更新群组成员信息
- [x] 95%的群功能开关
- [x] 查看群内被动技能状态
- [x] 自定义群欢迎消息（是真寻的不是管家的！）
- [x] .ban/.unban（支持设置ban时长）= 黑白名单
- [x] 刷屏禁言相关：刷屏检测设置/设置禁言时长/设置检测次数
- [x] 上传图片/连续上传图片 （上传图片至指定图库）
- [x] 移动图片  （同上）
- [x] 删除图片  （同上）
- [x] 群内B站订阅
- [x] 词条设置
- [x] 休息吧/醒来

### 已实现的超级用户功能
- [x] 添加/删除权限（是真寻的管理员权限，不是群管理员）
- [x] 开启/关闭指定群的广播通知
- [x] 广播
- [x] 自检（检查系统状态）
- [x] 所有群组/所有好友
- [x] 退出指定群
- [x] 更新好友信息/更新群信息
- [x] /t（对用户进行回复或发送消息）
- [x] 上传/删除/修改商品（需要编写对应的商品功能）
- [x] 节日红包发送
- [x] 修改群权限
- [x] ban
- [x] 更新色图
- [x] 更新价格/更加图片（csgo开箱）
- [x] 重载原神/方舟/赛马娘/坎公骑冠剑卡池
- [x] 更新原神今日素材/更新原神资源信息
- [x] PIX相关操作
- [x] 检查更新真寻
- [x] 重启
- [x] 添加/删除/查看群白名单
- [x] 功能开关(更多设置)
- [x] 功能状态
- [x] b了
- [x] 执行sql
- [x] 重载配置
- [x] 清理临时数据
- [x] 增删群认证
- [x] 同意/拒绝好友/群聊请求
- [x] 配置重载

#### 超级用户的被动技能
- [x] 邀请入群提醒(别人邀请真寻入群)
- [x] 添加好友提醒(别人添加真寻好友)

### 已实现的被动技能
- [x] 进群欢迎消息
- [x] 群早晚安
- [x] 每日开箱重置提醒
- [x] b站转发解析（解析b站分享信息，支持bv，bilibili链接，b站手机端转发卡片，cv，b23.tv），且5分钟内不解析相同url
- [x] 丢人爬（爬表情包）
- [x] epic通知（每日发送epic免费游戏链接）
- [x] 原神黄历提醒
- [x] 复读

### 已实现的看不见的技能！
- [x] 刷屏禁言检测
- [x] 功能调用统计
- [x] 检测恶意触发命令（将被最高权限ban掉30分钟，只有最高权限(9级)可以进行unban）
- [x] 自动同意好友请求，加群请求将会提醒管理员，退群提示，加群欢迎等等
- [x] 群聊时间检测（当群聊最后一人发言时间大于当前36小时后将关闭该群所有通知（即被动技能））
- [x] 群管理员监控，自动为新晋管理员增加权限，为失去群管理员的用户删除权限
- [x] 群权限系统
- [x] 定时更新权限
- [x] 自动配置重载
</details>

## 详细配置请前往文档，以下为最简部署和配置，如果你有基础并学习过nonebot2的话


## 简单部署

```

# 配置gocq

在 https://github.com/Mrs4s/go-cqhttp 下载Releases最新版本，运行后选择反向代理，
  后将gocq的配置文件config.yml中的universal改为universal: ws://127.0.0.1:8080/onebot/v11/ws

# 获取代码
git clone https://github.com/HibiKier/zhenxun_bot.git

# 进入目录
cd zhenxun_bot

# 安装依赖
pip install poetry      # 安装 poetry
poetry install          # 安装依赖

# 进行基础配置
####请查看 配置 部分####

# 开始运行
poetry shell            # 进入虚拟环境
python bot.py
```

## 简单配置

```
1.在.env.dev文件中

  SUPERUSERS = [""]   # 填写你的QQ

2.在configs/config.py文件中
  * 数据库配置

3.在configs/config.yaml文件中 # 该文件需要启动一次后生成
  * 修改插件配置项

```


## 使用Docker
__Docker 单机版（仅真寻Bot）__  
**点击下方的 GitHub 徽标查看教程**  
[![Github](https://shields.io/badge/GITHUB-Sakuracio-4476AF?logo=github&style=for-the-badge)](https://github.com/Sakuracio/zhenxun_bot_docker)  
[![DOCKER](https://shields.io/badge/docker-hibikier/zhenxun_bot-4476AF?logo=docker&style=for-the-badge)](https://hub.docker.com/r/hibikier/zhenxun_bot)  
__Docker 全量版（包含 真寻Bot PostgreSQL数据库 go-cqhttp webui等）__  
[![Github](https://shields.io/badge/GITHUB-SinKy--Yan-4476AF?logo=github&style=for-the-badge)](https://github.com/SinKy-Yan/zhenxunbot-docker)  
[![DOCKER](https://shields.io/badge/docker-jyishit/zhenxun_bot-4476AF?logo=docker&style=for-the-badge)](https://hub.docker.com/r/jyishit/zhenxun_bot)  
**点击上方的 GitHub 徽标查看教程**  
PS: **ARM平台** 请使用全量版 同时 **如果你的机器 RAM < 1G 可能无法正常启动全量版容器**

## [爱发电](https://afdian.net/@HibiKier)
<details>
<summary>爱发电 以及 感谢投喂 </summary>
<img width="365px" height="450px" src="https://user-images.githubusercontent.com/45528451/175059389-cfeb8174-fa07-4939-80ab-a039087a50f6.png">

### 感谢名单
(可以告诉我你的 __github__ 地址，我偷偷换掉0v|)  
[Kafka](https://afdian.net/u/41d66798ef6911ecbc5952540025c377)
[墨然](https://afdian.net/u/8aa5874a644d11eb8a6752540025c377)
[爱发电用户_T9e4](https://afdian.net/u/2ad1bb82f3a711eca22852540025c377)
[笑柒XIAO_Q7](https://afdian.net/u/4696db5c529111ec84ea52540025c377)
[noahzark](https://afdian.net/a/noahzark)
[腊条](https://afdian.net/u/f739c4d69eca11eba94b52540025c377)  
[ze roller](https://afdian.net/u/0e599e96257211ed805152540025c377)  
[爱发电用户_4jrf](https://afdian.net/u/6b2cdcc817c611ed949152540025c377)  
[爱发电用户_TBsd](https://afdian.net/u/db638b60217911ed9efd52540025c377)  
[烟寒若雨](https://afdian.net/u/067bd2161eec11eda62b52540025c377)  
[ln](https://afdian.net/u/b51914ba1c6611ed8a4e52540025c377)  
[爱发电用户_b9S4](https://afdian.net/u/3d8f30581a2911edba6d52540025c377)  
[爱发电用户_c58s](https://afdian.net/u/a6ad8dda195e11ed9a4152540025c377)  
[爱发电用户_eNr9](https://afdian.net/u/05fdb41c0c9a11ed814952540025c377)   
[MangataAkihi](https://github.com/Sakuracio)   
[炀](https://afdian.net/u/69b76e9ec77b11ec874f52540025c377)   
[爱发电用户_Bc6j](https://afdian.net/u/8546be24f44111eca64052540025c377)   1114
[大魔王](https://github.com/xipesoy)   
[CopilotLaLaLa](https://github.com/CopilotLaLaLa)  
[嘿小欧](https://afdian.net/u/daa4bec4f24911ec82e552540025c377)   
[回忆的秋千](https://afdian.net/u/e315d9c6f14f11ecbeef52540025c377)  
[十年くん](https://github.com/shinianj)
[哇](https://afdian.net/u/9b266244f23911eca19052540025c377)  
[yajiwa](https://github.com/yajiwa)  
[爆金币](https://afdian.net/u/0d78879ef23711ecb22452540025c377)  


</details>


## 更新

* 订阅up动态提供直链

* 修复b站订阅 [@pull/1112](https://github.com/HibiKier/zhenxun_bot/pull/1112)
* fix: 重载赛马娘卡池失败 [@pull/1114](https://github.com/HibiKier/zhenxun_bot/pull/1114)

### 2022/9/19

* 更换bilibili_sub获取用户昵称用的API&尝试修了一下get_video() [@pull/1097](https://github.com/HibiKier/zhenxun_bot/pull/1097)
* 修复csgo每日开箱可以多开一次

### 2022/9/18

* 修复 bilireq 版本过低导致 B 站视频解析错误 [@pull/1090](https://github.com/HibiKier/zhenxun_bot/pull/1096)

### 2022/9/16

* fix: bilibili_sub, azur_draw_card [@pull/1090](https://github.com/HibiKier/zhenxun_bot/pull/1090)
* 修复原神资源查询查询完毕后图片存储错误
* b站订阅发送 与 b站订阅 使用相同开关，即：关闭b站订阅

### 2022/9/10

* 自定义群欢迎消息参数不完全时提示报错
* 修改bt插件的url地址 [@pull/1067](https://github.com/HibiKier/zhenxun_bot/pull/1067)

### 2022/9/8

* 添加插件数据初始化判断

* BagUser提供方法`check_props`方法，用于判断用户是否含有该道具并是否使用
* 优化商品显示图片，提供限制，限购，折扣提示
* 修复图库内图片无法被连续删除的问题 [@pull/879](https://github.com/HibiKier/zhenxun_bot/pull/879)
* 色图提供配置项`MAX_ONCE_NUM2FORWARD`：群聊中单次发送图片数量达到指定时使用合并转发
* 优化修复了商品修改命令
* B站订阅UP动态改为详情页截图

### 2022/6/28

* 修复色图插件api修改无法搜索图片 [@pull/866](https://github.com/HibiKier/zhenxun_bot/pull/866)

### 2022/6/26

* 替换了bt URL
* PIX当使用pid查询图片时，会发送该pid下所有图片
* 商店提供了每日购买次数限制

### 2022/6/24

* 对WSL虚拟机 代理 添加写法 [@pull/847](https://github.com/HibiKier/zhenxun_bot/pull/847)

### 2022/6/21

* update parse_bilibili [@pull/840](https://github.com/HibiKier/zhenxun_bot/pull/840)

### 2022/6/19 \[v0.1.6.0]

* 暂时使用hook修复webui中plugins2setting修改时会改变plugins2setting.cmd为字符串
* 修复原神树脂重复提醒的bug [@pull/828](https://github.com/HibiKier/zhenxun_bot/pull/828)
* 词条优化问题展示,修改含机器人昵称和@逻辑 [@pull/835](https://github.com/HibiKier/zhenxun_bot/pull/835)

### 2022/6/18

* 修复昵称系统`BLACK_WORD`为空时造成报错
* 修复特殊头像时背景透明化出错
* 修复text2image纯文本时换行时颜色不统一
* 优化webUI，当有插件出错时不会影响其他插件显示
* 优化Config类型注释 [@pull/830](https://github.com/HibiKier/zhenxun_bot/pull/830)
* 优化browser

### 2022/6/17

* 修复wordbank的一些小问题 @pull/820

### 2022/6/14

* AsyncHttpx提供可关闭 ssl 验证参数 [@pull/812](https://github.com/HibiKier/zhenxun_bot/pull/812)
* fix: 自动更新群组 [@pull/810](https://github.com/HibiKier/zhenxun_bot/pull/810)
* fix: 修复添加词条时对answer中图片的处理 [@pull/806](https://github.com/HibiKier/zhenxun_bot/pull/806)
* 修复pix中指定num无法生效
* 替换了bt URL

### 2022/6/13

* Windows 重启适配 [@pull/804](https://github.com/HibiKier/zhenxun_bot/pull/804)
* 色图等提供修改md5方法 [@pull/800](https://github.com/HibiKier/zhenxun_bot/pull/800)
* webui中token.json文件写入补充 [@pull/798](https://github.com/HibiKier/zhenxun_bot/pull/798)
* 修复识图某些图片可能会出错

### 2022/6/11

* pix当只有一个tag时且为数字时可以通过添加'#'防止判定为数量

### 2022/6/9

* 修复b站订阅同群二人以上相同订阅时发送多次信息
* 修复超级用户帮助中缺少了 ‘插件商店’ 相关帮助
* 昵称系统提供了详细帮助

### 2022/6/5 \[v0.1.5.9]

* webui修复plugin2setting中cmd从list转变为str
* 当命令`我的金币`被风控时将以图片形式发送
* fix gold_redbag [@pull/763](https://github.com/HibiKier/zhenxun_bot/pull/763)
* 金币红包功能增加更多封面 [@pull/764](https://github.com/HibiKier/zhenxun_bot/pull/764)

### 2022/6/3

* 插件仓库在已安装插件边上会提示\[已安装]
* 修复ShopRegister kwargs某些字段无效
* 调整了一下查看所有请求中的年龄绘制 [@pull/745](https://github.com/HibiKier/zhenxun_bot/pull/745)
* 修复原神树脂提醒bug [@pull/756](https://github.com/HibiKier/zhenxun_bot/pull/756)

### 2022/5/31

* 修复开启/关闭全部功能时帮助图片未重绘 [@pull/721](https://github.com/HibiKier/zhenxun_bot/pull/721)
* bot_friend_group将group_handle.修改为friend_handle. [@pull/711](https://github.com/HibiKier/zhenxun_bot/pull/711)
* 修复发红包图片背景未透明化;修复原神树脂提醒参数错误 [@pull/712](https://github.com/HibiKier/zhenxun_bot/pull/712)
* 修复抽卡插件：方舟更新UP池信息时，若公告的第一个池子过期会导致无法更新UP池信息 [@pull/707](https://github.com/HibiKier/zhenxun_bot/pull/707)
* 商店插件判断是否有requirements.txt文件 [@pull/705](https://github.com/HibiKier/zhenxun_bot/pull/705)
* 删除原神玩家查询api返回变更的多余键值
* 优化了text2image方法

### 2022/5/29 \[v0.1.5.8]

* 提供了真寻适配仓库的插件 安装/卸载 操作
* 暂时关闭了插件资源清空
* 通过指令安装插件时会在插件目录下生成plugin_info.json记录当前插件信息

### 2022/5/28

* 修复私聊无法添加昵称
* 修复原神玩家查询层岩巨渊地下矿区没开时报错
* 修复 ```休息吧``` 无法阻断戳一戳
* 当图库无图片时，戳一戳将略过发送图片
* 新增搜图提供配置项```ALLOW_GROUP_R18```：允许在群聊中使用r18参数
* 新增自动更新插件```UPDATE_REMIND```：新版本提醒，原配置项```AUTO_UPDATE_ZHENXUN```改为自动更新升级
* black_word新增当群权限为-1时不再检测该群
* 修复非超级用户绑定原神cookie会被black_word阻拦
* 修复微博热搜报错,发红包小bug [@pull/688](https://github.com/HibiKier/zhenxun_bot/pull/688)
* 更多的中文提示

### 2022/5/26

* 修复\[滴滴滴]会被转义成&#91;滴滴滴&#93;导致无法触发的问题
* 将一些错误以中文提示输出
* 更新BT搜索源地址 [@pull/668](https://github.com/HibiKier/zhenxun_bot/pull/668)
* 更新抽卡插件 [@pull/667](https://github.com/HibiKier/zhenxun_bot/pull/667)

### 2022/5/25

* 修复webui中CountLimit字段limit_type类型错误
* 修改nickname插件：一处文案错误，添加敏感词 [@pull/624](https://github.com/HibiKier/zhenxun_bot/pull/624)
* gamedraw的ba卡池搬运了过来并且进行了真寻的适配 [@pull/617](https://github.com/HibiKier/zhenxun_bot/pull/617)
* feat: stream downloading and progress [@pull/607](https://github.com/HibiKier/zhenxun_bot/pull/607)
* 修改翻译插件，添加缺失的冒号 [@pull/602](https://github.com/HibiKier/zhenxun_bot/pull/602)
* 修复碧蓝航线/明日方舟up池解析出错的问题 [@pull/610](https://github.com/HibiKier/zhenxun_bot/pull/602)

### 2022/8/14

* 修复epic未获取到时间时出错
* 修复订阅主播时动态获取的id是直播间id

### 2022/8/8

* 修复赛马娘重载卡池失败的问题 [@pull/969](https://github.com/HibiKier/zhenxun_bot/pull/969)

### 2022/8/3

* 修复 bili动态链接在投稿视频时URL和分割线连在一起 [@pull/951](https://github.com/HibiKier/zhenxun_bot/pull/961)
* 更新 Epic 免费游戏商城链接拼接规则 [@pull/957](https://github.com/HibiKier/zhenxun_bot/pull/957)

### 2022/8/6

* 修复了原神自动签到返回invalid request的问题，新增查看我的cookie命令 [@pull/971](https://github.com/HibiKier/zhenxun_bot/pull/971)

<br>

__..... 更多更新信息请查看文档__

## Todo
- [x] web管理

## 感谢
[botuniverse / onebot](https://github.com/botuniverse/onebot) ：超棒的机器人协议  
[Mrs4s / go-cqhttp](https://github.com/Mrs4s/go-cqhttp) ：cqhttp的golang实现，轻量、原生跨平台.  
[nonebot / nonebot2](https://github.com/nonebot/nonebot2) ：跨平台Python异步机器人框架  
[Angel-Hair / XUN_Bot](https://github.com/Angel-Hair/XUN_Bot) ：一个基于NoneBot和酷Q的功能性QQ机器人  
[pcrbot / cappuccilo_plugins](https://github.com/pcrbot/cappuccilo_plugins) ：hoshino插件合集  
[MeetWq /nonebot-plugin-withdraw](https://github.com/MeetWq/nonebot-plugin-withdraw) ：A simple withdraw plugin for Nonebot2  
[maxesisn / nonebot_plugin_songpicker2](https://github.com/maxesisn/nonebot_plugin_songpicker2) ：适用于nonebot2的点歌插件  
[nonepkg / nonebot-plugin-manager](https://github.com/nonepkg/nonebot-plugin-manager) ：Nonebot Plugin Manager base on import hook  
[H-K-Y / Genshin_Impact_bot](https://github.com/H-K-Y/Genshin_Impact_bot) ：原神bot，这是一个基于nonebot和HoshinoBot的原神娱乐及信息查询插件  
[NothAmor / nonebot2_luxun_says](https://github.com/NothAmor/nonebot2_luxun_says) ：基于nonebot2机器人框架的鲁迅说插件  
[Kyomotoi / AnimeThesaurus](https://github.com/Kyomotoi/AnimeThesaurus) ：一个~~特二刺螈~~（文爱）的适用于任何bot的词库  
[Ailitonia / omega-miya](https://github.com/Ailitonia/omega-miya) ：基于nonebot2的qq机器人  
[KimigaiiWuyi / GenshinUID](https://github.com/KimigaiiWuyi/GenshinUID) ：一个基于HoshinoBot/NoneBot2的原神UID查询插件
