'''
列表的增删改查

增：
直接按照索引增 li[0] = 'test'
append() 追加
insert() 按索引增
list.extend("abc") 迭代着追加元素

删：
pop() 有返回值删除，默认删除最后一个，可指定索引位置
remove() 按元素删除, 若元素不存在则抛出 ValueError异常
del list[index] 按索引删，切片删，切片步长删
list.clear() 清空列表，返回一个值为[]

改：
list[index] = value 通过索引改
list1 = list1 + list2  列表相加
切片改
切片步长改

查：
list[索引]
切片查
切片步长查
循环查
'''


# 1.
#
# ```python
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# # 1)计算列表的长度并输出
# print(len(li))

# # 2)列表中追加元素
# # "seven", 并输出添加后的列表
# li.append("seven")
# print(li)

# # 3)请在列表的第1个位置插入元素
# # "Tony", 并输出添加后的列表
# li.insert(0, "Tony")
# print(li)
#
# # 4)请修改列表第2个位置的元素为
# # "Kelly", 并输出修改后的列表
# li[1] = "Kelly"
# print(li)
#
# # 5)请将列表l2 = [1, "a", 3, 4, "heart"]
# # 的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# l2 = [1, "a", 3, 4, "heart"]
# li.extend(l2)
# print(li)
# # 6)请将字符串s = "qwert"
# # 的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# s = "qwert"
# li.extend(s)
# print(li)
#
# # 7)请删除列表中的元素
# # "ritian", 并输出输出后的列表
# li.remove("ritian")
# print(li)
#
# #
# # 8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# print(li)
# element = li.pop(1)
# print(element)
# # 9)请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:4]
# print(li)

# # 10)请将列表所有得元素反转，并输出反转后的列表
# li = li[-1::-1]
# print(li)

# # 11)请计算出
# # "alex" 元素在列表li中出现的次数，并输出该次数。
# print(li)
# count_alex = li.count("alex")
# print(count_alex)
# ```
#
# 2.
#
# ```python
# # li = [1, 3, 2, "a", 4, "b", 5, "c"]
# # 1)通过对li列表的切片形成新的列表l1, l1 = [1, 3, 2]
# # 2)通过对li列表的切片形成新的列表l2, l2 = ["a", 4, "b"]
# # 3)通过对li列表的切片形成新的列表l3, l3 = ["1,2,4,5]
# # 4)通过对li列表的切片形成新的列表l4, l4 = [3, "a", "b"]
# # 5)通过对li列表的切片形成新的列表l5, l5 = ["c"]
# # 6)通过对li列表的切片形成新的列表l6, l6 = ["b", "a", 3]
li = [1, 3, 2, "a", 4, "b", 5, "c"]
l1 = li[:3]
l2 = li[3:-2]
l3 = li[::2]
l4 = li[1:-1:2]
l5 = li[-1:]
l6 = li[-3::-2]
# ```
# 3.
#
# ```python
# # lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# # 1)将列表lis中的"tt"变成大写（用两种方式）。
# #
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][0] = "TT"
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)
#
# # 2)将列表中的数字3变成字符串"100"（用两种方式）。
# #
lis[1] = 100
lis[3][2][1][1] = 100
# print(lis)

# # 3)将列表中的字符串"1"变成数字101（用两种方式）。
# lis[3][2][1][2] = 101
# print(lis)
lis[3][2][1].remove("1")
lis[3][2][1].append(101)
# print(lis)

# ```
#
# 4.
#
# ```python
li = ["alex", "wusir", "taibai"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"
str = ""
for i in range(len(li)):
    if i == len(li) - 1:
        str += li[i]
    else:
        str += li[i] + "_"
# print(str)
# ```
#
# 5.
#
# ```python
# # 利用for循环和range打印出下面列表的索引
# #
# li = ["alex", "WuSir", "ritian", "barry", "wenzho"]
# for i in range(len(li)):
#     print(i)

# ```
#
# 6.
#
# ```python
# # 利用while循环打印出下面列表的索引
#
li = ["alex", "WuSir", "ritian", "barry", "wenzho"]

# index = 0
# while len(li) > index:
#     print(index)
#     index += 1

# ```
#
# 7.
#
# ```python
# # 利用for循环和range找出100以内所有的偶数并将这些偶数添加到一个新列表中。
# li = []
# for i in range(2, 101):
#     if i % 2 == 0:
#         li.append(i)
# print(li)

# ```
#
# 8.
#
# ```python
# # 利用for循环和range找出50以内能被3整除的数，并将这些数插入到一个新列表中。
li = []

# for i in range(3, 51):
#     if i % 3 == 0:
#         li.append(i)
# print(li)
# ```
#
# 9.
#
# ```python
# # 利用for循环和range从100~1，倒序打印
# for i in range(100, 0, -1):
#     print(i)
#
# 10.
#
# ```python
# # 利用for循环和range打印100~10，
# # 倒序将所有的偶数添加到一个新列表中，然后在对列表的元素进行筛选，将能被4整除的数留下来。
# list1 = []
# for i in range(100, 9, -1):
#     print(i)
#     if i % 2 == 0:
#         list1.append(i)
# for i in list1:
#     if i % 4 != 0:
#         list1.remove(i)
# print(list1)
# ```
#
# 11.
#
# ```python
# # 利用for循环和range，将1-30的数字依次添加到一个列表中，并循环这# 个列表，将能被3整除的数改成*。
# lis = []
# for i in range(1, 31):
#     if i % 3 == 0:
#         i = "*"
#     lis.append(i)
# print(lis)
# ```
#
# 12.
#
# ```python
# # 查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，# 并添加到一个新列表中,最后循环打印这个新列表。
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
# lis = []
# for i in li:
#     if i.strip().startswith("A") and i.strip().endswith("c") or i.strip().startswith("a") and i.strip().endswith("c"):
#         lis.append(i.strip())
#
# for i in lis:
#     print(i)


# ```
#
# 13.
#
# ```python
# # 开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：#
# 敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]#
# 则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；
# 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# lis = []
# str = input("请输入：")
# while str:
#     for i in li:
#         str = str.replace(i, "*" * len(i))
#     lis.append(str)
#     str = input("请输入：")
# print(lis)
# ```
#
# 14.
#
# ```python
# # 有如下列表（选做题）
# # li = [1, 3, 4, "alex", [3, 7, 8, "BaoYuan"], 5, "RiTiAn"]
# # 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
li = [1, 3, 4, "alex", [3, 7, 8, "BaoYuan"], 5, "RiTiAn"]
#
for i in li:
    if type(i) == list:
        for j in i:
            print(j)
        continue
    print(i)
# ```