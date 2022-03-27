# import src
# 直接引用不到,他不在内存,内置,sys.path
'''
# 这么做虽然实现,但是有问题:
# 1, 项目中的这些py文件,肯定会互相引用,src 引用 settings, src 引用 commom.py.....
import sys
sys.path.append(r'D:\python_22\day18\blog\core')
sys.path.append(r'D:\python_22\day18\blog\conf')
sys.path.append(r'D:\python_22\day18\blog\lib')
.......
print(sys.path)
import src
src.run()
# 上面肯定是不行,low,我不能一个一个添加.

'''

# import sys
# # 我直接添加blog的目录
# sys.path.append(r'D:\python_22\day18\blog')
# from core import src
# # print(sys.path)
# src.run()

'''
# 问题2: 此项目 在我的计算机中 他的路径D:\python_22\day18\blog 写死了.
# 动态的获取blog的路径 无论在谁的计算机中,都可以找到blog的绝对路径.
import sys
# 我直接添加blog的目录
sys.path.append(r'D:\python_22\day18\blog')
from core import src
# print(sys.path)
src.run()
'''
# import sys
# import os
# print(__file__) #动态获取本文件的绝对路径
# print(os.path.dirname(__file__))  # 获取父级的目录
# print(os.path.dirname(os.path.dirname(__file__)))  # 获取爷级的目录 D:/python_22/day18/blog

####################  以上是思路

import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
from core import src

if __name__ == '__main__':
    src.run()




