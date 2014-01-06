=======================
解說 Python Import 機制
=======================

** Application目錄結構 **

    ::

        /main.py
        ...
        /m1/__init__.py
        /m1/m1.py
        ...
        /m1/m1/__init__.py
        /m1/m1/m1.py
        ...
        /m2/__init__.py
        /m2/m2.py
        ...
        /m3/__init__.py
        /m3/m3.py


** main.py **

    ::

        from m1.m1 import *
        from m2.m2 import *
        from m1.m1.m1 import *


** /m2/m2.py **

    ::

        from m1.m1
            # 也可以這樣做因為執行的 Py File 是 main.py
            # 他會先找 /m2/m1/m1.py 再不再，在尋找/m1/m1.py。


** /m1/m1.py **

    ::

        from m2.m2 import *
        from m1.m1 import *
            # 根據上述規則他會找到 /m1/m1/m1.py 這個檔案而不是 /m1/m1.py
            # 先找到的那個先使用。
            # 不建議使用 import * 盡量要明確指定！否則 unittest 會警告。


** 測試 **

    ::

        python main.py


** Module & Class 在 import 的差異**
    
    ::

        # myModule.py
            class my_module:pass

            import myModule
                # 引入 myModule.py

        # python 引入模組方法, 引入的 module 會先搜尋該文
        # 檔相對路徑在搜尋該 app 的根目錄的相對路徑。
            from {module_path} import {class}
                or
            import {module_path}

        # 錯誤
            import {module_path.class}

        # 錯誤
            import {module_path.function}

        # 正確
            from {module_path} import {class}
                or
            from {module_path} import {function}
