# coding:utf-8

import unittest

class test_import(unittest.TestCase):
	def setUp(self):
		print '\n[*] prepare for per test case...\n'

	def test_try_import(self):
		# 所有被引入的子目錄 import 的根據都是跟這這份文件的位置。
		# 所以可以在 m3/m3.py 內用 import m1.m1 或 from m1.m1 import *

		# 很常見的引入
		# from m1.m1 import *
		# from m2.m2 import *

		# 巢狀的引入, 內部可再根據 App 執行檔的根目錄路徑做引入
		# from ... import 的是 class 
		#
		# 盡量不要用 from ... import * 會出現警告。
		# 使用 from ... import {what_name} 會可以正常使用(不用擔心程式文稿內的其他變數)
		# from m3.m3 import *
		#
		from m3.m3 import m3
		#
		# 因為 m3/m3.py 內有 from m2.m2 import m2 , 所以可以這樣下。
		from m3.m3 import m2

		a=m2()

		print a

		# import module
		# from {module_path} import {class} # 而且可以正常運作(包含那個文件內的所有靜態資料或方法)
		import m3.m3

		print dir(m3.m3)
		print m3.m3.m3_function
		print m3.m3.m3

		from m3.m3 import m3_function

		print m3_function

if __name__ == '__main__':
    unittest.main()
