#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class CommentManageHandler(BaseHandler):
    def get(self):
        self.render('Admin/comments/comments.html')