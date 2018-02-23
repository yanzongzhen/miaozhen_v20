#coding:utf-8

from handlers.base.base_hanlder import BaseHandler

class AdminPageHandler(BaseHandler):
    def get(self):
        self.render('Admin/index.html')

