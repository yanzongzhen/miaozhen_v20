#coding:utf-8
from sqlalchemy import func

from libs.db.dbsession import dbSession
from models.Blog_model.blog_model import Blog, Comment


def add_blog_lib(self,title,desc,keywords,content):
    if title == '' or desc == '' or keywords == '' or content == '':
        return {'status':False,'msg':'please complete your input'}
    blog = Blog()
    blog.title = title
    blog.content = content
    blog.desc = desc
    blog.keywords = keywords
    self.db.add(blog)
    self.db.commit()
    return {'status': True, 'msg': 'OK'}

def get_bolg_list_lib(self):
    blogs = Blog.all()
    count = dbSession.query(func.count(Blog.id)).scalar()
    return count,blogs

def get_single_blog_lib(self,id):
    return Blog.by_id(id)

def get_list_comments_lib(self,id):
    if id is None:
        return {'status': False, 'msg': '缺少文章ID'}
    blog = Blog.by_id(id)
    if blog is None:
        return {'status': False, 'msg': '文章不存在'}
    blog.readnum += 1
    self.db.add(blog)
    self.db.commit()
    return blog.comments

def modify_blog_lib(self,id,title,desc,content,keywords):
    if title == '' or desc == '' or keywords == '' or content == '':
        return {'status':False,'msg':'please complete your input'}
    blog = Blog.by_id(id)
    blog.title = title
    blog.content = content
    blog.desc = desc
    blog.keywords = keywords
    self.db.add(blog)
    self.db.commit()
    return {'status': True, 'msg': 'OK'}

def del_blog_lib(self,id):
    if Blog.by_id(id):
        blog = Blog.by_id(id)
        dbSession.delete(blog)
        dbSession.commit()
        return {'status':True,'msg':'it is ok'}
    return {'status':False,'msg':'nobody'}


# 评论区
def add_comments_lib(self,Comments,name,email,blog_id):
    if Comments == '' or name == '' or email == '':
        return  {'status':False,'msg':'please complete your input'}
    if blog_id is None:
        return {'status': False, 'msg': '缺少文章ID'}
    blog = Blog.by_id(blog_id)
    if blog is None:
        return {'status': False, 'msg': '文章不存在'}
    comment = Comment()
    comment.content = Comments
    comment.article_id = blog_id
    comment.user_id = self.current_user.id
    comment.name = name
    self.db.add(comment)
    self.db.commit()
    return {'status': True, 'msg': '评论提交成功'}