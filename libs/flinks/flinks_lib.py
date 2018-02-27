#coding:utf-8
from models.flink_model.flink_model import Flink
from libs.db import dbsession
from sqlalchemy import func

def get_list_flink(self):
    flinks = Flink.all()
    counts = dbsession.dbSession.query(func.count(Flink.id)).scalar()
    return flinks,counts

def add_flinks_lib(self,name,url,pic_url,desc,target,rel):
    if name == '' or url == '' or pic_url == '' or desc == '' or target == '' or rel == '':
        return {'status':False,'msg':'请写全信息'}
    flink = Flink()
    flink.name = name
    flink.url = url
    flink.pic_url = pic_url
    flink.desc = desc
    flink.target = target
    flink.rel=rel
    self.db.add(flink)
    self.db.commit()
    return {'status':True, 'msg': 'OK'}

def show_update_flink_lib(self,id):
    flink = Flink.by_id(id)
    return flink

def update_flinks_lib(self,id,name,url,pic_url,desc,target,rel):
    if name == '' or url == '' or pic_url == '' or desc == '' or target == '' or rel == '':
        return {'status':False,'msg':'请写全信息'}
    flink = Flink.by_id(id)
    flink.name = name
    flink.url = url
    flink.pic_url = pic_url
    flink.desc = desc
    flink.target = target
    flink.rel=rel
    self.db.add(flink)
    self.db.commit()
    return {'status': True, 'msg': 'OK'}

def del_flink_lib(self,id):
    flink = Flink.by_id(id)
    dbsession.dbSession.delete(flink)
    dbsession.dbSession.commit()
    return {'status':True,'msg':'delete ok'}