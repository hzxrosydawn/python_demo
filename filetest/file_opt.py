# -*- coding:utf-8 -*-
# Team      :   Vincent Huang
# Author    :   Vincent Huang
# Created on:   2019/3/22 19:35
# File Name :   file_opt.py
# Tool      :   PyCharm

# 不能读取文件内容（即不能调用read()方法）的模式：w和a
# 若不存在会创建新文件的模式：a，a+，w，w+

from io import open

text_file_path = 'test.txt'     # 目标文件代码文件位于同一目录下，可以使用相对路径读取
with open(text_file_path, 'r', encoding='utf-8') as text_file_object:      # 以只读模式打开文本（可以指定文件的编码以防止乱码）
    print(text_file_object)     # 输出显示读到的_io.TextIOWrapper对象
    text_str = text_file_object.read()
    print("读取的文本内容:")
    print(text_str)

# with open(text_file_path, 'a', encoding='utf-8') as text_file_object:      # 以追加模式打开文本（可以指定文件的编码以防止乱码）
#     print(text_file_object)     # 输出显示读到的_io.TextIOWrapper对象
#     text_str = text_file_object.read()
#     print("读取的文本内容:")                           # 为a或a+模式时，因为为追加模式，指针已经移到文尾，读出来的是一个空字符串
#     print(text_str)
#     append_str = "追加的字符串"



# binary_file_path = 'C:\\Users\\Vincent Huang\\Desktop\\voicetest\\test.png'   # 目标文件代码文件位于其他目录下，可以使用相对路径读取
# with open(binary_file_path, 'rb') as binary_file:
#     binary_file.read()
# print(binary_file)     # 输出显示读到的_io.BufferedReader对象
