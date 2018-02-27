#coding:utf-8

from handlers.base.base_hanlder import BaseHandler
from tornado.web import authenticated
from libs.account.account_libs import get_some_info_lib

class AdminPageHandler(BaseHandler):
    @authenticated
    def get(self):
        remote_ip = self.request.remote_ip
        name = self.current_user.name
        result = get_some_info_lib(self,name)
        kw = {
            'remote_ip':remote_ip,
            'users':result
        }
        self.render('Admin/index.html',**kw)

