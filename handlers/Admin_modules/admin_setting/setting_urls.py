#coding:utf-8
from handlers.Admin_modules.admin_setting.setting_handler import (
    SettingHandler,
    ReadSetHandler
)

set_urls  = [
    (r'/admin/readset',ReadSetHandler),
    (r'/admin/setting',SettingHandler)
]