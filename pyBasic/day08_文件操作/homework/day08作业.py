# 1.有如下文件，a1.txt，里面的内容为：
# 老男孩是最好的学校，
# 全心全意为学生服务，
# 只为学生未来，不为牟利。
# 我说的都是真的。哈哈
#
# 分别完成以下的功能：
# a,将原文件全部读出来并打印。
# b,在原文件后面追加一行内容：信不信由你，反正我信了。
# c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
# d,将原文件全部清空，换成下面的内容：
# 每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你会发现，
# 你的进步越来越大。
# f1 = open("a1.txt", mode="r+", encoding="utf-8")
# print(f1.read())
# f1.write('信不信由你，反正我信了。')
# f1.close()
# f1 = open("a1.txt", mode="w", encoding="utf-8")
# f1.write\
# ('''每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你会发现，
# 你的进步越来越大。''')
# f1.close()



#
# 2.有如下文件，t1.txt,里面的内容为：
#
# 葫芦娃，葫芦娃，
# 一根藤上七个瓜
# 风吹雨打，都不怕，
# 啦啦啦啦。
# 我可以算命，而且算的特别准:
# 上面的内容你肯定是心里默唱出来的，对不对？哈哈
#
# 分别完成下面的功能：
#
# a,以r的模式打开原文件，利用for循环遍历文件句柄。
# b,以r的模式打开原文件，以readlines()方法读取出来，并循环遍历 readlines(),
# 并分析b,与c 有什么区别？深入理解文件句柄与 readlines()结果的区别。
# c,以r模式读取‘葫芦娃，’前四个字符。
# d,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
# e,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将 原内容全部读取出来。
#
# f1 = open("../day1/files1/t1.txt", mode='r', encoding='utf-8')
# for line in f1:
#     print(line)
# f1 = open("../day1/files1/t1.txt", mode='r', encoding='utf-8')
# for line in f1.readlines():
#     print(line)
# with open("../day1/files1/t1.txt", mode='r', encoding='utf-8') as f1:
#     print(f1.read(4))
# with open("../day1/files1/t1.txt", mode='r', encoding='utf-8') as f1:
#     print(f1.readline().strip())
# with open("../day1/files1/t1.txt", mode='a+', encoding='utf-8') as f1:
#     f1.write('老男孩教育')
#     f1.seek(0)
#     print(f1.read())





# 3.文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
#
# apple 10 3
# tesla 100000 1
# mac 3000 2
# lenovo 30000 3
# chicken 10 3
#
# 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
#
# with open('a.txt', mode='r', encoding='utf-8') as f1:
#     dic = {}
#     l = []
#     for line in f1:
#         lst = line.strip().split(" ")
#         dic['name'] = dic.get('name', lst[0])
#         dic['price'] = dic.get('price', lst[1])
#         dic['amount'] = dic.get('amount', lst[2])
#         l.append(dic)
# print(l)









# 4.有如下文件：
#
# alex是老男孩python发起人，创建人。
# alex其实是人妖。
# 谁说alex是sb？
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
# 将文件中所有的alex都替换成大写的SB（文件的改的操作）。
# with open('f.txt', mode='r', encoding='utf-8') as f1\
#         ,open('f_1.txt', mode='w', encoding='utf-8') as f2:
#     for line in f1:
#         f2.write(line.replace("alex", 'SB'))
# import os
# os.remove('f.txt')
# os.rename('f_1.txt','f.txt' )


# 5.文件a1.txt内容(升级题)
#
# name:apple price:10 amount:3 year:2012
#
# name:tesla price:100000 amount:1 year:2013
#
# .......
#
# 通过代码，将其构建成这种数据类型：
#
# [{'name':'apple','price':10,'amount':3,year:2012},
#
# {'name':'tesla','price':1000000,'amount':1}......]
#
# 并计算出总价钱。

# with open('a.txt', mode='r', encoding='utf-8') as f1:
#     l = []
#     for line in f1:
#         dic = {}
#         lst = line.strip().split(' ')
#         for i in lst[:3]:
#             dic.setdefault(i.split(':')[0], i.split(':')[1])
#         l.append(dic)
# s = 0
# for n in l:
#     s += int(n['price'])*int(n['amount'])
# print(s)
#


# 6.文件a1.txt内容(升级题)
#
# 序号 部门 人数 平均年龄 备注
#
# 1 python 30 26 单身狗
#
# 2 Linux 26 30 没对象
#
# 3 运营部 20 24 女生多
#
# .......
#
# 通过代码，将其构建成这种数据类型：
#
# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},
#
# ......]
#
# with open('a1.txt', mode='r', encoding='utf-8') as f1:
#     d = {}
#     l = []
#     for key in f1.readline().strip().split(' '):
#         d.setdefault(key)
#     for line in f1:
#         if len(line.strip()) != 0:
#             dic = {}
#             n = -1
#             for key in d:
#                 lst = line.strip().split(' ')
#                 n += 1
#                 dic[key] = lst[n]
#             l.append(dic)
# print(l)