''' 形参 动态参数 *args *kwargs '''
# 1. *args 接收任意数量的位置实参,并用 元组 的形式返回给形参 args
def add(*args):
    sum = 0.0
    for i in args:
        sum += i
    return sum

# print(add(1, 2, 3, 4))

# 2. **kwargs 接收任意数量的关键字参数,并用 字典 的形式返回给形参 kwargs
def infos(**kwargs):
    return kwargs

# print(infos(name="zew", age="31"))

# 3. 动态参数的混合使用, 注意 接收位置参数的 动态参数在前，接收关键字参数的 动态参数在后
def infos(*args, **kwargs):
    print(args)
    print(kwargs)

# infos("zew", 31, Sex="man")

''' * 的魔法作用 '''
# 注：动态参数在实际中对于函数调用方不友好，很难判断需要传递哪些参数类型，不建议使用。在函数外对可迭代对象的打散和集合有点用处
# 1.在函数中分为打散和聚合
# 聚合: 将任意数量的位置实参或关键字实参传递给形参（元组或字典），就是 聚合
# 打散: 将可迭代的位置实参(字符串,元组，列表，字典等)传递给形参，就是 打散

# 打散实例：
def func1(*args):
    print(args)

# func1(*"abc", *(1, 2, 3), *[3, 4, 5]) # ('a', 'b', 'c', 1, 2, 3, 3, 4, 5)

def func2(**kwargs):
    print(kwargs)

# func2(**{"name":"zew", "age":31}, **{"Sex":"Man",}) # {'name': 'zew', 'age': 31, 'Sex': 'Man'}

# 2. 在函数外的打散和聚合, 聚合时返回的是列表
# 例如元组的拆包:
a, *b = (1, 2, 3, 4) # 1 [2, 3, 4]
# print(a, b, type(a), type(b))

lis = [1, 2, 3, *[4, 5, 6]] # [1, 2, 3, 4, 5, 6]
# print(lis)

''' 形参的顺序 '''
# def func(位置参数, *args动态位置参数, 关键字默认值参数, 仅限关键字参数, **kwargs动态关键字参数):
# 注意:如果形参中有仅限关键字参数，当没有给它传参时，会抛出异常
# 感觉这个 仅限关键字参数没什么用处

# def func(name, *args, Sex="Man", c, **kwargs):
#     print(name,args,Sex,c,kwargs)

# func("zew", 31, grade="大专") # TypeError: func() missing 1 required keyword-only argument: 'c'
# func("zew", 31, c = "QA", grade="大专")

''' 命名空间
1.命名空间分为: 
 内置命名空间: 基本数据类型/内置函数等等 int str tuple list  print input...
 全局命名空间: 在函数外声明的变量/函数名
 局部命名空间: 在函数内声明的变量/函数等

2.命名空间的加载顺序: 内置命名空间 - > 全局命名空间(上下文从上到下依次加载) -> 局部命名空间(根据函数调用顺序)

3.命名空间的取值顺序: 局部命名空间 - > 全局命名空间 - > 内置命名空间
'''

''' 作用域
1. 全局作用域: 全局命名空间和内置命名空间
2. 局部作用域: 局部命名空间
3. 注: 局部作用域只能对全局作用域的变量进行引用，而不能改变全局作用域的变量值
内置函数:
globals(): 以字典形式返回全局作用域所有变量的对应关系
locals(): 以字典形式返回当前作用域的变量的对应关系
'''
# 示例：
a = 1
b = 2
def func():
    c = 3
    print(globals())
    print(locals()) # {'c': 3}

# func()


''' 关键字 global nonlocal '''
# 1. global 作用：1> 声明一个全局变量, 2> 当想在局部作用域的对全局作用域的变量进行修改时（仅限于str,int）,可在变量前加 global关键字
# 2. nonlocal 作用: 在局部作用域中对父级作用域的变量进行引用和修改
