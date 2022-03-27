# 1.写函数，让用户输入用户名密码，将密码转化成密文，然后构建一个字典，字典的键为用户名，
# 值为其对应的密码，将这个字典以json字符串的形式写入文件中。
import os
import time


def register(username, password):
    import os
    import json
    import hashlib
    tellers = {}
    m = hashlib.md5()
    m.update(fr"{password}".encode("utf-8"))
    pwd = m.hexdigest()
    tellers.setdefault(username, pwd)
    with open(file=os.path.join(os.path.dirname(os.path.dirname(__file__)),"files/users.txt"), mode="at", encoding="utf-8") as f:
        f.seek(0,2)
        f.write(json.dumps(tellers))
        f.write("\n")
        f.flush()
        f.close()


#
# def main():
#     # register('test1', 123456)
#
# if __name__ == '__main__':
#     main()

#
# 2.利用递归寻找文件夹中所有的文件，并将这些文件的绝对路径添加到一个列表中返回（面试题，有点难，可先做其他）。
'''
# l = []
# def dirfind(path):
#     import os
#     lst = os.listdir(path)
#     for dir_path in lst:
#         if os.path.isdir(os.path.join(path, dir_path)):
#             dirfind(os.path.join(path, dir_path))
#         elif os.path.isfile(os.path.join(path, dir_path)):
#             l.append(os.path.join(path, dir_path))
#     return l
#
#
# print(dirfind(r'E:\studyP\bolg'))
'''

def findAllFiles(path):
    import os
    files = [] # 保存当前目录及子目录下的所有文件
    currDir = os.listdir(path)
    for dir in currDir:
        if os.path.isdir(os.path.join(path, dir)):
            findAllFiles(os.path.join(path, dir))
        elif os.path.isfile(os.path.join(path,dir)):
            files.append(os.path.join(path,dir))
    return files

files = findAllFiles(os.path.dirname(os.path.dirname(__file__)))
for i in files:
    print(i)

#
# 3.写函数：用户输入某年某月，判断这是这一年的第几天（需要用Python的结构化时间）。
#
# 结构化时间可以通过这样取值：
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# print(time.strptime("2022-03-27 19:27:30", "%Y-%m-%d %H:%M:%S" ))
# time = time.strptime("2022-03-27 19:27:30", "%Y-%m-%d %H:%M:%S")
# print(time.tm_year, time.tm_yday)

# def daysFroYear():
#     import time
#     try:
#         dates = input("请输入年月日: 例如 2022/3/27 ").strip().replace(" ", "").split("/")
#         time = time.strptime(f"{dates[0]}-{dates[1]}-{dates[2]}", "%Y-%m-%d")
#         print(time.tm_year, time.tm_yday)
#     except Exception:
#         print("数据异常!")
#
# daysFroYear()



# 4.写函数，生成一个4位随机验证码（包含数字大小写字母）。

# def randomCode ():
#     import random
#     l1 = [chr(i) for i in range(97, 123)]
#     l2 = [chr(i) for i in range(97, 123)]
#     l3 = [str(i) for i in range(0, 9)]
#     l4 = [*l1, *l2, *l3]
#     return random.sample(l4,3) + random.sample(l3, 1)
# def main():
#     code = randomCode()
#     print(code)
# if __name__ == '__main__':
#     main()