#coding:utf-8
from handlers.base.base_hanlder import BaseHandler
from libs.flinks.flinks_lib import get_list_flink, add_flinks_lib, show_update_flink_lib, update_flinks_lib, \
    del_flink_lib


class FlinkManageHandler(BaseHandler):
    def get(self):
        flinks,counts = get_list_flink(self)
        kw = {
            'flinks':flinks,
            'counts':counts
        }
        self.render("Admin/flinks/flink.html",**kw)

class AddFlinkHandler(BaseHandler):
    def get(self):
        self.render('Admin/flinks/add-flink.html')

    def post(self):
        name = self.get_argument('name','')
        url = self.get_argument('url','')
        pic_url = self.get_argument('imgurl','')
        desc = self.get_argument('describe','')
        target = self.get_argument('target','')
        rel = self.get_argument('rel','')
        result = add_flinks_lib(self,name,url,pic_url,desc,target,rel)
        if result['status'] is True:
            return self.redirect('/admin/flink')
        return self.write({'status':400,'msg':result['msg']})

class UpdateFlinkHandler(BaseHandler):
    def get(self):
        id = self.get_argument('id','')
        result = show_update_flink_lib(self,id)
        self.render('Admin/flinks/update-flink.html',flink=result)

    def post(self):
        name = self.get_argument('name','')
        url = self.get_argument('url','')
        pic_url = self.get_argument('imgurl','')
        desc = self.get_argument('describe','')
        target = self.get_argument('target','')
        rel = self.get_argument('rel','')
        id = self.get_argument('id', '')
        result = update_flinks_lib(self,id,name,url,pic_url,desc,target,rel)
        if result['status'] is True:
            return self.redirect('/admin/flink')
        return self.write({'status':400,'msg':result['msg']})


class DelFlinkHandler(BaseHandler):
    def post(self):
        id = self.get_argument('id','')
        result = del_flink_lib(self,id)
        if result['status'] is True:
            return self.redirect('/admin/flink')
        return self.write({'status':400,'msg':result['msg']})