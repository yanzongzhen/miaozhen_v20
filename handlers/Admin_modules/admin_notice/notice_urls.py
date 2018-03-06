#coding:utf-8
from handlers.Admin_modules.admin_notice.notice_handler import (
    NoticeManageHandler,
    AddNoticeHandler,
    ModifyBlogHandler,
    DelBlogHandler)

notice_url = [
    (r'/admin/blog',NoticeManageHandler),
    (r'/admin/add_blog',AddNoticeHandler),
    (r'/admin/modify_blog',ModifyBlogHandler),
    (r'/admin/delete_blog',DelBlogHandler)
]