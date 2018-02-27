#coding=utf-8
from datetime import datetime
from models.accounts.account_user_model import User
from sqlalchemy import func
from libs.db.dbsession import dbSession
def edit_profile(self,name, password,old_passwd,new_passwd,phone):
    """编辑个人信息"""
    if password == "":
        return {'status': False, 'msg': "密码不能为空"}
    if old_passwd == "":
        return {'status': False, 'msg': "密码不能为空"}
    if name == "":
        return {'status': False, 'msg': "姓名不能为空"}
    user = self.current_user
    user.name = name
    user.password = new_passwd
    user.mobile = phone
    user.update_time = datetime.now()
    self.db.add(user)
    self.db.commit()
    return {'status': True, 'msg': "修改成功"}


def get_user_info(self):
    """获取用户信息"""
    user =  User.all()
    counts = dbSession.query(func.count(User.id)).scalar()
    return user,counts

def get_some_info_lib(self,name):
    user = User.by_name(name)
    return user

def user_see(self,uid):
    user = User.by_id(uid)
    kw = {
        'username': user.name,
        'userid': user.id,
        'usertel': user.mobile
    }
    return kw

def del_user_lib(self,id):
    if User.by_id(id) is None:
        return {'status':False,'msg':'error'}
    user = User.by_id(id)
    dbSession.delete(user)
    dbSession.commit()
    return {'status':True, 'msg': '删除成功'}