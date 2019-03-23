# Coding    :   UTF-8
# Team      :   Vincent
# Author    :   Vincent
# Created on:   2019/3/14 22:29
# File Name :   input_test.py
# Tool      :   PyCharm
import datetime

# name = input("Please input your name:")  # input()函数给出提示文本，等待用户键盘输入
# print(name)

# age = input("Please input your age:")  # Python 3.x中输入的即使是数字也当成是字符串，接收数值需要进行类型转换
# print(int(age))

# character = input("Please input a letter:")
# print(character + "的ASCII码为", ord(character))  # 使用ord()函数用户获取单个字符的Unicode指针，可用于获取单个字母的ASCII码

birth_year = input("请输入您的出生年份：")            # 输入出生年份，如1993
now_year = datetime.datetime.now().year             # 获取当前年份
age = now_year - int(birth_year)                    # 计算年龄
print("您的年龄为：" + str(age) + "岁")               # 转换年龄为字符以进行拼接
# 根据联合国标准判断年龄所属的年龄段
if age < 18:
    print("您现在是未成年人")
if 18 <= age < 66:
    print("您现在是青年人")
if 66 <= age < 80:
    print("您现在是中年人")
if age >= 80:
    print("您现在是老年人")

height = float(input("请输入您的身高（cm）："))
weight = float(input("请输入您的体重（kg）："))
