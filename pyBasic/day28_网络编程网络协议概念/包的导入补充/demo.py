import sys
# import glance
# 导入一个包(文件夹)相当于执行了这个包下的__init__文件
# 并不相当于把这个包下的所有文件都导入进来了

# 要想直接导入某个包(文件夹)下的文件
# 方式一 import
# import glance.api.policy as policy
# policy.get()

# 方式二
# from glance.api import policy  # 直接从包中导入文件
# policy.get()

# from glance.api.policy import get #  直接从包中导入函数名或变量名
# get()

# SyntaxError: invalid syntax
# from glance import api.policy # 报错 from ... import 后面不能带点

# 进阶 看博客...
# https://www.cnblogs.com/Eva-J/articles/7292109.html#_label12
# sys.path 第第一个元素，总是你当前执行文件的父目录
#
import glance
# 绝对导入

# 相对导入
    # . 当前目录
    # .. 上级目录

import json
# 当你需要写一个功能
# 这个功能不是直接运行的，而是被别人导入之后使用的，这种情况如果你的这个独立功能形成文件夹
# 文件夹内的所有文件都需要使用相对导入

# 但是如果我们自己开发一个项目，这个项目有一些文件是需要直接运行的，这种情况下不适合用相对导入
# 适合用绝对导入
