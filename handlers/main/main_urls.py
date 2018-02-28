#coding:utf-8
from handlers.main.main_hanlder import MainHandler
from handlers.Admin_modules.admin.admin_urls import admin_urls
from handlers.Admin_modules.admin_articles.article_urls import article_urls
from handlers.Admin_modules.admin_category.category_urls import category_urls
from handlers.Admin_modules.admin_commit_manage.comment_urls import comment_manage_urls
from handlers.Admin_modules.admin_flinks.flink_urls import flink_urls
from handlers.Admin_modules.admin_notice.notice_urls import notice_url
from handlers.Admin_modules.admin_setting.setting_urls import set_urls
from handlers.Admin_modules.account.user_urls import user_urls
from handlers.Admin_modules.admin_contact.contact_manage_urls import contact_m_url

from handlers.Front.about.ablout_urls import f_about_url
from handlers.Front.blog.blog_urls import f_blog_url
from handlers.Front.contact.contact_urls import f_contact_urls
from handlers.Front.blog_view.blog_view_urls import f_blog_view_url
from handlers.Front.project_view.peoject_view_urls import f_project_view_url
from tornado.web import StaticFileHandler
from handlers.Admin_modules.files.files_url import file_url
handlers = [
    (r'/',MainHandler),
    (r'/images/(.*\.(jpg|mp3|mp4|ogg|png|JPG))', StaticFileHandler, {'path': 'files/image/'}),
]

'''后端'''
handlers += admin_urls
handlers += article_urls
handlers += category_urls
handlers += comment_manage_urls
handlers += flink_urls
handlers += notice_url
handlers += set_urls
handlers += user_urls
handlers += contact_m_url
handlers += file_url

'''前端'''
handlers += f_about_url
handlers += f_blog_url
handlers += f_blog_view_url
handlers += f_project_view_url
handlers += f_contact_urls