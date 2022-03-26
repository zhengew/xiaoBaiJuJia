'''
柜员模块，验证相对导入
'''
import os
import sys

# sys.path.append(os.path.dirname(__file__))

# 实现相对导入
from ..smteller.teller import *
'''
    from ..smteller.teller import *
ImportError: attempted relative import with no known parent package
'''


def telc():
    print(f"通过相对导入访问smteller/teller.py模块中的成员变量")

# def main():
#     telc()
# if __name__ == '__main__':
#     main()
#
# print(__name__)