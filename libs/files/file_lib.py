#coding:utf-8
import sys

import os

base_pic_url = "http://localhost:8000/images/"

def pic_parse(self,imgs):
    for img in imgs:
        content_type = imgs.get(img)[0]['content_type']
        filename = img
        body = imgs.get(img)[0]['body']
        yield {
            "filename":filename,
            "content_type":content_type,
            "body":body
        }

def save_pic(self,img_list):
    if img_list:
        url = []
        exists_url = []
        for img in img_list:
            filebody = img['body']
            filename = img['filename']
            url.append(base_pic_url+filename)
            save_url = 'files/image/'+filename
            if os.path.exists(save_url):
                old_pic_url = base_pic_url+filename
                exists_url.append(old_pic_url)
                return {'status':True,'msg':'OK but exists','data':exists_url}
            with open(save_url,'wb') as f:
                f.write(filebody)
        return {'status':True,'msg':'OK','data':url}
    else:
        return {'status':False,'msg':'Error'}