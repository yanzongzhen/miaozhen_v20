#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class AboutHandler(BaseHandler):
    def get(self):
        self.render('Front/about/about.html')