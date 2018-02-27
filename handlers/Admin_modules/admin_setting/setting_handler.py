#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.setting.setting_libs import get_list_lib, update_setting_lib


class ReadSetHandler(BaseHandler):
    def get(self):
        self.render('Admin/setting/readset.html')

class SettingHandler(BaseHandler):
    def get(self):
        set = get_list_lib(self)
        self.render('Admin/setting/setting.html',set=set)

    def post(self):
        title = self.get_argument('title','')
        se_title = self.get_argument('ftitle','')
        url = self.get_argument('siteurl','')
        keywords = self.get_argument('keywords','')
        desc = self.get_argument('describe','')
        email = self.get_argument('email','')
        icp = self.get_argument('icp','')
        limit_time = self.get_argument('limit-time','')
        result = update_setting_lib(self,
                                    title,
                                    se_title,url,keywords,desc,
                                    email,icp,limit_time)

        if result['status'] is True:
            return self.redirect('/admin/setting')
        return self.write({'status':400,'msg':result['msg']})