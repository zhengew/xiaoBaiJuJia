'''
1.项目中的这些py文件，可定会相互引用,src引用 settings...
2.问题2： 此项目在我的电脑路径与别人电脑路径不一致问题
 动态获取 blog的路径,无论在谁的计算机中，都可以找到blog的绝对路径.
 注意:
    # run()
    # sys.path.append() 相对路径
    # print(__file__) # 动态获取本文件的绝对路径
    # print(os.path.dirname(__file__)) # 获取父级目录
    # print(os.path.dirname(os.path.dirname(__file__))) # 获取父级的父级目录

    BASE_PATH = os.path.dirname(os.path.dirname(__file__))
    之前相对引用 sys.path追加路径出现的问题是因为BASE_PATH没有放到 main() 里面去执行，这玩意是动态的，必须执行了内存中才有
'''

import os
import sys
# sys.path.append()
# 动态添加 sys.path
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

def main():
    # sys.path.append() 相对路径
    # print(__file__) # 动态获取本文件的绝对路径
    # print(os.path.dirname(__file__)) # 获取父级目录
    # print(os.path.dirname(os.path.dirname(__file__))) # 获取父级的父级目录
    # 相对引用路径
    sys.path.append(BASE_PATH)
    from core import src
    src.run()

if __name__ == '__main__':
    main()