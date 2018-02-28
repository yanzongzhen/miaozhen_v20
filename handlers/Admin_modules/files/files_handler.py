#coding:utf-8
import json

from handlers.base.base_hanlder import BaseHandler

from libs.files.file_lib import pic_parse, save_pic


class UploadPicHandler(BaseHandler):
    def post(self):
        img_list = []
        imgs = self.request.files #获取照片列表
        for img in pic_parse(self,imgs):
            img_list.append(img)

        result = save_pic(self,img_list)
        if result['status'] is True:
            return self.write({'data':result['data'],'errno':0})
        return self.write({'msg': result['msg'],'errno': 1})