''' 抽象类
# 抽象类
    # 是一个开发的规范，约束它的所有子类必须实现一些和它同名的方法

# 支付程序
    # 微信支付 url连接，告诉你参数是什么格式
        # {'username:'用户名', 'money':200}
    # 支付宝支付 url连接，告诉你参数是什么格式
        # {'uname:'用户名', 'price':200}
    # 苹果支付

'''
# 抽象类 实现方式二
from abc import ABCMeta, abstractmethod
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):pass


class Wechat(Payment):
    def __init__(self, name):
        self.name = name
    def pay1(self, money): # Wechat 类为实现抽象类执行的方法名 pay
        print(f"{self.name}通过微信成功支付了{money}元")

class Alipay(Payment):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        print(f"{self.name}通过支付宝成功支付了{money}元")


# a = Wechat('alex')
# a.pay(1)

'''
a = Wechat('alex')
TypeError: Can't instantiate abstract class Wechat with abstract method pay
'''

# 归一化设计
# 统一外部访问 支付接口的调用方式
def pay(name, money, kind):
    if kind.lower() == 'wechat':
        obj = Wechat(name)
    elif kind.lower() == 'alipay':
        obj = Alipay(name)

    obj.pay(money)


def main():
    pay('tbjx', 200.0, 'alipay')
    # pay('tbjx', 100, 'Wechat')

'''
Traceback (most recent call last):
  File "/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day25_经典类新式类多继承抽象类多态/homework/05抽象类实现方式二.py", line 58, in <module>
    main()
  File "/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day25_经典类新式类多继承抽象类多态/homework/05抽象类实现方式二.py", line 55, in main
    pay('tbjx', 100, 'Wechat')
  File "/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day25_经典类新式类多继承抽象类多态/homework/05抽象类实现方式二.py", line 46, in pay
    obj = Wechat(name)
TypeError: Can't instantiate abstract class Wechat with abstract method pay
'''

if __name__ == '__main__':
    main()