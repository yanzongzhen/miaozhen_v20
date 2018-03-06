#coding:utf-8

from handlers.base.base_hanlder import BaseHandler
from tornado.web import authenticated
from libs.account.account_libs import get_some_info_lib

class AdminPageHandler(BaseHandler):
    @authenticated
    def get(self):
        user_name = self.get_secure_cookie('user_name')
        if user_name:
            remote_ip = self.request.remote_ip
            name = self.current_user.name
            user, blog_count, comment_count,flink_count, project_count, admin_count = get_some_info_lib(self, name)
            kw = {
                'remote_ip': remote_ip,
                'users': user,
                'blog_count': blog_count,
                'comment_count': comment_count,
                'flink_count': flink_count,
                'project_count': project_count,
                'admin_count': admin_count
            }
            self.render('Admin/index.html', **kw)
        else:
            self.redirect('/admin/login')


