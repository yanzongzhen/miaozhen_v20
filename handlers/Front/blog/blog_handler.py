#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.setting.setting_libs import get_list_lib


class BlogHandler(BaseHandler):
    def get(self):
        blogs = []
        sets = get_list_lib(self)
        kw = {
            'blogs':blogs,
            'sets':sets
        }
        self.render('Front/blog/blog.html',**kw)