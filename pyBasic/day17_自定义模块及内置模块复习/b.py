'''
被导入模块
'''

name = 'b.py'

def func1():
    print("name = b.py")

def func2():
    global name
    name = "bb.py"