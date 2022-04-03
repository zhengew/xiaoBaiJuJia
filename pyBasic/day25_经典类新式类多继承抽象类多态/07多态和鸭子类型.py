'''
# 多态 一个类型表现出来的多种状态
# 支付 表现出来的 微信支付和苹果支付这两种状态
# 在java情况下：一个参数必须指定类型
# 所以如果想让两个类型的对象都都可以传，那么必须让这两个类继承自一个父类，在制定类型的时候使用父类来指定
'''
# def add(int a,int b):
#     return a+b
#
# print(add(1,'asuhjdhDgl'))

# class Payment:pass
# class WeChat(Payment):
#     def __init__(self,name):
#         self.name = name
#     def pay(self,money):
#         dic = {'username':self.name,'money':money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过微信支付%s钱成功'%(self.name,money))
#
# class Apple(Payment):
#     def __init__(self,name):
#         self.name = name
#     def pay(self,money):
#         dic = {'name': self.name, 'number': money}
#         # 想办法调用苹果支付 url连接 把dic传过去
#         print('%s通过苹果支付%s钱成功' % (self.name, money))

#JAVA
# def pay(Payment a, int b):
#     a.pay(b)
# obj = Apple('alex')
# pay(obj,400)
# obj = WeChat('alex')
# pay(obj,400)

'''
鸭子类型
'''
# 所有实现了 __len__ 方法的类, 在调用len函数的时候，obj都是鸭子类型
# 迭代器协议， __iter__ __next__ 是迭代器

class range: # 此时这个 range 就是个迭代器
    def __iter__(self):
        pass
    def __next__(self):
        pass

# class lentype:pass
# class list(lentype):pass
# class dict(lentype):pass
# class set(lentype):pass
# class tuple(lentype):pass
# class str(lentype):pass
#
# def len(lentype obj):
#     pass

# len(list)
# len(dict)
# len(set)
# len(tuple)
# len(str)

# class list:
#     def __len__(self):pass
# class dict:
#     def __len__(self): pass
# class set:
#     def __len__(self): pass
# class tuple:
#     def __len__(self): pass
# class str:
#     def __len__(self): pass
# def len(鸭子类型看起来有没有实现一个__len__ obj):
#     return obj.__len__()

# super() 是重要的