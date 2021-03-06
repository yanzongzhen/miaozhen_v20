#coding:utf-8
from handlers.Admin_modules.admin_articles.article_handler import (
    ArticleManageHandler,
    AddArticleHandler,
    UpdateArticleHandler,
DelArticleHandler
)

article_urls = [
    (r'/admin/article',ArticleManageHandler),
    (r'/admin/article_delete',DelArticleHandler),
    (r'/admin/add_article',AddArticleHandler),
    (r'/admin/update_article',UpdateArticleHandler)
]