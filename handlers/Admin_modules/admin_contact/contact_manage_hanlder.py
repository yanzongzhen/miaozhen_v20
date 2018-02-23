#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class ContactManageHandler(BaseHandler):
    def get(self):
        self.render('Admin/contact/contact.html')