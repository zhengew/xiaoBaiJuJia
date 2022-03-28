'''
演示import
1.import 使用全局命名空间
2.在内存中开辟一个以被导入模块命名的命名空间
3.通过模块名. 调用此模块中的变量/函数名/类名等.

被导入模块有独立的名称空间
'''

import b

name = 'test1'

b.func1() # name = b.py
print(name) # test1
b.func2()
print(b.name) # bb.py
print(name) # test1
