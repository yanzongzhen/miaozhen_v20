#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.blog.blog_libs import add_blog_lib, get_bolg_list_lib, get_single_blog_lib, modify_blog_lib, del_blog_lib


class NoticeManageHandler(BaseHandler):

    def get(self):
        count, blogs = get_bolg_list_lib(self)
        kw = {
            'count': count,
            'blogs': blogs
        }
        self.render('Admin/notices/notice.html',**kw)


class AddNoticeHandler(BaseHandler):
    def get(self):
        self.render('Admin/notices/add-notice.html')

    def post(self):
        title = self.get_argument('title','')
        keywords = self.get_argument('keywords','')
        desc = self.get_argument('desc','')
        content = self.get_argument('content','')
        result = add_blog_lib(self,title,desc,keywords,content)
        if result['status'] is True:
            return self.write({'status':200,'msg':result['msg']})
        return self.write({'status':400,'msg':result['msg']})

class ModifyBlogHandler(BaseHandler):
    def get(self):
        id = self.get_argument('id', '')
        blog = get_single_blog_lib(self,id)
        self.render('Admin/notices/modify_blog.html',blog=blog)

    def post(self, *args, **kwargs):
        id = self.get_argument('id','')
        title = self.get_argument('title','')
        desc = self.get_argument('desc','')
        content = self.get_argument('content','')
        keywords = self.get_argument('keywords','')
        result = modify_blog_lib(self,id,title,desc,content,keywords)
        if result['status'] is True:
            return self.write({'status':200,'msg':result['msg']})
        return self.write({'status':400,'msg':result['msg']})


class DelBlogHandler(BaseHandler):
    def post(self):
        id = self.get_argument('id','')
        result = del_blog_lib(self,id)
        if result['status'] is True:
            return self.write({'status':200,'msg':result['msg']})
        return self.write({'status':400,'msg':result['msg']})