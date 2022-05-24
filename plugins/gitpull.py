from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from services.log import logger
from configs.config import Config
from git.repo import Repo
from git.exc import GitCommandError


__zx_plugin_name__ = "拉取git仓库 [Superuser]"
__plugin_usage__ = """
usage：
    拉取指定的git仓库
    这是一个阻塞命令，注意不要经常调用...
    remote需要事先在本地仓库配置好..既然用这个插件，这一点应该是常识吧（
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
    "GIT_REMOTE": {"value": 'origin', "help": "选择remote，需要事先在本地仓库配置好", "default_value": 'origin'},
    "GIT_BRANCHES": {"value": 'dev', "help": "git分支，推荐远程修改在开发分支上", "default_value": 'dev'},
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
    if remote is None or remote == '' or branches is None or branches == '':
        await withdraw_msg.finish(f'请先在配置文件中配置参数..')
    repo = Repo('.')
    _remote = repo.remote(remote)
    try:
        _remote.fetch()
    except GitCommandError:
        await withdraw_msg.finish(f'仓库连接失败..')
    try:
        repo.git.checkout(branches)
    except GitCommandError:
        await withdraw_msg.finish(f'分支{branches}不存在..')
    _remote.pull(branches)
    await withdraw_msg.send(f'更新成功')
    logger.info(
        f"(USER {event.user_id}, GROUP {event.group_id if isinstance(event, GroupMessageEvent) else 'private'}) gitpull！"
    )