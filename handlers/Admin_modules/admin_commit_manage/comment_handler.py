#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.comment.comment_libs import Commnets_list_lib, get_single_comment_lib, del_comment_lib


class CommentManageHandler(BaseHandler):
    def get(self):
        counts,comments = Commnets_list_lib(self)
        kw = {
            'counts':counts,
            'comments':comments
        }
        self.render('Admin/comments/comments.html',**kw)

class CommentSeeHandler(BaseHandler):
    def post(self):
        id = self.get_argument('id','')
        result = get_single_comment_lib(self,id)
        if result['status'] is True:
            return self.write({'status':200,'msg':'ok','data':result['data']})
        return self.write({'status':400, 'msg': 'error'})

class DelCommentHandler(BaseHandler):
    def post(self):
        id = self.get_argument('id','')
        result = del_comment_lib(self,id)
        if result['status'] is True:
            return self.write({'status':200,'msg':'ok'})
        return self.write({'status':400, 'msg': 'error'})