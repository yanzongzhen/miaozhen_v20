#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.blog.blog_libs import get_single_blog_lib, add_comments_lib, get_list_comments_lib
from libs.setting.setting_libs import get_list_lib


class BlogViewHandler(BaseHandler):
    def get(self):
        id = self.get_argument('blog_id','')
        blogs = get_single_blog_lib(self,id)
        comments = get_list_comments_lib(self,id)
        sets = get_list_lib(self)
        kw = {
            'blog':blogs,
            'comments':comments,
            'sets':sets
        }
        self.render('Front/post/post.html',**kw)


class CommentHandler(BaseHandler):
    def post(self):
        Comments = self.get_argument('Comments','')
        name = self.get_argument('name','')
        email = self.get_argument('email','')
        blog_id = self.get_argument('blog_id','')
        result = add_comments_lib(self,Comments,name,email,blog_id)
        if result['status'] is True:
            return self.write({'status':200,'msg':result['msg']})
        return self.write({'status':400,'msg':result['msg']})
