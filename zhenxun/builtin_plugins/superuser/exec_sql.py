from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me
from nonebot_plugin_alconna import UniMsg
from nonebot_plugin_saa import Image, Text
from nonebot_plugin_session import EventSession
from tortoise import Tortoise

from zhenxun.configs.utils import PluginExtraData
from zhenxun.services.db_context import TestSQL
from zhenxun.services.log import logger
from zhenxun.utils.enum import PluginType
from zhenxun.utils.image_utils import ImageTemplate

__plugin_meta__ = PluginMetadata(
    name="数据库操作",
    description="执行sql语句与查看表",
    usage="""
    查看所有表
    exec [sql语句]
    """.strip(),
    extra=PluginExtraData(
        author="HibiKier",
        version="0.1",
        plugin_type=PluginType.SUPERUSER,
    ).dict(),
)

_matcher = on_command(
    "exec",
    rule=to_me(),
    permission=SUPERUSER,
    priority=1,
    block=True,
)

_table_matcher = on_command(
    "查看所有表",
    rule=to_me(),
    permission=SUPERUSER,
    priority=1,
    block=True,
)

SELECT_TABLE_SQL = """
select a.tablename as name,d.description as desc from pg_tables a
    left join pg_class c on relname=tablename
    left join pg_description d on oid=objoid and objsubid=0 where a.schemaname = 'public'
"""


@_matcher.handle()
async def _(session: EventSession, message: UniMsg):
    sql_text = message.extract_plain_text().strip()
    if sql_text.startswith("exec"):
        sql_text = sql_text[4:].strip()
    if not sql_text:
        await Text("需要执行的的SQL语句!").finish()
    logger.info(f"执行SQL语句: {sql_text}", "exec", session=session)
    try:
        if not sql_text.lower().startswith("select"):
            await TestSQL.raw(sql_text)
        else:
            db = Tortoise.get_connection("default")
            res = await db.execute_query_dict(sql_text)
            _column = []
            for r in res:
                if len(r) > len(_column):
                    _column = r.keys()
            data_list = []
            for r in res:
                data = []
                for c in _column:
                    data.append(r.get(c))
                data_list.append(data)
            table = await ImageTemplate.table_page(
                "EXEC", f"总共有 {len(data_list)} 条数据捏", list(_column), data_list
            )
            await Image(table.pic2bytes()).send()
    except Exception as e:
        logger.error("执行 SQL 语句失败...", session=session, e=e)
        await Text(f"执行 SQL 语句失败... {type(e)}").finish()
    await Text("执行 SQL 语句成功!").finish()


@_table_matcher.handle()
async def _(session: EventSession):
    try:
        db = Tortoise.get_connection("default")
        query = await db.execute_query_dict(SELECT_TABLE_SQL)
        column_name = ["表名", "简介"]
        data_list = []
        for table in query:
            data_list.append([table["name"], table["desc"]])
        logger.info("查看数据库所有表", "查看所有表", session=session)
        table = await ImageTemplate.table_page(
            "数据库表", f"总共有 {len(data_list)} 张表捏", column_name, data_list
        )
        await Image(table.pic2bytes()).send()
    except Exception as e:
        logger.error("获取表数据失败...", session=session, e=e)
        await Text(f"获取表数据失败... {type(e)}").send()
