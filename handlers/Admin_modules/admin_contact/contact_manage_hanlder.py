#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.contact.contact_lib import get_contact_list, get_one_contact_lib, del_contact_lib


class ContactManageHandler(BaseHandler):
    def get(self):
        contact,count = get_contact_list(self)
        kw = {
            'contacts':contact,
            'count':count
        }
        self.render('Admin/contact/contact.html',**kw)

class SeeContactHandler(BaseHandler):
    def post(self):
        id = self.get_argument('id','')
        result = get_one_contact_lib(self,id)

        if result['status'] is True:
            return self.write({'status':200,'data':result['data']})
        return self.write({'status':400,'msg':result['msg']})

class DelContactHandler(BaseHandler):
    def post(self):
        id  = self.get_argument('id','')
        result = del_contact_lib(self,id)
        if result['status'] is True:
            self.redirect('/admin/contact')
        return self.write({'status':400,'msg':result['msg']})