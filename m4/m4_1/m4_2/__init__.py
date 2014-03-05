# coding:utf-8

# 使用相對路徑 import (當 import 這個 module 的時候一併帶入)
from .aClass import *

# 使用相對路徑 import 上一層的物件
from ..bClass import *

# 代表當 from m4.m4_1.m4_2 import * 的時候, 就執行這個 Script
#
# >>> from m4.m4_1.m4_2 import *
# >>> aClass
# 	<module 'm4.m4_1.m4_2.aClass' from 'm4\m4_1\m4_2\aClass.pyc'>
# >>> aClass.myClass		<-- 正常的指定方法 from m4.m4_1.m4_2 import aClass
# 	<class m4.m4_1.m4_2.aClass.myClass at 0x00397A40>
# >>>
#