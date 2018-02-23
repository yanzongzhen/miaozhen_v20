#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class NoticeManageHandler(BaseHandler):
    def get(self):
        self.render('Admin/notices/notice.html')


class AddNoticeHandler(BaseHandler):
    def get(self):
        self.render('Admin/notices/add-notice.html')