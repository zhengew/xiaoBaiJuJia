''' py文件的两个功能 脚本和模块

1. 脚本: 一个文件就是整个程序,比如模拟博客园登陆的文件
2. 模块: 文件中存放着很多函数，用来被导入使用

python 内置全局变量 __name__:
当文件被当作脚本执行时: __name__ 等于 '__main__'
当文件被当作模块导入时: __name__ 等于 模块名
'''
# from test import read1 as read
# if __name__ == '__main__':
#     read()
#     print(read.__name__) # read1
import sys

''' 模块的搜索路径
内存中一斤加载的模块 - > 内置模块 - > sys.path 路径中包含的模块

系统导入模块的路径
1> 内存中: 如果之前成功导入过某个模块,直接使用已经存在的模块
2> 内置路径中: 安装路径 lib 或者 第三方库 set-packages
3> sys.path : 是一个路径列表
'''
# for i in sys.path:
#     print(i)

# 示例: 获取当前模块的路径，并使用相对路径，将带导入模块添加到 sys.path中
# 1. 当前文件的所在路径
import sys
import os

# __file__ 获取当前文件所在路径
print(__file__) # /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day15_模块的导入/py文件功能_脚本和模块.py
# os.path.dirname(__file__) 获取当前文件所在的目录
print(os.path.dirname(__file__) + r"/files/test.txt")

# 导入 regi 报错，未找到 regi模块
# import regi

# 解决方式: 将 regi模块所在路径添加到 sys.path中
sys.path.append(os.path.dirname(__file__) + r"/files/regi.py")
print(sys.path)

import