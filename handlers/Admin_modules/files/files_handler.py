#coding:utf-8
import json
import tornado.gen
import tornado.web
from handlers.base.base_hanlder import BaseHandler

from libs.files.file_lib import pic_parse, save_pic


class UploadPicHandler(BaseHandler):
    @tornado.gen.coroutine
    def post(self):
        imgs = self.request.files.get('file', None) #获取照片列表

        result = save_pic(self,imgs)
        if result['status'] is True:
            return self.write({'data':result['data'],'status':200})
        return self.write({'data': result['msg'],'status': 400})