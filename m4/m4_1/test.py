# coding:utf-8

# 相對路徑 import ( Py2 不建議使用, Py3 不可用 ), 如果要在 Py2 禁用即需要 from __future__ import absolute_import

from __future__ import absolute_import  # 開啟這行將禁用 import bClass
from . import bClass
