''' 相对导入
定义: 针对某个项目中的不同模块之间进行导入，成为相对导入。
语法: form 相对路径 import xxx

相对路径:
. : 表示当前路径
.. : 表示当前路径的父级路径
... : 表示当前路径的父路径的父路径
'''
# 相对导入同项目下的模块

import os, sys

sys.path.append(os.path.dirname(__file__) + r"/login_moudles")
# print(sys.path)

from login_module.smtelca import telca

telca.telc()
# telca.users()
