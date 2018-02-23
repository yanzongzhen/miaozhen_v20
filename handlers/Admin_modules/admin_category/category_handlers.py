#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

'''栏目'''
class CategotyHandler(BaseHandler):
    def get(self):
        self.render('Admin/categorys/category.html')


class UpdateCategoryHandler(BaseHandler):
    def get(self):
        self.render('Admin/categorys/update-category.html')