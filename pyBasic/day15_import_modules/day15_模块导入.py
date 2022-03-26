''' 模块
1. 定义: 模块就是一些常用功能的集合体.
2. 模块的分类:
1> 内置模块 (标准库)
2> 第三方模块 (第三方库)
3> 自定义模块
'''

''' 导入模块
1. import 关键字

2. 第一次导入模块执行三件事：
1> 创建一个以模块名命名的名称空间
2> 执行这个名称空间(即导入模块)里面的代码
3> 通过 模块名. 的方式引用模块里面的内容(变量,函数名,类名等)
注: 重复导入只是对加载到内存中的模块对象增加了一次引用，不会重复执行模块内的语句 **

3. 被导入模块有独立的名称空间，模块中的函数，把这个名称空间叫做全局名称空间

4. as 关键字支持给模块起别名，方便引用，有利于代码的扩展和优化

5. 支持导入多个模块，建议多行导入
'''
# 示例:
# import test # from the test.py
# import test

''' from 模块 import 函数名 与 import 模块对比
1. from 模块 import 函数名/全局变量：
优点: 使用方便，不要用 模块名.
会直接将 被导入模块的函数名/全局变量 导入到当前模块的命名空间中，
在当前命名空间中直接使用函数名或变量名即可，不需要加 模块名. 来引用
缺点:
当前模块中如果有导入模同名的函数名或变量名，会被覆盖（根据上下文相互覆盖）

2. from 模块 import 函数名 也支持 as 关键字起别名
起别名后，不会与当前命名空间的中的函数冲突

3. from 模块 import * 
1> 导入全部，不建议使用，可以通过在被导入模块中加入__all__ 来限制可以导入的函数或变量
方式一：
__all__ = ["函数名", ... ,"变量名"]
方式二:
__all__ = all["函数名", ... ,"变量名"]

# 注意: __all__ 只对 form module import * 的导入方式生效.
'''
# 示例：
from test import read1 as read
def read1():
    print("在当前模块中导入test.read1,并起别名read,验证是否会与当前模块的read1函数冲突")
# read()
# read1()
# read()

# from test import *
# read1()
# read2()
# change()
# print(name)
'''
NameError: name 'name' is not defined
__all__ = all("read1", "read2", "change")
TypeError: all() takes exactly one argument (3 given)
'''

''' 模块循环导入问题
模块循环/嵌套导入抛出异常的根本原因是由于python只有第一次导入会执行模块内的代码，之后的重复导入仅仅是对内存地址的引用。
实际开发过程中应尽量避免，如果遇到多个模块都要共享的数据，应把数据抽离出来，集中存在到一个文件中去引用
'''

