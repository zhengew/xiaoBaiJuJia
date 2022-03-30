# 1. 计算阶乘 5! = 5*4*3*2*1
    # 循环
    # 递归
def func(num):
    if num == 1:
        return num
    else:
        return num * func(num - 1)
res = func(5)
print(res)
# # 第一步 递
# def func(5):
#     5 * func(4)
#
# def func(4):
#     4 * func(3)
#
# def func(3):
#     3 * func(2)
#
# def func(2):
#     2 * func(1)
#
# def func(1):
#     1 * func(0)
#     # 所以得出如果num == 1 时，要返回num
#
# # 第二步 归
# def func(5):
#     return 5 * 4 * 3 * 2 * 1
#
# def func(4):
#     return 4 * 3 * 2 * 1
#
# def func(3):
#     return 3 * 2 * 1
#
# def func(2):
#     return 2 * 1
#
# def func(1):
#     1 * func(0)
#     return 1
#     # 所以得出如果num == 1 时，要返回num