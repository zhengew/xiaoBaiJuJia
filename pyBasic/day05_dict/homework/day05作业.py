# ```
# # 1.有如下这个字典:
# # dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# #
# # 循环打印字典中所有的键(两种方式)
# # for key in dic:
# #     print(key)
# # for key in dic.keys():
# #     print(key)
# # 循环打印字典中所有的值(两种方式)
# # for key in dic:
# #     print(dic[key])
# # for value in dic.values():
# #     print(value)
# # 循环打印字典中所有的键和值(两种方式)
# # for key in dic:
# #     print(key,dic[key])
# # for key,value in dic.items():
# #     print(key,value)
# # 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典 (两种方式)
# # dic["k4"] = "v4"
# # dic.setdefault("k4","v4")
# # print(dic)
# # 请修改字典中"k1"对应的值为"alex"，输出修改后的字典
# # dic["k1"] = "alex"
# # print(dic)
# # 请在k3对应的值中追加一个元素44，输出修改后的字典
# # dic["k3"].append(44)
# # print(dic)
# # 请在k3对应的值的第1个位置插入个元素18，输出修改后的字典
# # dic["k3"].insert(0,18)
# # print(dic)
# ```
#
# 2.
#
# ```
# dic1 = {
#  'name':['alex',2,3,5],
#  'job':'teacher',
#  'oldboy':{'alex':['python1','python2',100]}
#  }
#
# # 1，将name对应的列表追加⼀个元素’wusir’。
# dic1["name"].append("wusir")
# print(dic1)
#
# # 2，将name对应的列表中的alex⾸字⺟⼤写。
# dic1["name"][0] = dic1["name"][0].capitalize()
# print(dic1)
# # 3，oldboy对应的字典加⼀个键值对’⽼男孩’,’linux’。
# dic1["oldboy"]["老男孩"] = "linux"
# print(dic1)
# # 4，将oldboy对应的字典中的alex对应的列表中的python2删除
# dic1['oldboy']["alex"].remove("python2")
# print(dic1)
# ```
#
# 3.
#
# ```
# # 有如下这个字典,请完成一下的方法:
#
# av_catalog = {
#     "欧美":{
#         "www.太白.com": ["很多免费的,世界最大的","质量一般"],
#         "www.alex.com": ["很多免费的,也很大","质量挺好"],
#         "oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "hao222.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
# # 给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'量很大'。
# # av_catalog["欧美"]["www.太白.com"].insert(1,"量很大")
# # print(av_catalog)
#
# # 将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# # av_catalog["欧美"]["hao222.com"].remove("全部收费,屌丝请绕过")
# # print(av_catalog)
#
# # 将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# # av_catalog["日韩"]["tokyo-hot"][1] = av_catalog["日韩"]["tokyo-hot"][1].upper()
# # print(av_catalog)
# # 给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# # av_catalog['大陆']['1048'] = ['一天就封了']
# # print(av_catalog)
#
# # 删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
# # del av_catalog["欧美"]["oldboy.com"]
# # print(av_catalog)
#
# # 给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# # av_catalog['大陆']['1024'][0] = av_catalog['大陆']['1024'][0]+'可以爬下来'
# # print(av_catalog)
# ```
#
# 4.
#
# ```
# # 将下方的字典中k2对应的值循环打印
#
# info = {
# "k1":"v1",
# "k2":["alex","wusir","oldboy"],
# }
# for k2_value in info["k2"]:
#     print(k2_value)
# ```
#
# 5.
#
# ```
# # 有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}
# s = "k: 1|k1:2|k2:3 |k3 :4"
# l1 = s.replace(" ","").split("|")
# l2 = []
# dic = {}
# n = 0
# for i in l1:
#     l2.append(i.split(":"))
# for key,value in l2:
#     dic.setdefault(key,value)
# print(dic)
# ```
#
# 6.
#
# ```
# # 有如下值 li= [11,22,33,44,55,77,88,99,90] ,将所有大于 66 的值保存至字典
# # 的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
# dic = {}
# li= [11,22,33,44,55,77,88,99,90]
# for i in li:
#     if i < 66:
#         dic.setdefault("小于66",[])
#         dic["小于66"].append(i)
#     else:
#         dic.setdefault("大于66", [])
#         dic["大于66"].append(i)
# print(dic)
# ```
#
# 7.
#
# ```
# # 看代码写结果(一定要自己先推测一下结果,然后在验证)
# #
# # v = {}
# #
# # for index in range(10):
# #
# #  v['users'] = index
# #
# # print(v)
#
#
#
# {'user': 9}
# ```
#
# 8.
#
# ```
# # 输出商品列表，用户输入序号，显示用户选中的商品
# #
# # 商品列表：
#
# goods = [
#     {"name": "电脑", "price": 1999},
#
#     {"name": "鼠标", "price": 10},
#
#     {"name": "游艇", "price": 20},
#
#     {"name": "美女", "price": 998}
# ]
#
# # 要求:
# #
# # 1：页面显示 序号 + 商品名称 + 商品价格，如：
# #
# # 1 电脑 1999
# #
# # 2 鼠标 10
# #
# # ...
# #
# # 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# #
# # 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入(while)
# #
# # 4：用户输入Q或者q，退出程序。
#
# n = 1
# for dic in goods:
#     print(n,dic["name"],dic["price"])
#     n += 1
# while 1:
#     index = input("输入商品序号:")
#     if index > "0" and index < "5":
#         print("%s %s" %(goods[int(index)-1]["name"],goods[int(index)-1]["price"]))
#         break
#     elif index.upper() == "Q":
#         break
#     else:
#         print("输入序号不正确")
# ```