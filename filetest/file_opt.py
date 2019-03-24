# -*- coding:utf-8 -*-
# Team      :   Vincent Huang
# Author    :   Vincent Huang
# Created on:   2019/3/22 19:35
# File Name :   file_opt.py
# Tool      :   PyCharm

# 不能读取文件内容（即不能调用read()方法）的模式：w和a
# 若不存在会创建新文件的模式：a，a+，w，w+

# There are three main types of I/O: text I/O, binary I/O and raw I/O

from io import open
import numpy as np

# ==== 读写文本文件测试 开始 ====
'''
# 以只读模式读取文本文件。要求目标文本文件必须存在，否则抛出错误
text_file_path = 'test.txt'    # 目标文本文件代码文件位于同一目录下，可以使用相对路径读取
with open(text_file_path, 'r', encoding='utf-8') as text_file_object:  # 以只读模式打开文本文件
    print(text_file_object)     # 输出显示读到的_io.TextIOWrapper对象
    text_str = text_file_object.read()   # 无参数的read()方法一次性读取文件的全部内容
    print('已读取的文本内容:')
    print(text_str)          # 输出读取到的内容
'''

'''
# 从开头读取一定长度的内容
text_file_path = 'test.txt'
with open(text_file_path, 'r', encoding='utf-8') as text_file_object:
    # read(size=-1)从指针位置开始读取size个字符（即读取部分内容，一个汉字和一个ASCII字符均按一个计算）
    # 指定的字节数超出实际文件的大小也不会出错
    text_str = text_file_object.read(8)
    print('已读取的部分文本内容:')
    print(text_str)          # 输出读取到的部分内容
'''

'''
# 读取指定范围内的内容
text_file_path = 'test.txt'
with open(text_file_path, 'r', encoding='utf-8') as text_file_object:
    # seek(offset[， whence])可以使指针向后移动offset个字节数（按一个汉字两个字节，一个ASCII字符一个字节计算，与read(size)不同）。
    # whence指定移动的起点，0表示从文件开头（默认），1表示从当前位置，2从文件尾部
    # 如果不是以二进制方式读取（即不是rb模式），只允许指定whence的值为0，否则抛
    # 出io.UnsupportedOperation: can't do nonzero cur-relative seeks异常
    text_file_object.seek(2, 0)
    # 如果指针移动的位置正好在半个非ASCII字符的位置，那么读取将会出现指定的编码无法解码的错误
    # 比如：UnicodeDecodeError: 'utf-8' codec can't decode byte 0xaf in position 0: invalid start byte
    text_str = text_file_object.read(3)
    print('已读取的部分文本内容:')
    print(text_str)          # 输出读取到的部分内容
'''

'''
# 一行一行地读取文本文件，以防目标文件太大导致内存被撑爆
text_file_path = 'test.txt'
with open(text_file_path, 'r', encoding='utf-8') as text_file_object:
    line_number = 0
    print('读取的文本内容:')
    while True:
        line_number += 1
        # readline(size=-1)方法一次读取一行中从开头的size个字符，未指定 size 则读取整行
        line = text_file_object.readline()
        if line != '':
            # 从readlines()方法的输出可以看出readline(size=-1)方法会包含每行末尾的换行符'\n'
            # 所以输出的各行内容之间会有一个空行间隔
            # print(str(line_number), ':', line)
            #  使用rstrip()或slice截取来去除每行末尾的换行符后可以正确显示
            # print(str(line_number), ':', line.rstrip())
            print(str(line_number), ':', line[:-1])
        else:
            break
'''

'''
# 如果目标文件的某些行的内容太多，一样会有撑爆内存的风险，保险的做法是反复读取指定size个字符
text_file_path = 'test.txt'
with open(text_file_path, 'r', encoding='utf-8') as text_file_object:
    text_str = ''
    while True:
        block = text_file_object.read(10)
        if block != '':
            text_str += block
        else:
            break
    print('读取的文本内容:')
    print(text_str)
'''

'''
# 一次性读取所有行，得到一个由每行文本构成的列表。可用于方便地读取配置文件
text_file_path = 'test.txt'
with open(text_file_path, 'r', encoding='utf-8') as text_file_object:
    # readlines()方法内部是通过循环调用readline()来实现的
    lines = text_file_object.readlines()
    print('读取的行数：', lines.__len__())
    print('读取的文本内容:')
    print(lines)        # 当文本文件较大时，直接输出所有行会比较慢，可以逐行输出
    print('逐行输出读取的所有行：')
    for line in lines:
        print(line.rstrip())
'''

'''
# 以只写模式（不能读）打开目标文件并写入文本内容，会覆盖原有内容。如果目标文件不存在则创建一个新的文件
text_file_path = 'test.txt'
with open(text_file_path, 'w', encoding='utf-8') as text_file_object:  # 以只写模式打开文本文件（）
    print(text_file_object)     # 输出显示读到的_io.TextIOWrapper对象
    # text_file_object.read()    # 只写模式不能读，调用read()方法会抛出io.UnsupportedOperation: not readable异常
    text_str = '3.141\ntest测试文件'
    print('待写入的文本内容:')
    print(text_str)
    text_file_object.write(text_str)  # 检查test.txt文本文件中已经写入了文本内容
'''

'''
# 以只追加模式（不能读）打开文本文件（重复运行几次下面的代码可以看到更明显的追加效果）
# 如果目标文件已存在，则指针将放在文件末尾，后续可以在文件末尾追加写入新内容。如果目标文件不存在，则创建一个新文件
text_file_path = 'test.txt'
with open(text_file_path, 'a', encoding='utf-8') as text_file_object:      # 以追加模式打开文本（可以指定文件的编码以防止乱码）
    print(text_file_object)     # 输出显示读到的_io.TextIOWrapper对象
    # text_file_object.read()    # 只追加模式不能读，调用read()方法会抛出io.UnsupportedOperation: not readable异常
    append_str = '追加的字符串\n'
    print('待追加的文本内容:')                           # 使用a或a+模式时，指针已经移到文尾，读出来的是一个空字符串
    print(append_str)
    text_file_object.write(append_str)
'''

'''
# 将字符列表写入文本文件
data = ['a', 'b', 'c']
text_file_path = 'test.txt'
with open(text_file_path, 'w', encoding='utf-8') as text_file_object:
    text_file_object.writelines(data)
'''


'''
# 读取某个文本文件中的内容后，写入另一个文件中（即实现复制操作）
text_file_path = 'test.txt'
with open(text_file_path, 'r', encoding='utf-8') as text_file_object:
    text_str = text_file_object.read()
    print('待写入的文本内容:')
    print(text_str)

text_file_path_02 = 'text02.txt'
with open(text_file_path_02, 'w', encoding='utf-8') as text_file_object_02:
    text_file_object_02.write(text_str)
'''

'''
#  一次性写入多行内容
text_file_path = 'test.txt'
with open(text_file_path, 'r', encoding='utf-8') as text_file_object:
    text_str = text_file_object.readlines()
    print('待写入的文本内容:')
    print(text_str)

text_file_path_02 = 'text02.txt'
with open(text_file_path_02, 'w', encoding='utf-8') as text_file_object_02:
    text_file_object_02.writelines(text_str)
'''
# ==== 读写文本文件测试 结束 ====


# ==== 读写二进制文件测试 开始 ====

'''
binary_file_path = 'test.png'
# 以只读模式读取二进制文件，在写入另一个文件中（即实现复制二进制文件）
with open(binary_file_path, 'rb') as binary_file_object:
    print(binary_file_object)     # 输出显示读到的_io.BufferedReader对象
    binary_data = binary_file_object.read()
    print(binary_data)      # 输出的是十六进制表示的二进制字节
with open('test02.png', 'wb') as binary_file_object_02:
    binary_file_object_02.write(binary_data)
'''


'''
binary_file_path = 'test.txt'
# 以读取二进制文件的只读模式读取非 ASCII 文本，然后按指定编码格式解码（任何文件都是二进制存储）
# 与直接按指定编码格式读取文本文件的结果相同
with open(binary_file_path, 'rb') as binary_file_object:
    print(binary_file_object)     # 输出显示读到的_io.BufferedReader对象
    binary_stream = binary_file_object.read()
    text_str = binary_stream.decode('utf-8')
    print(text_str)
'''
# ==== 读写二进制文件测试 结束 ====
