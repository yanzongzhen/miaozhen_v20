#coding:utf-8
import re

content = '<p>test<img src="http://localhost:8000/images/IMG_0672.JPG" style="max-width: 100%;"></p>'

patern = re.compile(r'[a-zA-z]+://[^\s]*',re.S)
print(re.findall(patern,content)[0][:-1])
