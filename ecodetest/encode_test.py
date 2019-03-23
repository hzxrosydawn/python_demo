# -*- coding:utf-8 -*-
# Team      :   Vincent Huang
# Author    :   Vincent Huang
# Created on:   2019/3/22 18:50
# File Name :   encode_test.py
# Tool      :   PyCharm
import base64

test_str = "binary string"
print(test_str)
encoded_str = base64.b64encode(test_str.encode('utf-8'))
print(str(encoded_str, 'utf-8'))
decoded_str = base64.b64decode(encoded_str)
print(str(decoded_str, 'utf-8'))