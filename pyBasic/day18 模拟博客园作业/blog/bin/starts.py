'''
1.项目中的这些py文件，可定会相互引用,src引用 settings...

'''

import os
import sys
sys.path.append(r"/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day18 模拟博客园作业/blog")

def main():
    # run()
    print(sys.path)
if __name__ == '__main__':
    main()