# 猫
    # 吃
    # 喝
    # 睡
    # 爬树

# 狗
    # 吃
    # 喝
    # 睡
    # 看家

class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def drink(self):
        print(f'{self.name} is drinking')

    def slep(self):
        print(f'{self.name} is sleeping')

    def climb_tree(self):
        print(f'{self.name}开始睡觉')


class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def drink(self):
        print(f'{self.name} is drinking')

    def slep(self):
        print(f'{self.name} is sleeping')

    def house_keep(self):
        print(f'{self.name}开始睡觉')


# xb = Cat('小白')
# xb.eat()
# xb.drink()
# xb.slep()
# xb.climb_tree()
#
# xh = Dog('小白')
# xh.eat()
# xh.drink()
# xh.slep()
# xh.house_keep()


# 继承 -- 需要解决代码的重复问题
# 继承语法

# class A:
#     pass
#
# class B(A):
#     pass

# B 继承 A， A是父类，B是子类
# A 是 父类 基类 超类
# B 是 子类 派生类

# 子类可以使用父类中的方法，静态变量

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f'{self.name} is eating')
#
#     def drink(self):
#         print(f'{self.name} is drinking')
#
#     def slep(self):
#         print(f'{self.name} is sleeping')



# class Cat(Animal):
#     def climb_tree(self):
#         print(f'{self.name}开始睡觉')
#
#
# class Dog(Animal):
#     def house_keep(self):
#         print(f'{self.name}开始睡觉')
#
#
# xb = Cat('小白')
# xb.eat()
# 先开辟空间，空间里又一个类指针  -- > 指向Cat
# 调用 init ，对象下自己的空间中找 init没找到，到Cat 类中找init没找到
# 找父类Animal 中的init


'''
当子类和父类的方法重名的时候，我们只使用子类的方法，而不会调用父类的方法了。 是不是重写呢？
'''
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f'{self.name} is eating')
#
#     def drink(self):
#         print(f'{self.name} is drinking')
#
#     def slep(self):
#         print(f'{self.name} is sleeping')
#
#
# class Cat(Animal):
#
#     def eat(self):
#         print(f'{self.name} 吃猫粮')
#
#     def climb_tree(self):
#         print(f'{self.name}开始睡觉')
#
#
# xb = Cat('小白')
# xb.eat()

'''
子类想要调用父类的方法的同时，还想要执行自己的同名方法
猫和狗在调用eat的时候，既调用自己的也调用父类的,
在子类的方法中调用父类的方法：父类名.方法名(self)
'''
# class Animal:
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food
#         self.blood = 100
#         self.waise = 100
#
#     def eat(self):
#         print(f'{self.name} is eating {self.food}')
#
#     def drink(self):
#         print(f'{self.name} is drinking')
#
#     def slep(self):
#         print(f'{self.name} is sleeping')
#
#
# class Cat(Animal):
#     def eat(self):
#         self.blood += 100
#         Animal.eat(self) # 如果自己有还想用父类的： 直接在子类的方法中调用父类的方法: 父类名.方法名(self)
#     def climb_tree(self):
#         print(f'{self.name}开始睡觉')
#         self.drink()
#
# class Dog(Animal):
#     def eat(self):
#         self.waise += 100
#         Animal.eat(self)
#     def house_keep(self):
#         print(f'{self.name}开始睡觉')
#
#
# xb = Cat('小白', '猫粮')
# xb.eat()
# xh = Dog('小黑', '狗粮')
# xh.eat()
# print(xb.__dict__)
# print(xh.__dict__)
#
# xb.climb_tree()

'''
小白 is eating 猫粮
小黑 is eating 狗粮
{'name': '小白', 'food': '猫粮', 'blood': 200, 'waise': 100}
{'name': '小黑', 'food': '狗粮', 'blood': 100, 'waise': 200}
'''

'''
继承语法： class 子类名(父类名):pass
父类和子类方法的选择：
    # 子类的对象，如果去调用方法
    # 永远优先调用自己的
        # 如果自己有 用自己的
        # 如果自己没有，用父类的
        # 如果自己有还想用父类的： 直接在子类的方法中调用父类的方法: 父类名.方法名(self)
'''


# 练习题：思考下面代码的输出
# class Foo:
#     def __init__(self):
#         self.func()  # 在每一个self调用func的时候，我们不看这句话是在哪里执行的，只看self是谁的
#
#     def func(self):
#         print('in food')
#
# class Son(Foo):
#     def func(self):
#         print('in son')
#
# Son() # in son


''' 思考二：如果想给狗和猫定制个性的属性 '''
class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.blood = 100
        self.waise = 100

    def eat(self):
        print(f'{self.name} is eating {self.food}')

    def drink(self):
        print(f'{self.name} is drinking')

    def slep(self):
        print(f'{self.name} is sleeping')

class Cat(Animal):
    def __init__(self, name, food, eye_color):
        Animal.__init__(self,name,food)  # 调用了父类的初始化，去完成一些通用属性的初始化
        self.eye_colof = eye_color # 派生属性

# 猫： eye_color眼睛的颜色
# 狗： size型号
# xb = Cat('小白', '猫粮', '蓝色')
# print(xb.__dict__)
#
#
# class Dog(Animal):
#     def __init__(self, name, food, size):
#         Animal.__init__(self, name, food)
#         self.size = size
#
# xh = Dog('小黑', '狗粮', '中型犬')
# print(xh.__dict__)
#
# xh.eat()


'''
单继承
'''
# class D:
#     def fun(self):
#         print('in D')
# class C(D):pass
# class A(C):
#     def fun(self):
#         print('in A')
#
# class B(A):pass

# b = B()   --> 先实例化B对象  给了 b
# b.fun()   ---> b在调用 fun()
# 上面两步等价于  B().fun()
# B().fun() # in A

'''
多继承
    # 有一些语言是不支持多继承  java
    # python语言的特点：可以在面向对象中支持多继承
'''
# class A:
#     def func(self): print('in A')
# class B:
#     def func(self): print('in B')
# class C(A, B):pass  # 多继承，C 有两个父类 A， B
#
# C().func() # in B  离谁近，先找谁 class C(A, B)  离A近，所以执行 A类里面的 func

''' 什么时候调子类？ 什么时候调父类的？'''
# 单继承
    # 调子类： 子类自己有的时候
    # 调父类：子类自己没有的时候
    # 调子类和父类的：子类和父类都有，在子类中调用父类的

# 多继承
    # 一个类有多个父类，在调用父类方法的时候，按照继承顺序，先继承的就先寻找

class B:
    def __init__(self):
        self.func()
    def func(self):
        print('in class B')

B()