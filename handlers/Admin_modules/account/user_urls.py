#coding:utf-8
from handlers.Admin_modules.account.user_handler import (
    ManageUserHandler,
    LoginHandler,
    LoginLogHandler,
    AddUserHandler,
    UpdateUserHandler,
    UserSeeHandler, UpdateOtherUserHandler,
    DeleteUserHandler,
    LogoutHandler)

user_urls = [
    (r'/admin/login',LoginHandler),
    (r'/admin/loginout',LogoutHandler),
    (r'/admin/update-info',UpdateUserHandler),
    (r'/admin/update-user',UpdateOtherUserHandler),
    (r'/admin/add_user',AddUserHandler),
    (r'/admin/loginlog',LoginLogHandler),
    (r'/admin/manage_user',ManageUserHandler),
    (r'/User/see',UserSeeHandler),
    (r'/User/delete',DeleteUserHandler)
]