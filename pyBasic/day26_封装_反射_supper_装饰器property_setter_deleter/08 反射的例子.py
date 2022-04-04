''' 利用反射优化 归一化设计 '''

# class Payment:pass
#
# class Alipay(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'uname':self.name, 'price':money}
#         # 想办法调用支付宝支付 url连接 把dic传过去
#         print('%s通过支付宝支付%s钱成功' %(self.name, money))
#
# class WeChat(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'username':self.name, 'monye':money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过微信支付%s钱成功' %(self.name, money))
#
# class Apple(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'username': self.name, 'number': money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过苹果支付%s钱成功' % (self.name, money))
#
# class QQpay(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'username': self.name, 'number': money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过QQ支付%s钱成功' % (self.name, money))
#
# import sys
# aw = WeChat('alex')
# aw.pay(400)
# aa = Alipay('alex')
# aa.pay(400)

'''归一化设计 '''
# def pay(name, price, kind):
#     # 反射优化版本
#     class_name = getattr(sys.modules['__main__'], kind)  # 通过反射获取了本文件中对应类的内存地址
#     obj = class_name(name)
#     obj.pay(psssssrice)

    # 原始版本
    # if kind == 'Wechat':
    #     obj = WeChat(name)
    # elif kind == 'Alipay':
    #     obj = Alipay(name)
    # elif kind == 'Apple':
    #     obj = Apple(name)
    #
    # obj.pay(price)

# pay('alex', 400, 'WeChat')
# pay('alex', 400, 'Alipay')
# pay('alex', 100, 'Apple')
# pay('alex', 100, 'QQpay')