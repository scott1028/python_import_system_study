# coding:utf-8
# 似乎在 外部使用 from m2.m2 import m2 依然可以存取 test 變數

test=1

class m2:
	print test
	def __init__(self):
		print test
	pass

print 'loaded m2'