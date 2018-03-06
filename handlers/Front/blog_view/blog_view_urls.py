#coding:utf-8
from handlers.Front.blog_view.blog_view_handler import BlogViewHandler,CommentHandler

f_blog_view_url = [
    (r'/single-post',BlogViewHandler),
    (r'/single-post/comment',CommentHandler)
]