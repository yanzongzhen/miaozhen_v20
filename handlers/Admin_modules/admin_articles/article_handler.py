#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.articles.article_lib import add_article_lib, get_article_list_lib, show_old_article_lib, update_article_lib, \
    del_article_lib

'''文档管理'''
class ArticleManageHandler(BaseHandler):
    def get(self):
        articles,counts = get_article_list_lib(self)
        kw = {
            'articles':articles,
            'counts':counts
        }
        self.render("Admin/articles/article.html",**kw)

class AddArticleHandler(BaseHandler):
    def get(self):
        self.render('Admin/articles/add-article.html')

    def post(self):
        title = self.get_argument('title','')
        content = self.get_argument('content','')
        keywords = self.get_argument('keywords','')
        describe  = self.get_argument('describe','')
        tags  = self.get_argument('tags','')
        result = add_article_lib(self,title,content,keywords,describe,tags)
        if result['status'] is None:
            return self.write({'status': 400, 'msg': result['msg']})
        return self.redirect('/admin/article')

class UpdateArticleHandler(BaseHandler):
    def get(self):
        id = self.get_argument('id','')
        article = show_old_article_lib(self,id)
        self.render('Admin/articles/update-article.html',article=article)

    def post(self):
        title = self.get_argument('title','')
        content = self.get_argument('content','')
        keywords = self.get_argument('keywords','')
        describe  = self.get_argument('describe','')
        tags = self.get_argument('tags','')
        ids = self.get_argument('id', '')
        result = update_article_lib(self,ids,title,content,keywords,describe,tags)
        if result['status'] is None:
            return self.write({'status': 400, 'msg': result['msg']})
        return self.redirect('/admin/article')

class DelArticleHandler(BaseHandler):
    def post(self):
        id = self.get_argument('id','')
        result = del_article_lib(self,id)
        if result['status'] is True:
            return self.redirect('/admin/article')
        return self.write({'status':400,'msg':result['msg']})