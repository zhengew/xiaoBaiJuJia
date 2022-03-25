''' 闭包
定义:
1. 闭包只能存在嵌套函数中
2. 内层函数对外层函数非全局变量的引用(使用)，就会形成闭包。（定义）
3. 被引用的非全局变量也称为自由变量，这个自由变量会与内层函数产生一个绑定关系，自由变量不会在内存中消失。（现象）

作用：
1. 保证数据安全

如何判断一个嵌套函数是不是闭包？
# 函数名.__code__.co_freevars 查看函数的自由变量
print(avg.__code__.co_freevars)  # ('series',)

闭包多用于面试题：
什么是闭包？
闭包有什么作用？
'''

# 举例: 计算平均收盘价
def make_average():
    prices = [] # 存放每日收盘价

    def avg_price(price):
        prices.append(price)
        return round(sum(prices) / len(prices), 2)

    return avg_price # 外层函数return内层函数

avg = make_average()

print(avg(100))
print(avg(200))

print(avg.__code__.co_freevars) # 查看avg中是否有自由变量，如果有 就是 闭包