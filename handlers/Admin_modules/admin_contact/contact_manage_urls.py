#coding:utf-8
from handlers.Admin_modules.admin_contact.contact_manage_hanlder import ContactManageHandler, SeeContactHandler, \
    DelContactHandler

contact_m_url = [
    (r'/admin/contact',ContactManageHandler),
    (r'/admin/see_contact',SeeContactHandler),
    (r'/admin/delete_contact',DelContactHandler)
]