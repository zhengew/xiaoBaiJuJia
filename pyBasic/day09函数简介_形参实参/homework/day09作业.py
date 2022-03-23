# # 1. 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def element(l):
#     if type(l) == list or type(l) == tuple:
#         lis = [n for i, n in enumerate(l, 0) if i % 2 != 0]
#         return lis
#     else:
#         return "类型应为list或tuple"
#
# list1 = [1, 2, 3, 4, 5, 6]
# list1 = tuple(list1)
# print(element(l = list1))
# print(element("abk"))


# 2. 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def isLength(element):
#     if len(element) > 5:
#         print("长度大于5")
#     else:
#         print("长度小于5")
#
# isLength("abc")

# 3. 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def listLength(element):
#     if type(element) == list:
#         if len(element) > 2:
#             element =  element[:2]
#         return element
#     else:
#         return "数据类型不是list"
#
# lis = listLength([1, 2, 3])
# print(lis)

# 4. 写函数，计算传入函数的字符串中,[数字]、[字母] 以及 [其他]的个数，并返回结果。
# def countTypeNums(infos):
#     if type(infos) == str:
#         counts = {"count_int" : 0, "count_alp" : 0, "count_oth" : 0}
#         for i in infos:
#             if i.isdecimal():
#                 counts["count_int"] += 1
#             elif i.isalpha():
#                 counts["count_alp"] += 1
#             else:
#                 counts["count_oth"] += 1
#         return f"数字:{counts['count_int']}, 字母:{counts['count_alp']}, 其他:{counts['count_oth']}"
#     else:
#         return "请输入字符串"
#
# info = "123,ab."
# print(countTypeNums(info))


# 5. 写函数，接收两个数字参数，返回比较大的那个数字。
# def maxNum(num1, num2):
#     if (type(num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float):
#         return num1 if num1 > num2 else num2
#     else:
#         return "数据输入错误"
#
# print(maxNum(2, 1), maxNum(1, 2), maxNum(3.1, 3.25), maxNum(1, "3"))

# 6. 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#    dic = {"k1": "v1v1", "k2": [11,22,33,44]}
#    PS:字典中的value只能是字符串或列表
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# def new_dict(dicts):
#     if type(dicts) == dict:
#         for k,v in dicts.items():
#             if len(v) > 2:
#                 dicts[k] = v[:2]
#         return dicts
#     else:
#         return "数据类型不是dict"
#
# dic = new_dict(dic)
# print(dic)

# 7. 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，此字典的键
# 值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# def newDicts(infos):
#     if type(infos) == list:
#         dicts = {}
#         for i in range(len(infos)):
#             dicts.setdefault(i, infos[i])
#         return dicts
#     else:
#         return "数据类型非list"
#
# infos = ['a', 'b', 'c']
# infos = newDicts(infos)
# print(infos, type(infos))

# # 8. 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到
# # 函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
# def studentInfos():
#     name = input("Name:")
#     sex = input("Sex:")
#     age = input("Age:")
#     grade = input("Grade:")
#     return name, sex, age, grade
#
# def studentMsg():
#     infos = studentInfos()
#     with open(file="..//files//student_msg.txt", mode="a", encoding="utf-8") as w_f:
#         for i in infos:
#             w_f.write(f"{i}\n")
#         w_f.flush()
#         w_f.close()
#
# def main():
#     studentMsg()
#
# if __name__ == '__main__':
#     main()

# 9. 对第8题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。

# def studentMsg(sex = "男"):
#     infos = []
#     while 1:
#         name = input("Name:")
#         if name == "":
#             break
#         age = input("Age:")
#         qaq = input("Sex: 1.男， 2.女?")
#         if qaq == "2":
#             sex = "女"
#         grade = input("Grade:")
#         msg = {"Name":name, "Age":age, "Sex":sex, "Grade":grade}
#         infos.append(msg)
#
#     # 写入文件
#     with open(file="..//files//student_msg.txt", mode="a", encoding="utf-8") as a_f:
#         for dic in infos:
#             str = ""
#             for k, v in dic.items():
#                 str += k + ":" + v + ", "
#             str = str[:-2] + "\n"
#             a_f.write(str)
#
# def main():
#     studentMsg()
#
# if __name__ == '__main__':
#     main()

# 10. 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（**选做题**）。
def fileInfos():
    files = "..//files//" + input("文件名:")
    content1 = input("旧内容:")
    content2 = input("新内容:")

    return files, content1, content2

def updateFiles():
    try:
        import os
        infos = fileInfos()
        filename, info1, info2 = infos
        with open(file=filename, mode="r", encoding="utf-8") as r_f, open(file=filename+"1", mode="w", encoding="utf-8") as w_f:
            for line in r_f:
                line = line.replace(info1, info2)
                w_f.write(line)
        os.remove(filename)
        os.rename(filename+"1", filename)
    except FileNotFoundError:
        print("文件不存在")

def main():
    updateFiles()
if __name__ == '__main__':
    main()