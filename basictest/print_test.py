# Coding    :   UTF-8
# Team      :   Vincent
# Author    :   Vincent
# Created on:   2019/3/8 23:49
# File Name :   print_test.py
# Tool      :   PyCharm
import datetime
a = 100
b = 50
c = 'hello world'
print(9)                    # 直接输出数值
print(a)                    # 输出数值变量
print(a * b)                # 输出表达式的计算结果
print('go big or go home')  # 直接输出字符串
print(c)                    # 输出字符串变量的值
print(a, b, c)              # 使用逗号分隔在不换行的情况下输出多个值
print(chr(65))              # 借助chr()函数输出ASCII码的字符A
print(chr(97))              # 借助chr()函数输出ASCII码的字符a
print('\u4e2d\u56fd')       # 输出Unicode字符“中国”

fp = open(r'/test.txt', 'a+')
print('要么出众，要么出局', file=fp)     # 输出字符串到在当前磁盘根目录下的指定文件中
fp.close()
print('当前年份：' + str(datetime.datetime.now().year))                          # 借助datetime模块打印当前时间
print('当前日期时间：' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 借助datetime模块打印指定格式的时间