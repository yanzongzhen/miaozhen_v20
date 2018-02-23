#coding=utf-8

from qiniu import Auth, put_file, etag, urlsafe_base64_encode,put_data
import qiniu.config
#需要填写你的 Access Key 和 Secret Key
access_key = 'msE-IFOSpp3PSBfKj9ac05DKheXF95e7mjZZ-uex'
secret_key = 'CQ7qotyLFwLpV0RgNU2kN6sFQIYqEIS75ihBZPuI'
#构建鉴权对象

q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'tornado'
#上传到七牛后保存的文件名

def upload_qiniu_file_content(content):
    """上传到七牛"""
    token = q.upload_token(bucket_name)
    ret, info = put_data(token, None, content)
    return ret['key'], info  #文件名，状态信息


def down_qiniu_file(file_url):
    """从七牛下载"""
    # 或者直接输入url的方式下载
    base_url = file_url
    # 可以设置token过期时间
    private_url = q.private_download_url(base_url, expires=10)
    return private_url


