# -*- coding:utf-8 -*-
# Team      :   Vincent Huang
# Author    :   Vincent Huang
# Created on:   2019/3/22 18:50
# File Name :   encode_test.py
# Tool      :   PyCharm
import base64

# 编解码文本
# base64.b64encode(s, altchars=None)接收的s是bytes类型，返回一个经Base64编码后的bytes类型对象
# 标准Base64字符串中包含‘+’、‘/’、‘=’、‘~’和‘.’等字符，其中，‘+’、‘/’和‘=’字符在URL中都有特殊意义
# “~”与文件系统冲突，不能使用，而“.”在某些文件系统中出现两次就为错误
# altchars 用于指定至少长度为2（多余的长度会被忽略）的字节型对象用于替换‘+’和‘/’字符，可用于创建URL安全和文件系统安全的Base64字符串
# altchars 默认为 None，表示使用标准的Base64字符进行编码

# base64.b64decode(s, altchars=None, validate=False)收的s也是bytes类型，返回一个经Base64解码后的bytes类型对象
# altchars 必须为字节型对象或至少长度为2的ASCII字符串，用于替换‘+’和‘/’字符，可用于创建URL安全和文件系统安全的Base64字符串
# # altchars 默认为 None，表示使用标准的Base64字符进行解码
test_str = "我在学习Java加密与解密相关的技术。我在学习Java加密与解密相关的技术。"
print('编码前：', test_str)
encoded_bytes = base64.b64encode(test_str.encode('utf-8'))
print('标准编码后：')
print(str(encoded_bytes, 'utf-8'))  # 测试字符串经Base64编码之后含有‘+’、‘/’、‘=’字符
decoded_bytes = base64.b64decode(encoded_bytes)
print('标准解码后：', str(decoded_bytes, 'utf-8'))   # 输出表名字符串已经还原

# 使用‘+’替换为‘-’、‘/’替换为‘_’以进行安全编码（参考RFC 3548）。目前无法替换‘=’字符，所以，仍不是URL严格安全的
encoded_bytes = base64.b64encode(test_str.encode('utf-8'), '-_'.encode('utf-8'))
print('安全编码后：')
print(str(encoded_bytes, 'utf-8'))  # 测试字符串经Base64编码之后含有‘+’替换为‘-’，‘/’替换为‘_’，但‘=’没有替换
decoded_bytes = base64.b64decode(encoded_bytes, '-_')
print('安全解码后：', str(decoded_bytes, 'utf-8'))   # 输出表名字符串已经还原