#coding:utf-8
from handlers.base.base_hanlder import BaseHandler

'''文档管理'''
class ArticleManageHandler(BaseHandler):
    def get(self):
        self.render("Admin/articles/article.html")

class AddArticleHandler(BaseHandler):
    def get(self):
        self.render('Admin/articles/add-article.html')

class UpdateArticleHandler(BaseHandler):
    def get(self):
        self.render('Admin/articles/update-article.html')