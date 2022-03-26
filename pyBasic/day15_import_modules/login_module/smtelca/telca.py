'''
柜员模块，验证相对导入
'''
import os

# 实现相对导入
from ..smteller import users

def telca():
    print(f"通过相对导入访问smteller/teller.py模块中的成员变量")



def main():
    telca()

if __name__ == '__main__':
    main()