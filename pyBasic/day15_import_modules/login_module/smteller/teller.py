'''
柜员模块，验证相对导入
'''
import os


def users():
    print(f"teller.py的父级目录:{os.path.dirname(__file__)}")

def main():
    users()

if __name__ == '__main__':
    main()