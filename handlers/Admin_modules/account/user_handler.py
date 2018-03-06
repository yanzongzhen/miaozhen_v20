#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.account.account_auth_libs import login,register
from libs.account.account_libs import edit_profile, get_user_info, user_see, del_user_lib
import tornado.gen
import json

'''用户管理'''
class ManageUserHandler(BaseHandler):
    def get(self):
        result,counts = get_user_info(self)
        kw = {
            'users':result,
            'counts':counts,
        }
        self.render('Admin/usermanages/manage-user.html',**kw)

class DeleteUserHandler(BaseHandler):
    def post(self):
        id = self.get_argument('id','')
        result = del_user_lib(self,id)
        if result['status'] is True:
            return self.write({'status':200,'msg':result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})

class UserSeeHandler(BaseHandler):
    def post(self):
        uid = self.get_argument('id','')
        kw = user_see(self,uid)
        print kw
        self.write({'status':200,'msg':'OK','data':kw})

class AddUserHandler(BaseHandler):
    @tornado.gen.coroutine
    def post(self):
        name = self.get_argument('username','')
        password = self.get_argument('userpwd','')
        twice_passwd = self.get_argument('new_password','')
        phone = self.get_argument('usertel','')
        result = register(self,name,password,twice_passwd,phone)
        if result['status'] is True:
            print result['msg']
            return self.redirect('/admin/manage_user')
        return self.write({"status":400,"msg":result['msg']})


class UpdateUserHandler(BaseHandler):
    def post(self):
        name = self.get_argument('username','')
        phone = self.get_argument('usertel','')
        old_passwd = self.get_argument('old_password','')
        password = self.get_argument('password','')
        new_passwd = self.get_argument('new_password','')

        result = edit_profile(self,name, password,old_passwd,new_passwd,phone)
        if result['status'] is True:
            print result['msg']
            return self.redirect('/admin/login')
        return self.write({"status": 400, "msg": result['msg']})

class UpdateOtherUserHandler(BaseHandler):
    def post(self):
        name = self.get_argument('username','')
        phone = self.get_argument('usertel','')
        old_passwd = self.get_argument('old_password','')
        password = self.get_argument('password','')
        new_passwd = self.get_argument('new_password','')

        result = edit_profile(self,name, password,old_passwd,new_passwd,phone)
        if result['status'] is True:
            self.write({"status":200, "msg": result['msg']})
            return self.redirect('/admin/manage_user')
        return self.write({"status": 400, "msg": result['msg']})


"""登陆函数"""
class LoginHandler(BaseHandler):
    """02登录函数"""
    def get(self):
        self.render("Admin/usermanages/login.html")

    def post(self):
        name = self.get_argument('username', '')
        password = self.get_argument('userpwd', '')
        result = login(self, name, password)
        if result['status'] is True:
            return self.redirect('/admin')
        return self.write({'status': 400, 'msg': result['msg']})

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user_name")
        self.redirect("/admin/login")


class LoginLogHandler(BaseHandler):
    def get(self):
        self.render('Admin/usermanages/loginlog.html')