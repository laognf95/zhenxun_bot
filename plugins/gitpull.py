from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from services.log import logger
from configs.config import Config
from git.repo import Repo


__zx_plugin_name__ = "拉取git仓库 [Superuser]"
__plugin_usage__ = """
usage：
    拉取指定的git仓库
    这是一个阻塞命令，注意不要经常调用...
    指令：
        gitpull
""".strip()
__plugin_des__ = "拉取仓库"
__plugin_cmd__ = ["gitpull [_superuser]"]
__plugin_version__ = 0.1
__plugin_author__ = "laognf95"
__plugin_settings__ = {
    "cmd": ["gitpull"],
}
__plugin_configs__ = {
    "GIT_REMOTE": {"value": 'origin', "help": "gitremote", "default_value": 'origin'},
    "GIT_BRANCHES": {"value": 'master', "help": "git分支", "default_value": 'master'},
}
__plugin_block_limit__ = {
    "rst": "正在拉取..."
}

withdraw_msg = on_command("gitpull", priority=5, block=True, permission=SUPERUSER)

@withdraw_msg.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    remote = Config.get_config(
            "gitpull", "GIT_REMOTE"

        )
    branches = Config.get_config(
            "gitpull", "GIT_BRANCHES"
        )
    repo = Repo('.')
    _remote = repo.remote(remote)
    try:
        _remote.fetch()
    except:
        await withdraw_msg.finish(f'仓库连接失败..')
    repo.git.checkout(branches)
    _remote.pull(branches)
    await withdraw_msg.send(f'更新成功')
    logger.info(
        f"(USER {event.user_id}, GROUP {event.group_id if isinstance(event, GroupMessageEvent) else 'private'}) gitpull！"
    )