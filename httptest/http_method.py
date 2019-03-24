#  -*- coding:utf-8 -*-
# Team      :   Vincent
# Author    :   Vincent
# Created on:   2019/3/24 17:10
# File Name :   http_method.py
# Tool      :   PyCharm

#方式2：requests 以JSON的形式提交数据
#Exp:{"username":"jack","password":"123"}
import requests
import json

'''
# GET 请求
response_object = requests.get('http://127.0.0.1:5000/users/rosydawn')
print(response_object.text)
# 带参数的 GET 请求
# 通过字典来发送params参数，如果值为None的键不会被添加到url中
response_object = requests.get(url='http://127.0.0.1:5000/users', params={'order': 'desc'})
print(response_object.json())
'''

# POST 请求
login_data = {
    'username': 'rosydawn',
    'password': '123456'
}
# 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
headers = {'Content-Type': 'application/json'}
# print(json.dumps(login_data))
response_object = requests.post(url='http://127.0.0.1:5000/users/login', data=json.dumps(login_data), headers=headers)
print(response_object.text)
# print(response_object.raw.read())
# print(response_object.text)