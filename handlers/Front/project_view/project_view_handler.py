#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.articles.article_lib import show_article_id_detail_lib
from libs.setting.setting_libs import get_list_lib


class ProjectViewHandler(BaseHandler):
    def get(self):
        id = self.get_argument('id','')
        project = show_article_id_detail_lib(self,id)
        sets = get_list_lib(self)
        self.render('Front/project/project.html',sets=sets,project=project)