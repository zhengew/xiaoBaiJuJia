# 1.
#
# (1)
#
# ```python
# name = " aleX leNb "
# print(name.strip())
# ```
#
# aleX leNb
#
# (2)
#
# ```python
# name = " aleX leNb "
# print(name.replace(" ", ""))
# ```
#
# aleXleNb
#
# (3)
#
# ```python
# name = " aleX leNb "
# print(name[:3].strip())
# print(name.strip()[:2])
# ```
#
# name = " aleX leNb "
# print(name.strip().startswith("al"))
# al     True
#
# (4)
#
# ```python
# name = " aleX leNb "
# print(name.strip().endswith("Nb"))
# name = " aleX leNb "
# print(name.strip()[-2:])

# True   Nb
#
# (5)
#
# name = " aleX leNb "
# print(name.strip()[:4])
# print(name.strip()[-4:].replace("l", "p"))

#  apeX peNb
#
# (6)

# name = " aleX leNb "
# print(name.strip().replace("l", "p", 1))

#   apeX leNb
#
# (7)
#
# ```python
# name = " aleX leNb "
# print(name.split("l"))


# [' a', 'eX ', 'eNb ']
#
# (8)
#
# ```python
# name = " aleX leNb "
# print(name.strip().upper())

#  ALEX LENB
#
# (9)
#
# ```python
# name = " aleX leNb "
# print(name.strip().lower())
#
#  alex lenb
#
# (10)
#
# ```python
# name = " aleX leNb "
# ```
# print(name.strip()[0])
#  a
#
# (11)
#
# ```python
# name = " aleX leNb "
# ```
# print(name.strip()[:2])
#   al
#
# (12)
#
# ```python
# name = " aleX leNb "
# ```
# print(name.strip()[-1])

# b
#
# 2.
#
# (1)
#
# ```python
# s = "123a4b5c"
# print(s[:3])
# ```
#
# (2)
#
# ```python
# s = "123a4b5c"s1 = s[3:6] print(s1)
# ```
# a4b
# (3)
#
# ```python
# s = "123a4b5c" s1 = s[-1] print(s1)
# ```
# c
# (4)
#
# ```python
# s = "123a4b5c"
# s1 = s[1:-1:2]
# print(s1)
# ```
# 2ab
# (5)
#
# ```python
# s = "123a4b5c"
# ```
# print(s[-1::-2])
# cba2
# 3.
#
# ```python
# # 使用while循环字符串 s="你好世界" 中每个元素s="你好世界"l = len(s)n = 0while n < l:    print(s[n])    n += 1
# ```
# s="你好世界"
# len_s = len(s)
# index = 0
# while index < len_s:
#     print(s[index])
#     index += 1

# 4.
#
# ```python
# s="321" n = 0 l = len(s) while l:    print("倒计时{}秒".format(s[n]))    l -= 1    n += 1
# ```
# 打印倒计时321
# s = "321"
# len_s = len(s)
# index = 0
# while len_s > index:
#     print(f"倒计时{s[index]}秒")
#     index += 1


# 5.
#
# ```python
# # 使用for循环对s="321"进行循环，打印的内容依次是：# "倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"
# (提示使用字符串方法中的格式化)s="321"n = 0 l = len(s) while l:    print("倒计时{}秒".format(s[n]))
# l -= 1    n += 1else:    print("出发!")
# ```
# s = "321"
# len_s = len(s)
# index = 0
# while len_s > index:
#     print("倒计时{}秒".format(s[index]))
#     index += 1
# print("出发!")
# 6.
#
# ```python
# # 实现一个整数加法计算器(两个数相加)：
# num = input("请输入两位数加法")s = 0for i in num.replace(" ","").split("+"):
# if i.isdecimal():        s += int(i)    else:        print("输入错误")        breakelse:    print(s)
# ```

# num = input("请输入两位数加法：例如 2 + 5 ")
# sum = 0
# for i in num.replace(" ", "").split("+"):
#     if i.isdecimal():
#         sum += int(i)
#     else:
#         print("请输入数字!")
#         break
# print(sum)

# 7.
#
# ```python
# # 计算用户输入的内容中有几个 s 字符？input_user = input("请输入")print(input_user.count("s"))
# ```
# str = input("请输入：")
# print(str.count("s"))
# 8.
#
# ```python
# # 使用while循环分别正向和反向对字符串# message = "伤情最是晚凉天，憔悴厮人不堪言。" 进行打印。
# message = "伤情最是晚凉天，憔悴厮人不堪言。"l = len(message)n1 = 0n2 = -1while n1 < l:
# print("%s" %(message[n1]),"%s" %(message[n2]))    n1 += 1    n2 -= 1
# ```
#
# message = "伤情最是晚凉天，憔悴厮人不堪言。"
# print(message[::])
# print(message[-1::-1])

# len_message = len(message)
# index = 0
# while len_message > index:
#     print(message[index])
#     index += 1

# index = len(message) - 1
# while index > 0:
#     print(message[index])
#     index -= 1

# 9.
#
# ```python
# # 获取用户输入的内容，并计算前四位"a"出现几次,并输出结果input_user = input("请输入")print(input_user[:4].count("a"))
# ```

# str = input("请输入：")
# print(str[:4].count("a"))

# 10.
#
# ```python
# # 制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，# 根据⽤户的名字和爱好进⾏任意现实 如：
# 敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
# ```

# name = input("姓名：")
# place = input("地点：")
# hobby = input("爱好：")
# print("敬爱可亲的{},最喜欢在{}地方干{}".format(name, place, hobby))


# 11.
#
# ```python
# # 判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的.
# 例如, 上海⾃来⽔来⾃海上

# ```

# str = "上海⾃来⽔来⾃海上"
# if str == str[-1::-1]:
#     print(f"{str}，是回文")
# else:
#     print(f"{str},不是回文")



# 12.
#
# ```python
# # 输⼊⼀个字符串，要求判断在这个字符串中⼤写字⺟，# ⼩写字⺟，数字，其他共出现了多少次，并输出出来

# ```
# str = input("输入任意字符串：")
# count_lower = 0
# count_upper = 0
# count_digit = 0
# count_other = 0
#
# for i in str:
#     if i.isalpha():
#         if i == i.lower():
#             count_lower += 1
#         elif i == i.upper():
#             count_upper += 1
#     elif i.isdecimal():
#         count_digit += 1
#     else:
#         count_other += 1
# print(f"{str}中:\n"
#       f"大写字母出现{count_upper}次，\n"
#       f"小写字母出现{count_lower}次, \n"
#       f"数字出现{count_digit}次,\n"
#       f"其他类型出现{count_other}次")

# 13.
#
# ```python
# # 用户可持续输入（用while循环），用户使用的情况：
# 输入A，则显示走大路回家，然后在让用户进一步选择：
# 是选择公交车，还是步行？#
# 选择公交车，显示10分钟到家，并退出整个程序。#
# 选择步行，显示20分钟到家，并退出整个程序。#
# 输入B，则显示走小路回家，并退出整个程序。#
# 输入C，则显示绕道回家，然后在让用户进一步选择：
# 是选择游戏厅玩会，还是网吧？#
# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
# ```
#
selected = input("请选择回家方式：A 走大陆， B 走小路， C 绕道回家？")
while 1:
    if selected.isalpha():
        if selected.upper() == "A":
            info = input("走大陆回家，1.公交, 2.步行？")
            if info == "1":
                print("10分钟到家")
                break
            elif info == "2":
                print("20分钟到家")
                break
        elif selected.upper() == "B":
            print("走小路回家")
            break
        elif selected.upper() == "C":
            info = input("绕道回家，1.游戏厅, 2.网吧？")
            if info == "1":
                print("一个半小时到家，爸爸在家，拿棍等你。")
            elif info == "2":
                print("两个小时到家，妈妈已做好了战斗准备。")
            selected = input("请选择回家方式：A 走大陆， B 走小路， C 绕道回家？")

    else:
        print("输入错误！")

