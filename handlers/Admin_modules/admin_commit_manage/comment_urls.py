#coding:utf-8
from handlers.Admin_modules.admin_commit_manage.comment_handler import CommentManageHandler

comment_manage_urls = [
    (r'/admin/comment',CommentManageHandler)
]