# coding:utf-8

import unittest

class test_import(unittest.TestCase):
	def setUp(self):
		print '\n[*] prepare for per test case...\n'

	def try_test_import(self):
		# 所有被引入的子目錄 import 的根據都是跟這這份文件的位置。
		# 所以可以在 m3/m3.py 內用 import m1.m1 或 from m1.m1 import *

		# 很常見的引入
		# from m1.m1 import *
		# from m2.m2 import *

		# 巢狀的引入, 內部可再根據 App 執行檔的根目錄路徑做引入
		# from ... import 的是 class 
		from m3.m3 import *

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
