#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.articles.article_lib import get_article_list_lib
from libs.setting.setting_libs import get_list_lib

class MainHandler(BaseHandler):
    def get(self):
        project,counts = get_article_list_lib(self)
        sets = get_list_lib(self)
        kw = {
            'project':project,
            'sets':sets
        }
        self.render('Front/index.html',**kw)
