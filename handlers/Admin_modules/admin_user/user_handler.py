#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class ManageUserHandler(BaseHandler):
    def get(self):
        self.render('Admin/usermanages/manage-user.html')


class LoginHandler(BaseHandler):
    def get(self):
        self.render('Admin/usermanages/login.html')


class LoginLogHandler(BaseHandler):
    def get(self):
        self.render('Admin/usermanages/loginlog.html')