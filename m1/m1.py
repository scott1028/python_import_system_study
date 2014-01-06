# coding:utf-8

import m1_2

class m1:pass

print 'loaded m1'

# import m1_sub.m1_sub
# 似乎會找整個 app 的執行根目錄或是這份文檔的相對位置
# 
from m1_sub import m1_sub

# 如果執行 python /main.py, 會先找 /m2/m2/m2.py, 再找 m2/m2.py
from m2.m2 import *
# 
from m3.m3 import *
