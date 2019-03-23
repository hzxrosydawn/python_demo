# -*- coding:utf-8 -*-
# Team      :   Vincent Huang
# Author    :   Vincent Huang
# Created on:   2019/3/22 10:14
# File Name :   process_test.py
# Tool      :   PyCharm
from multiprocessing import Process
import time
import os


# 两个子进程方法
def child_1(interval):
    print("子进程开始执行（%s）开始执行，父进程为（%s）" % (os.getpgid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("子进程执行时间为'%")

