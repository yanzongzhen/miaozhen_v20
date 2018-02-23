#coding:utf-8
from handlers.Admin_modules.admin_category.category_handlers import (
    CategotyHandler,
    UpdateCategoryHandler
)

category_urls = [
    (r'/admin/category',CategotyHandler),
    (r'/admin/update_category',UpdateCategoryHandler)
]