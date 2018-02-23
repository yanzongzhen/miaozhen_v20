#coding:utf-8
from handlers.Admin_modules.admin_contact.contact_manage_hanlder import ContactManageHandler

contact_m_url = [
    (r'/admin/contact',ContactManageHandler)
]