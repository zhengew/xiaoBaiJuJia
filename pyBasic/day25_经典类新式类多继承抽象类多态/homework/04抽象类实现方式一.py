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
# 抽象类
class Payment:
    def pay(self, money):
        raise NotImplementedError(self.__class__, '未实现pay方法')


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
  File "/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day25_经典类新式类多继承抽象类多态/homework/04抽象类实现方式一.py", line 52, in <module>
    main()
  File "/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day25_经典类新式类多继承抽象类多态/homework/04抽象类实现方式一.py", line 49, in main
    pay('tbjx', 100, 'Wechat')
  File "/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day25_经典类新式类多继承抽象类多态/homework/04抽象类实现方式一.py", line 44, in pay
    obj.pay(money)
  File "/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day25_经典类新式类多继承抽象类多态/homework/04抽象类实现方式一.py", line 16, in pay
    raise NotImplementedError(self.__class__, '未实现pay方法')
NotImplementedError: (<class '__main__.Wechat'>, '未实现pay方法')
'''

if __name__ == '__main__':
    main()