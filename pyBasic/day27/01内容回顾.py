'''
# super
    # super遵循的mro算法
    # 只在新式类中能使用
    # py2新式类中需要自己添加参数(子类名, 子类对象)

# 封装
    # 广义上的封装
    # 狭义上的封装 __名字
        # 私有化
            # 方法名私有化
            # 实例变量的私有化
            # 静态变量的私有化
        # 私有化的特点
            # 只能在类的内部使用，不能在外部使用
        # 私有的各种静态变量和方法能不能继承
            # 不能被子类继承

# 内置函数
    # 判断一个变量是不是可调用的,判断这个变量后面能不能加()
        # callable(名字)
    # 装饰器
        # @property  把一个方法伪装成属性，使它调用的时候不用加括号
        # 给伪装成属性的方法赋值  @函数名.setter装饰器， 此处的函数名必须为@property装饰的函数
        # 删除属性  @函数名.deleter装饰器， 此处的函数名必须为@property装饰的函数

    # 反射相关
        # hasattr
        # getattr
        # 字符串数据类型的变量名，采用getattr(对象, '变量名')，获取变量的值

# 各种反射练习题：答案
# 选课系统的作业

'''