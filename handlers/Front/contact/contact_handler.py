#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class ContactHandler(BaseHandler):
    def get(self):
        self.render('Front/contact/contact.html')