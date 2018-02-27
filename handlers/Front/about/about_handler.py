#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.setting.setting_libs import get_list_lib


class AboutHandler(BaseHandler):
    def get(self):
        sets = get_list_lib(self)
        self.render('Front/about/about.html',sets=sets)