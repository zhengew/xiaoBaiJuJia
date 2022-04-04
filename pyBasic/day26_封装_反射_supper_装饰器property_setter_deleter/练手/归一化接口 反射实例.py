# 通过反射 实现支付类的 归一化设计

class Payment:
    def pay(self, money):
        ''' 支付接口统一实现pay方法'''
        raise NotImplementedError(self.__class__,'未实现Payment中的pay方法')

class Wechat(Payment):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        if isinstance(money, int) or isinstance(money, float):
            print(f'{self.name}通过微信支付了{money}元')


class Alipay(Payment):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        if isinstance(money, int) or isinstance(money, float):
            print(f'{self.name}通过支付宝支付了{money}元')
# 归一化设计
import sys
def pay(name, price, kind):
    '''
    :param name:
    :param price:
    :param kind: 类名
    :return: 判断kind是否可以反射，
        如果可以获取kind对应内存空间并实例化类，在调用类中的pay方法，return结果
    '''
    if hasattr(sys.modules['__main__'], kind):
        return getattr(sys.modules['__main__'], kind)(name).pay(price)


pay('alex', 10, 'Wechat')       # alex通过微信支付了10元
pay('alex', 10.10, 'Alipay')    # alex通过支付宝支付了10.1元
