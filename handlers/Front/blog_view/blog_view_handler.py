#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class BlogViewHandler(BaseHandler):
    def get(self):
        blogs = {}
        comment = {}
        self.render('Front/post/post.html',blog=blogs,comment=comment)