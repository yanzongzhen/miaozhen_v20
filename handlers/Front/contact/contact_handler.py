#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.contact.contact_lib import add_contact_lib
from libs.setting.setting_libs import get_list_lib


class ContactHandler(BaseHandler):
    def get(self):
        sets = get_list_lib(self)
        self.render('Front/contact/contact.html',sets=sets)

    def post(self):
        name = self.get_argument('name','')
        email = self.get_argument('email','')
        phone = self.get_argument('phone','')
        address = self.get_argument('address','')
        details = self.get_argument('details','')

        result = add_contact_lib(self, name, email, phone, address, details)

        if result['status'] == True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})