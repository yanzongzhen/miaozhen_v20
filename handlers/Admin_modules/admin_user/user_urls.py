#coding:utf-8
from handlers.Admin_modules.admin_user.user_handler import (
    ManageUserHandler,
    LoginHandler,
    LoginLogHandler
)

user_urls = [
    (r'/admin/login',LoginHandler),
    (r'/admin/loginlog',LoginLogHandler),
    (r'/admin/manage_user',ManageUserHandler)
]