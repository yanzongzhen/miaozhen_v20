#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class BlogHandler(BaseHandler):
    def get(self):
        blogs = []
        self.render('Front/blog/blog.html',blogs=blogs)