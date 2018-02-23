#coding:utf-8
from handlers.Admin_modules.admin_notice.notice_handler import (
    NoticeManageHandler,
    AddNoticeHandler
)

notice_url = [
    (r'/admin/notice',NoticeManageHandler),
    (r'/admin/add_notice',AddNoticeHandler)
]