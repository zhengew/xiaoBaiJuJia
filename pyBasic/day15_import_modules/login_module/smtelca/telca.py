'''
柜员模块，验证相对导入
'''
import os
import sys

# sys.path.append(os.path.dirname(__file__))

# 实现相对导入
# from ..smteller import teller

'''
这个问题是因为我的包闯将的貌似不符合规范，先不管了
    from ..smteller import teller
ImportError: attempted relative import with no known parent package
'''

# teller.users()

def telc():
    print(f"通过相对导入访问smteller/teller.py模块中的成员变量")

def main():
    telc()
if __name__ == '__main__':
    main()

print(__name__)