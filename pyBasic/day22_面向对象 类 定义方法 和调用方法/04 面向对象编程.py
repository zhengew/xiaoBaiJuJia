''' 面向对象编程
# 先来定义模子, 用来秒数一类事物
# 具有相同的属性和动作

'''
# class Person: # 类名
#     def __init__(self, name, sex, job, hp, weapon, ad): # 必须叫这个名字，不能改变的，所有的在一个具体的人物出现后拥有的属性，都可以写在这里
#         self.name = name
#         self.sex = sex
#         self.job = job
#         self.level = 0
#         self.hp = hp
#         self.weapon = weapon
#         self.ad = ad
#
# alex = Person('alex', '不详', '搓澡工', 250, '搓澡巾', 1) # alex 就是对象， alex = Person()的过程是通过类获取一个对象的过程 - 实例化
# wusir = Person('wusir', 'male', '法师', 500, '打狗棍', 1000)
# print(alex,alex.__dict__)
# print(wusir, wusir.__dict__)
# print(alex.name) # print(alex.__dict__['name']) # 属性的查看
# alex.name = 'alexsb' # 属性的修改
# print(alex.name)
#
# alex.money = 10000 # 属性的增加
# print(alex.money)
#
# print(alex.__dict__)
# del alex.money  # 属性的删除
# print(alex.__dict__)
# 类名() 会自动调用类中的 __init__方法

# 类和对象之间的关系？
    # 类 是一个大范围 是一个模子，它约束了事物有哪些属性，但是不能约束具体的值
    # 对象 是一个具体的内容，是模子的产物，它遵循了类的约束，同时给属性赋上具体的值

# Person是一个类: alex 和 wusir 都是 这个类的对象
# 类有一个空间，存储的是定义在 class中的所有名字
# 每一个对象又拥有自己的空间，通过对象名.__dict__就可以查看这个对象的属性和值

# 1.
# 修改列表/字典中的某个值，或者对象的某一个属性，都不会影响这个对象/字典/列表所在的内存空间
import math

''' 实例化所经历的步骤 '''
    # 1. 类名() 之后第一件事：开辟一块内存空间
    # 2. 调用 __init__ 把空间的内存地址作为 形参 self 参数传递给函数内部
    # 3. 所有的这一个对象需要使用的属性都需要和self关联起来。
    # 4. 执行完init中的逻辑后，self变量会自动的被返回到调用处（发生实例化的地方）也就是 ret = re.findall(reg, str)  ret 就是个实例化对象

# dog 类 实现狗的属性  名字 品种 血量 攻击力 都是可以通过实例化被定制的

# class Dog:
#     def __init__(self, name, blood, aggr, kind):
#         self.name = name
#         self.blood = blood
#         self.aggr = aggr
#         self.kind = kind
#
# d1 = Dog('豆包', '金毛', 100, 1)
#
# print(d1.__dict__)

''' 练习题 '''
# 定义一个圆形，半径是这个圆形的属性，实例化一个半径为5的圆形，一个半径为10 的圆形
    # 计算圆形的面积
    # 计算圆的周长


class Circle:
    import math
    def __init__(self, r):
        self.r = r
    def squar(self):
        return round(math.pi * self.r * self.r, 2)

    def perimeter(self):
        return round(math.pi * 2 * self.r, 2)

r1 = Circle(5)
r2 = Circle(10)
print(r1.__dict__, r2.__dict__)

print(r1.squar(), r1.perimeter())

# 定义一个用户类，用户名和密码是这个类的属性，实例化两个用户，分别又不同的用户名和密码
    # 登陆成功后 才创建对象
    # 设计一个方法 修改密码 鉴权

class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password

u1 = Users('zhangsan', 123456)
u2 = Users('tbjx', 123456)
print(type(u2.password))


# 继续完成 人狗大战
    # 你是人
    # 狗是一个npc
    # 你一个回合 狗一个回合
    # 狗掉的血是一个波动值
    # 闪避值

# 继续完成计算器作业