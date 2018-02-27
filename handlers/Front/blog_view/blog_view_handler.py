#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.setting.setting_libs import get_list_lib


class BlogViewHandler(BaseHandler):
    def get(self):
        blogs = {}
        comment = {}
        sets = get_list_lib(self)
        kw = {
            'blogs':blogs,
            'comment':comment,
            'sets':sets
        }
        self.render('Front/post/post.html',**kw)