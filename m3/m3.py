# coding:utf-8
# from m1.m1 import *

import m1.m1

# 這種引入方式似乎該文件內除了 class 外的變數依然可以再 class 內運作
from m2.m2 import m2

class m3:pass

def m3_function():
	pass

print 'loaded m3'
# print type(m1)