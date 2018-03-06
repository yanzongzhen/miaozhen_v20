#coding:utf-8
from sqlalchemy import func
from libs.db.dbsession import dbSession
from models.Blog_model.blog_model import Comment

def Commnets_list_lib(self):
    counts = dbSession.query(func.count(Comment.id)).scalar()
    Comments = Comment.all()
    return counts,Comments

def get_single_comment_lib(self,id):
    if id is None:
        return {'status':False,'msg':'评论不存在'}
    comment = Comment.by_id(id)
    comments = {
        'id':comment.id,
        'content':comment.content,
        'name':comment.name
    }
    return {'status':True,'msg':'ok','data':comments}

def  del_comment_lib(self,id):
    if id is None:
        return {'status':False,'msg':'评论不存在'}
    comment = Comment.by_id(id)
    dbSession.delete(comment)
    dbSession.commit()
    return {'status': True, 'msg': 'ok'}