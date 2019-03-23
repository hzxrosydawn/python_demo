# Coding    :   UTF-8
# Team      :   Vincent Huang
# Author    :   Vincent Huang
# Created on:   2019/3/22 9:59
# File Name :   main_sub_test.py
# Tool      :   PyCharm
from multiprocessing import Process  # 导入进程类


# 定义子进程
def sub_process(interval):
    print("我是子进程")
    print("1")


# 定义主进程
def main():
    print("主进程开始")
    p = Process(target=sub_process, args=(1,))
    p.start()
    print("主进程结束")


if __name__ == '__main__':
    main()




