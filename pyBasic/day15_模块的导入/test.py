# 限制 from test import * 导入的函数或变量
__all__ = ["read1", "read2", "change"]

print("from the test.py")
name = "太白金星"

def read1():
    print("test模块:", name)

def read2():
    print("test模块:")
    read1()

def change():
    global name
    name = "alex"
