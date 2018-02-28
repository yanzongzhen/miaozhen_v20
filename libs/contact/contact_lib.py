#coding:utf-8
from sqlalchemy import func

from libs.db.dbsession import dbSession
from models.contact_model.contact_model import Contact


def add_contact_lib(self,name,email,phone,address,details):
    if name == '' or email == '' or phone == '' or address == '' or details == '':
        return {'status': False, 'msg': '发送失败，请补全信息'}
    contact = Contact()
    contact.name = name
    contact.email = email
    contact.mobile = phone
    contact.address = address
    contact.content = details
    self.db.add(contact)
    self.db.commit()
    return {'status':True,'msg':'发送成功，请耐心等待'}

def get_contact_list(self):
    contact = Contact.all()
    count = dbSession.query(func.count(Contact.id)).scalar()
    return contact,count

def get_one_contact_lib(self,id):
    if id:
        contact = Contact.by_id(id)
        name = contact.name
        content = contact.content
        address = contact.address
        mobile = contact.mobile
        data = {
            'name':name,
            'content':content,
            'address':address,
            'mobile':mobile
        }
        return {'status':True,'data':data}
    return {'status': False, 'msg': 'error'}

def del_contact_lib(self,id):
    if id:
        contact = Contact.by_id(id)
        dbSession.delete(contact)
        dbSession.commit()
        return {'status':True,'msg':'OK'}
    return {'status': False, 'msg': 'error'}