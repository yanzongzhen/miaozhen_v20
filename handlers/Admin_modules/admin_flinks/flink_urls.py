#coding:utf-8
from handlers.Admin_modules.admin_flinks.flink_hanlder import (
    AddFlinkHandler,
    FlinkManageHandler,
    UpdateFlinkHandler
)

flink_urls = [
    (r'/admin/flink', FlinkManageHandler),
    (r'/admin/add_flink', AddFlinkHandler),
    (r'/admin/update_flink', UpdateFlinkHandler)
]