#coding:utf-8

from libs.db.dbsession import dbSession
from models.setting_model.setting_model import Setting
from  models.flink_model.flink_model import Flink

def get_list_lib(self):
    all_set = dbSession.query(Setting).order_by(Setting.createtime.desc()).first()
    return all_set


def update_setting_lib(self,title,se_title,url,keywords,desc,email,icp,limit_time):
    if title == '' or se_title == '' or url == '' or keywords == '' or desc == '' or email == '' or icp == ''or limit_time == '':
        return {'status':False,'msg':'please complete your input'}
    sets = Setting()
    sets.title = title
    sets.se_title = se_title
    sets.url = url
    sets.keywords = keywords
    sets.desc = desc
    sets.Email = email
    sets.ICP = icp
    sets.limit_time = limit_time
    self.db.add(sets)
    self.db.commit()
    return {'status':True,'msg':'OK'}

def get_list_flink_lib(self):
    return Flink.all()

