#coding:utf-8
from uuid import uuid4

from sqlalchemy import func

from libs.db.dbsession import dbSession
from models.article_model.article_model import Article

def add_article_lib(self,title,content,keywords,describe,tags,url):
    if title == "" or content == "" or keywords == "" or describe == "" or tags == "":
        return {'status':False,'msg':'请补全信息'}
    article = Article()
    article.tags = tags
    article.keywords=keywords
    article.title = title
    article.desc =describe
    article.article_pic_name = url
    article.content = content
    self.db.add(article)
    self.db.commit()
    return {'status': True, 'msg': 'OK'}

def get_article_list_lib(self):
    counts = dbSession.query(func.count(Article.id)).scalar()
    articles = Article.all()
    return articles,counts

def show_old_article_lib(self,id):
    article = Article.by_id(id)
    return article


def update_article_lib(self,ids,title,content,keywords,describe,tags,url):
    if title == "" or content == "" or describe == "":
        return {'status':False,'msg':'请补全信息'}
    article = Article.by_id(ids)
    article.tags = tags
    article.article_pic_name=url
    article.keywords = keywords
    article.title = title
    article.desc = describe
    article.content = content
    self.db.add(article)
    self.db.commit()
    return {'status':True, 'msg': 'OK'}


def del_article_lib(self,id):
    article = Article.by_id(id)
    dbSession.delete(article)
    dbSession.commit()
    return {'status':True,'msg':'delete ok'}

def show_article_id_detail_lib(self,id):
    return Article.by_id(id)