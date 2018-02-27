#coding=utf-8
from random import randint
from datetime import datetime
from models.accounts.account_user_model import User

def login(self, name, password):
    """02登录函数"""
    print name, password
    if name == '' and password == '':
        return {'status': False, 'msg': '请输入用户名或密码'}
    user= User.by_name(name)#注意
    if user and user.auth_password(password):#注意
        user.last_login = datetime.now()
        user.loginnum += 1
        self.db.add(user)
        self.db.commit()
        self.session.set('user_name', user.name)
        return {'status': True, 'msg': '登录成功'}
    return {'status': False, 'msg': '用户名输入错误或者密码不正确'}


def register(self,name,password,twice_passwd,phone):
    print name,password,twice_passwd
    if name == '' and password == '':
        return {'status': False, 'msg': '请输入用户名或密码'}
    if password == twice_passwd:
        return {'status': False, 'msg': '请输入相同的密码'}
    user = User()
    user.name = name
    user.mobile = phone
    user.password = password
    self.db.add(user)
    self.db.commit()
    return {'status': True, 'msg':'注册成功'}


