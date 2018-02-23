#coding:utf-8
from handlers.Admin_modules.admin.admin_handler import (
    AdminPageHandler,
)

admin_urls = [
    (r'/admin',AdminPageHandler)
]