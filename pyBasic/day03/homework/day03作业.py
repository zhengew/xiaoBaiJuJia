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
# print(name.replace(" ",""))
# ```
#
# aleXleNb
#
# (3)
#
# ```python
# name = " aleX leNb "
# print(name.strip()[0:2])
# ```
#
# ```python
# name = " aleX leNb "
# print(name.strip().startswith("al"))
# ```
#
# al     True
#
# (4)
#
# ```python
# name = " aleX leNb "
# print(name.strip().endswith("Nb"))
# ```
#
# ```python
# name = " aleX leNb "
# print(name.strip()[-2:])
# ```
#
# True   Nb
#
# (5)
#
# ```python
# name = " aleX leNb "
# print(name.replace("l","p"))
# ```
#
#  apeX peNb
#
# (6)
#
# ```python
# name = " aleX leNb "
# print(name.replace("l","p",1))
# ```
#
#   apeX leNb
#
# (7)
#
# ```python
# name = " aleX leNb "print(name.split("l"))
# ```
#
# [' a', 'eX ', 'eNb ']
#
# (8)
#
# ```python
# name = " aleX leNb "print(name.upper())
# ```
#
#  ALEX LENB
#
# (9)
#
# ```python
# name = " aleX leNb "print(name.lower())
# ```
#
#  alex lenb
#
# (10)
#
# ```python
# name = " aleX leNb "print(name[1])
# ```
#
#  a
#
# (11)
#
# ```python
# name = " aleX leNb "print(name[:3])
# ```
#
#   al
#
# (12)
#
# ```python
# name = " aleX leNb "print(name[-2:])
# ```
#
# b
#
# 2.
#
# (1)
#
# ```python
# s = "123a4b5c"s1 = s[:3]print(s1)
# ```
#
# (2)
#
# ```python
# s = "123a4b5c"s1 = s[3:6]print(s1)
# ```
#
# (3)
#
# ```python
# s = "123a4b5c"s1 = s[-1]print(s1)
# ```
#
# (4)
#
# ```python
# s = "123a4b5c"s1 = s[1:-1:2]print(s1)
# ```
#
# (5)
#
# ```python
# s = "123a4b5c"s1 = s[-1:1:-2]print(s1)
# ```
#
# 3.
#
# ```python
# # 使用while循环字符串 s="你好世界" 中每个元素s="你好世界"l = len(s)n = 0while n < l:    print(s[n])    n += 1
# ```
#
# 4.
#
# ```python
# s="321"n = 0l = len(s)while l:    print("倒计时{}秒".format(s[n]))    l -= 1    n += 1
# ```
#
# 5.
#
# ```python
# # 使用for循环对s="321"进行循环，打印的内容依次是：# "倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"(提示使用字符串方法中的格式化)s="321"n = 0l = len(s)while l:    print("倒计时{}秒".format(s[n]))    l -= 1    n += 1else:    print("出发!")
# ```
#
# 6.
#
# ```python
# # 实现一个整数加法计算器(两个数相加)：num = input("请输入两位数加法")s = 0for i in num.replace(" ","").split("+"):    if i.isdecimal():        s += int(i)    else:        print("输入错误")        breakelse:    print(s)
# ```
#
# 7.
#
# ```python
# # 计算用户输入的内容中有几个 s 字符？input_user = input("请输入")print(input_user.count("s"))
# ```
#
# 8.
#
# ```python
# # 使用while循环分别正向和反向对字符串# message = "伤情最是晚凉天，憔悴厮人不堪言。" 进行打印。message = "伤情最是晚凉天，憔悴厮人不堪言。"l = len(message)n1 = 0n2 = -1while n1 < l:    print("%s" %(message[n1]),"%s" %(message[n2]))    n1 += 1    n2 -= 1
# ```
#
# 9.
#
# ```python
# # 获取用户输入的内容，并计算前四位"a"出现几次,并输出结果input_user = input("请输入")print(input_user[:4].count("a"))
# ```
#
# 10.
#
# ```python
# # 制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，# 根据⽤户的名字和爱好进⾏任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx (字符串格式化)input_name = input("请输入姓名:")input_address = input("请输入地点:")input_hobby = input("请输入爱好:")print("敬爱可亲的{name}，最喜欢在{address}地⽅⼲{hobby}"\      .format(name= input_name,address= input_address,hobby= input_hobby))
# ```
#
# 11.
#
# ```python
# # 判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海⾃来⽔来⾃海上says = input("请输入一句话:")i = 0j = len(says) -1while i <= j:    if says[i] != says[j]:        print("这句话不是回文")        break    i += 1    j -= 1else:    print("这句话是回文")
# ```
#
# 12.
#
# ```python
# # 输⼊⼀个字符串，要求判断在这个字符串中⼤写字⺟，# ⼩写字⺟，数字，其他共出现了多少次，并输出出来input_alpha = input("输入一段话:")u, l, d = 0, 0, 0for el in input_alpha:    if el.isdecimal():        d += 1    elif el.isupper():        u += 1    elif el.islower():        l += 1print("大写字母数量:%s\n小写字母数量:%s\n数字数量:%s\n其他数量:%s"\      %(u,l,d,len(input_alpha.replace(" ",""))-u-l-d))
# ```
#
# 13.
#
# ```python
# # 用户可持续输入（用while循环），用户使用的情况：# 输入A，则显示走大路回家，然后在让用户进一步选择：# 是选择公交车，还是步行？# 选择公交车，显示10分钟到家，并退出整个程序。# 选择步行，显示20分钟到家，并退出整个程序。# 输入B，则显示走小路回家，并退出整个程序。# 输入C，则显示绕道回家，然后在让用户进一步选择：# 是选择游戏厅玩会，还是网吧？# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。s = 1while s:    go_home1 = input("请输入A,B,C:")    if go_home1 == "A":        print("走大路回家")        while 1:            go_home2 = input("选择公交车，还是步行:")            if go_home2 == "公交车":                print("10分钟到家")                s = 0                break            elif go_home2 == "步行":                print("20分钟到家")                s = 0                break            else:                print("请正确输入!")    elif go_home1 == "B":        print("走小路回家")        s = 0    elif go_home1 == "C":        print("绕道回家")        while 1:            go_home2 = input("选择游戏厅玩会，还是网吧:")            if go_home2 == "游戏厅":                print("一个半小时到家，爸爸在家，拿棍等你。")                s = 0                break            elif go_home2 == "网吧":                print("两个小时到家，妈妈已做好了战斗准备。")                s = 0                break            else:                print("请正确输入!")    else:        print("请正确输入!")
# ```
#
