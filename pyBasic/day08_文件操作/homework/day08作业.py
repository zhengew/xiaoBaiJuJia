# 1.有如下文件，a1.txt，里面的内容为：
# 老男孩是最好的学校，
# 全心全意为学生服务，
# 只为学生未来，不为牟利。
# 我说的都是真的。哈哈
# filename = "..//files//a1.txt"
# with open(file=filename, mode="w", encoding="utf-8") as write_f:
#     msg = "老男孩是最好的学校，\n全心全意为学生服务，\n只为学生未来，不为牟利。\n我说的都是真的。哈哈"
#     write_f.write(msg)

# 分别完成以下的功能：

# a,将原文件全部读出来并打印。
# with open(file=filename, mode="r", encoding="utf-8") as read_f:
#     for line in read_f:
#         print(line.strip())

# b,在原文件后面追加一行内容：信不信由你，反正我信了。
# with open(file=filename, mode="a", encoding="utf-8") as write_f:
#     write_f.write("\n信不信由你，反正我信了。")
#     write_f.flush()
# c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
# with open(file=filename, mode="r+", encoding="utf-8") as rw_f:
#     for line in rw_f:
#         print(line.strip())
#     rw_f.write("\n信不信由你，反正我信了。")
#
# print("*".center(20))
# d,将原文件全部清空，换成下面的内容：
# 每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你会发现，
# 你的进步越来越大。
# with open(file=filename, mode="r", encoding="utf-8") as r_f, open(file=filename, mode="w", encoding="utf-8") as w_f:
#     for line in r_f:
#         line = line.replace("")
#     msg = "每天坚持一点，\n每天努力一点，\n每天多思考一点，\n慢慢你会发现，\n你的进步越来越大。"
#     r_f.seek(0)
#     w_f.write(msg)



#
# 2.有如下文件，t1.txt,里面的内容为：
#
# 葫芦娃，葫芦娃，
# 一根藤上七个瓜
# 风吹雨打，都不怕，
# 啦啦啦啦。
# 我可以算命，而且算的特别准:
# 上面的内容你肯定是心里默唱出来的，对不对？哈哈
filename = "..//files//t1.txt"
with open(file=filename, mode="w", encoding="utf-8") as write_f:
    msg = '''
        葫芦娃，葫芦娃，
        一根藤上七个瓜
        风吹雨打，都不怕，
        啦啦啦啦。
        我可以算命，而且算的特别准:
        上面的内容你肯定是心里默唱出来的，对不对？哈哈
    '''
    write_f.write(msg.strip().replace(" ", ""))
    write_f.flush()
# 分别完成下面的功能：
#
# a,以r的模式打开原文件，利用for循环遍历文件句柄。
# with open(file=filename, mode="r", encoding="utf-8") as r_f:
#     for line in r_f:
#         print(line.strip())

# b,以r的模式打开原文件，以readlines()方法读取出来，并循环遍历 readlines(),
# with open(file=filename, mode="r", encoding="utf-8") as r_f:
#     for line in r_f.readlines():
#         print(line.strip())

# 并分析b,与c 有什么区别？深入理解文件句柄与 readlines()结果的区别。
# c,以r模式读取‘葫芦娃，’前四个字符。
# with open(file=filename, mode="r", encoding="utf-8") as r_f:
#     print(r_f.read(4))

# d,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
# with open(file=filename, mode="r", encoding="utf-8") as r_f:
#     print(r_f.readline())

# e,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将 原内容全部读取出来。
#
# with open(file=filename, mode="a+", encoding="utf-8") as a_f:
#     a_f.write("\n老男孩教育")
#     a_f.seek(0)
#     for line in a_f:
#         print(line.strip())


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
# with open(file="..//files//a1.txt", mode="w", encoding="utf-8") as w_f:
#     msg = "apple 10 3\ntesla 100000 1\nmac 3000 2\nlenovo 30000 3\nchicken 10 3"
#     w_f.write(msg)
#     w_f.flush()
#
# with open(file="..//files//a1.txt", mode="r", encoding="utf-8") as w_f:
#     infos = []
#     for line in w_f:
#         infos.append(line.strip().split(" "))
#
#     # 列表，元素为字典
#     list_infos = []
#     result = 0.0
#     for i in range(len(infos)):
#         dic = {"name":infos[i][0], "price":infos[i][1], "amount":infos[i][2]}
#         list_infos.append(dic)
#         result += float(infos[i][1])
#
#     # 输出列表及总价（太墨迹了，应该有更简单的方法）：
#     print(list_infos, result)


# 4.有如下文件：
#
# alex是老男孩python发起人，创建人。
# alex其实是人妖。
# 谁说alex是sb？
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
# 将文件中所有的alex都替换成大写的SB（文件的改的操作）。
# import os
#
# filename = "..//files//alex.txt"
# with open(file = filename, mode="w") as r_f:
#     msg = '''
#         alex是老男孩python发起人，创建人。
#         alex其实是人妖。
#         谁说alex是sb？
#         你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
#         将文件中所有的alex都替换成大写的SB（文件的改的操作）
#     '''
#     r_f.write(msg)
#
# with open(file=filename, mode="r", encoding="utf-8") as r_f, open(file=filename[:-4] + "1.txt", mode="w", encoding="utf-8") as w_f:
#     for line in r_f:
#         line = line.replace("alex", "SB")
#         w_f.write(line)
#
# os.remove(filename)
# os.rename(filename[:-4] + "1.txt", filename)

# 5.文件a1.txt内容(升级题)
# name:apple price:10 amount:3 year:2012
# name:tesla price:100000 amount:1 year:2013
# .......
# 通过代码，将其构建成这种数据类型：
#
# [{'name':'apple','price':10,'amount':3,year:2012},
#
# {'name':'tesla','price':1000000,'amount':1}......]
#
# 并计算出总价钱。



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

## 最后两道题先暂停，之后再写。。 20220323 17：25