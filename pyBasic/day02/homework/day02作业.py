# # Day02作业
#
# 1.
#
# ```
# # 猜数字，设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了,然后继续让用户输入;
# # 如果比66小，则显示猜测的结果小了,然后继续让用户输入;只有等于66，显示猜测结果正确，然后退出循环。
# while 1:
#     num = input("请输入数字：")
#     if num.isdigit():
#         num = int(num)
#         if num > 66:
#             print("猜大了")
#         elif num < 66:
#             print("猜小了")
#         else:
#             print("恭喜你猜对了")
#             break
#     else:
#         print("请输入数字！")


#
# 2.
#
# ```
# # 在上一题的基础，设置：给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，
# # 退出循环，如果三次之内没有猜测正确，则自动退出循环，并显示‘大笨蛋’
# i= 3
# while i > 0:
#     num = input("请输入数字：")
#     if num.isdigit():
#         num = int(num)
#         if num > 66:
#             print("大了")
#         elif num < 66:
#             print("小了")
#         else:
#             print("猜对了")
#             break
#     else:
#         print("请输入数字!")
#     i -= 1
# else:
#     print("大笨蛋")
# ```
#
# 3.
#
# ```
# 判断下列逻辑语句的True,False
# 逻辑运算符优先级 not > and > or,同级别从左往右运算
# 1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# False or True or False and True and True or False
# False or True or False or False
# True
# not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# not True and True or False and True and True or False
# False and True or False and True and True or False
# False or False or False
# False
# 4.
#
# ```
# 求出下列逻辑语句的值。
# 非0即True
# 8 or 3 and 4 or 2 and 0 or 9 and 7

# 0 or 2 and 3 and 4 or 6 and 0 or 3

# ```
#
# 5.
#
# ```
# 下列结果是什么？
#
# 6 or 2 > 1
# 答案:6
# 3 or 2 > 1
# 答案:3
# 0 or 5 < 4
# 答案:F
# 5 < 4 or 3
# 答案:3
# 2 > 1 or 6
# 答案:T
# 3 and 2 > 1
# 答案:T
# 0 and 3 > 1
# 答案:0
# 2 > 1 and 3
# 答案:3
# 3 > 1 and 0
# 答案:0
# 3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
# 答案:2
# ```
#
# 6.
#
# ```
# # 使用while循环输出 1 2 3 4 5 6 8 9 10
# i = 1
# while i < 11:
#     if i == 7:
#         i += 1
#     print(i)
#     i += 1
#
# for i in range(1, 11):
#     if i == 7:
#         continue
#     print(i)
# ```
#
# 7.
#
# ```
# # 求1-100的所有数的和

# i = 1
# sum = 0
# while i < 101:
#     sum += i
#     i += 1
# print(sum)
#
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)
# ```
#
# 8.
#
# ```
# # 求1-100的所有数的和
# i =100
# while i:
#     if (i%2) != 0:
#         print(i)
#     i -= 1
# ```
#
# 9.
#
# ```
# # 求1-100的所有数的和
# i =100
# while i:
#     if (i%2) == 0:
#         print(i)
#     i -= 1
# ```
#
# 10.
#
# ```
# # 求1-100的所有数的和
# i =99
# sum = 0
# while i:
#     if (i%2) == 0:
#         sum -= i
#     else:
#         sum += i
#     i -= 1
# print(sum)
# ```
#
# 11.
#
# 简述ASCII、Unicode、utf-8编码英文和中文都是用几个字节?
#
# ASCII:英文1个字节,无中文
#
# Unicode:英文2个字节,中文4个字节
#
# utf-8:英文1个字节.中文3个字节
#
# 12.
#
# 简述位和字节的关系？
#
# 8bit = 1byte
#
# 13.
#
# "老男孩"使用GBK占几个字节,使用Unicode占用几个字节?
#
# 不算引号的话,GBK占用6个字节,Unicode占用12个字节
#
# 14.
#
# ```
# # 猜年龄游戏升级版 要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，
# # 就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。
# flag = 3
# while flag:
#     num = input("猜数字：")
#     if num.isdigit():
#         num = int(num)
#         if num > 66:
#             print("大了")
#         elif num < 66:
#             print("小了")
#         else:
#             print("恭喜你答对了")
#             break
#         flag -= 1
#
#         if flag <= 0:
#             qaq = input("是否继续？Y or N ")
#             if qaq.upper() == "Y":
#                 flag = 3
#             elif qaq.upper() == "N":
#                 print("退出游戏")
#                 break
#     else:
#         print("请输入数字!")


#
# 15.
#
# ```
# # ⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
flag = 3
username = "test1"
password = "123456"
while flag:
    name = input("请输入用户名：")
    pwd = input("请输入密码：")
    if name != username or pwd != password:
        flag -= 1
        print("用户名或密码错误，还有%d次机会" % flag)
    else:
        print("登陆成功")
else:
    print("用户被锁定")

# 附录:
#
# 14改:
#
# ```
# s,i = 1,3
# while s:
#     while i:
#         num = int(input("请输入数字:"))
#         if num < 66:
#             print("小了")
#         elif num > 66:
#             print("大了")
#         else:
#             print("正确")
#             s = 0
#             break
#         i -= 1
#     if s == 1:
#         nxt = input("是否继续玩?是请按Y,不是请按N")
#         if nxt == "Y":
#             s,i = 1,3
#         elif nxt == "N":
#             break
# ```