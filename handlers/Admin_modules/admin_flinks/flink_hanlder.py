#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

class FlinkManageHandler(BaseHandler):
    def get(self):
        self.render("Admin/flinks/flink.html")

class AddFlinkHandler(BaseHandler):
    def get(self):
        self.render('Admin/flinks/add-flink.html')

class UpdateFlinkHandler(BaseHandler):
    def get(self):
        self.render('Admin/flinks/update-flink.html')