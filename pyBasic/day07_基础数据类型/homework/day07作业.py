# 2.
# ```
# 2.用户输入一个数字，判断一个数是否是水仙花数。
#
# 水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数. 那这个数就是一个水仙花数,\
# 例如: 153 = 1**3 + 5**3 + 3**3
# num = input("请输入任意数字：")
# result = 0
# while num:
#     if num.isdecimal():
#         for i in range(len(num)):
#             result += int(num[i]) ** 3
#         if result == int(num):
#             print(f"{num}是水仙花")
#         else:
#             print(f"{num}不是水仙花")
#     else:
#         print("输入错误!")
#     num = input("请输入任意数字：")

# ```
#
# 3.
#
# ```
# 3.请说出下面a,b,c三个变量的数据类型。
# a = ('太白金星') # 字符串，元组如果只有一个元素，元素后面需要加上逗号分隔
# a = ('太白金星',)
# print(a, type(a))
# b = (1,) # 元组
# c = ({'name': 'barry'}) # 字典
# c = ({'name': 'barry'}) # {'name': 'barry'} <class 'dict'>
# print(c, type(c))
# c = ({'name': 'barry'},) # ({'name': 'barry'},) <class 'tuple'>
# print(c, type(c))

''' 注意: 元组或者集合，如果只有一个元素，且没有逗号分隔，则元素是什么类型就是什么类型 '''
#   a:字符串   b:元组    c:字典
# ```
# 4.
# ```
# 4.按照需求为列表排序：
l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# 从大到小排序
# l1.sort(reverse=True)
# print(l1)

# 从小到大排序
# l1.sort(reverse=False)
# print(l1)
# 反转l1列表
# l1.reverse()
# print(l1)
# ```

# 5.
# ```
# 5.看代码写结果：
# dic = dict.fromkeys('abc',[]) # {"a":[], "b":[], "c":[]}
# dic['a'].append(666)  # {"a":[666], "b":[666], "c":[666]}
# dic['b'].append(111)  # {"a":[666, 111], "b":[666, 111], "c":[666, 111]}
# print(dic)

# fromkeys 生成的字典，value都是相同的，执行内存中同一个地址，如果是可变类型，则改变任意一个键值对，其他的键值对也会改变

# ```
# 6.
# ```
# 6.完成彩票36选7的功能. 从36个数中随机的产生7个数. 最终获取到7个不重复的数据作为最终的开奖结果.
# 随机数:
# from random import randint
#
# random_nums = set()
# result = ""
#
# while len(random_nums) < 7:
#     random_nums.add(randint(0, 35))
#
# for i in random_nums:
#     result += str(i) + " "
# print("彩票开奖号码为:" + result[:-1])

# ```
# 7.
# ```
# 7.字符串和字节转换
# s1 = '太白金星'
# 将s1转换成utf-8的bytes类型。
# b_utf8 = s1.encode(encoding="utf-8")
# print(b_utf8)

# 将s1转化成gbk的bytes类型。
# unicode_b = b_utf8.decode(encoding="utf-8")
# b_gbk = unicode_b.encode(encoding="gbk")
# print(b_gbk)

# b = b'\xe5\xa4\xaa\xe7\x99\xbd\xe6\x9c\x80\xe5\xb8\x85'
# b为utf-8的bytes类型，请转换成gbk的bytes类型。
# bytes_gbk = b.decode(encoding="utf-8").encode(encoding="gbk")
# print(bytes_gbk)
# print(bytes_gbk.decode("gbk"))

# ```
# 8.
# ```
# 8.把列表中所有姓周的⼈的信息删掉(升级题：此题有坑, 请慎重):
# lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
# 结果: lst = ['麻花藤']
# lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
# del_name = []
#
# for name in lst:
#     if name.startswith("周"):
#         del_name.append(name)
#
# for name in del_name:
#     if name in lst:
#         lst.remove(name)
# print(lst)

# ```
# 9.
# ```
# 9.⻋牌区域划分, 现给出以下⻋牌. 根据⻋牌的信息, 分析出各省的⻋牌持有量. (升级题)
cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南','京':'北京'}
# # 结果: {'⿊⻰江':2, '⼭东': 2, '北京': 1,'上海':1}
# key_info = list(locals.keys())
# dicts = dict.fromkeys(key_info, 0)
# result = {}
#
# for info in cars:
#     for key in key_info:
#         if info.startswith(key):
#             dicts[key] += 1
#
# for k, v in dicts.items():
#     if v > 0:
#         result[locals[k]] = v
#
# print(result)

# 方式二 先通过 setdefault(key, value) 创建字典，再通过 dic[key]改变键值
# dic = {}
# for iname in cars:
#     dic.setdefault(locals[iname[0]],0)
#     dic[locals[iname[0]]] += 1
#
# print(dic)


# ```
# 10.
#
# ```
# # 10.⼲掉主播. 现有如下主播收益信息:
# zhubo = {'卢本伟':122000, '冯提莫':189999, '⾦⽼板': 99999, '吴⽼板': 25000000, 'alex': 126}
# 1. 计算主播平均收益值 2. ⼲掉收益⼩于平均值的主播 3. ⼲掉卢本伟
zhubo = {'卢本伟':122000, '冯提莫':189999, '⾦⽼板': 99999, '吴⽼板': 25000000, 'alex': 126}

sum_shouY = 0.0

for v in list(zhubo.values()):
    sum_shouY += v

avg_shouY = round(sum_shouY / len(zhubo), 2)

del_zhuno = []
for k, v in zhubo.items():
    if v < avg_shouY or k == "卢本伟":
        del_zhuno.append(k)

for name in del_zhuno:
    zhubo.pop(name)

print(f"主播平均收益为:{avg_shouY}")
print(zhubo)


# ```