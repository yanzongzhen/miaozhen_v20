#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class ReadSetHandler(BaseHandler):
    def get(self):
        self.render('Admin/setting/readset.html')



class SettingHandler(BaseHandler):
    def get(self):
        self.render('Admin/setting/setting.html')