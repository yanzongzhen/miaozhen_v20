#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class ProjectViewHandler(BaseHandler):
    def get(self):
        self.render('Front/project/project.html')