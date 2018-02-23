#coding:utf-8
from handlers.base.base_hanlder import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        project = []
        self.render('Front/index.html',project=project)
