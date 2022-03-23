''' 文件读常用方法 '''
'''
read()
read(n) 在 r模式下，n是按照字符读取
readline()
readlines() 返回一个列表
for循环遍历文件句柄
'''

''' 第一版 几乎不用 '''

# f = open(file=".//files//test.txt", mode="r", encoding="utf-8") # f 文件句柄 open() 调用操作系统的功能
# contents = f.read() # 对文件的读写操作都需要通过文件句柄
# print(contents)
# f.close() # 关闭文件句柄

''' 第二版 with 语句，默认执行 f.close() 关闭文件句柄 '''

# with open(file=".//files//test.txt", mode="r", encoding="utf-8") as f:
    # 1.read() 读取全部内容，内存消耗大
    # print(f.read())

    # 2.read(n) # 在 r模式下，n是按字符读取
    # print(f.read(1))

    # 3.readline() 每次读取一行，每行末尾都有个换行符
    # print(f.readline().strip())

    # 4.readlines() 返回一个列表，列表里的每一个元素是源文件的每一行
    # print(f.readlines())

    # 5.for循环遍历文件句柄,文件句柄是一个迭代器，每次循环只在内存中占用一行数据，节省内存开销
    # for line in f:
    #     print(line, end="")

''' 
rb模式: 以二进制格式打开文件。文件指针将会放在文件的开头，
主要用来操作非文本文件，例如 图片/视频/音频等，
带有b的模式操作文件，不用声明编码方式

rb模式也支持: read() read(n) readline() readlines() for循环遍历
'''

# with open(file=".//files//bdd.jpg", mode="rb") as f:
#     # print(f.read())
#     for line in f:
#         print(line)

''' 文件的写操作 '''

'''
文件写操作主要有四种模式： 
w 模式:如果文件不存在，w模式会先创建文件，然后再写入文件；如果文件存在，会先清空文件，再写入内容
wb 模式:以二进制格式打开文件，只用来写入文件；
如果文件已存在，则打开文件，并从开头开始编辑，及原有内容会被清空；
如果文件不存在，则创建新文件。
w+
w+b
'''

# with open(file=".//files//write.txt", mode="w", encoding="utf-8") as f:
#     f.write("w 模式:如果文件不存在，w模式会先创建文件，然后再写入文件")
#     f.flush() # 强制表村

''' wb 模式'''
# 练习题：复制 .//files//bdd.jpg，复制的文件名为bdd2.jpg
# 注意 with 语句虽然默认会关闭文件句柄，但是有时间开销，如果存在并发写入的情况，建议手动关闭文件句柄
# with open(file=".//files//bdd.jpg", mode="rb") as read_f, open(file=".//files//bdd2.jpg", mode="wb") as write_f:
#     bdd_bytes = read_f.read()
#     read_f.close()
#
#     write_f.write(bdd_bytes)
#     write_f.close()

''' 文件操作:追加
文件追加操作也有四种模式:
a 模式: 如果文件存在，则在文件末尾追加文件; 如果文件不存在，则先创建文件再写入
ab 模式
a+ 模式
a+b 模式
'''
# with open(file=".//files//test.txt", mode="a", encoding="utf-8") as f:
#     f.write("\na 追加模式，如果文件存在，则在文件末尾追加内容；如果文件不存在，则创建文件后写入")


''' 文件操作的其他模式 
r+ 读写
w+ 写读
a+ 写读

bytes类型操作的读写,写读
r+b 读写
w+b 写读
a+b 写读

注意：在读写模式下，如果先写后读，会覆盖原内容，因为光标在文件开始位置
'''
# with open(file=".//files//test.txt", mode="r+", encoding="utf-8") as f:
#     contents = f.read()
#     print(contents)
#
#     f.write("\nr+模式，文件需要先读取再写入，否则会覆盖源文件内容")

''' 
文件操作的其他功能：

1. read(n): 如果是文本模式，例如 r/r+等等，代表读取n个字符；如果是b模式，例如rb,代表读取n个字节

2. seek(n): 光标移动到n位置，移动单位是byte，如果是utf-8，中文要移动3个字节
seek(0) 移动到开头
seek(0, 2) ，默认0表示开头，2表示结尾，seek(0, 2) 即 把光标从开头移动到结尾

3. tell() 获取当前光标的所在位置

4. readable() / writeable() 判断文件是否可读/可写
'''

'''
文件的修改：

方式一：将文件全部读取到内容中，f.read(),然后批量修改

方式二：通过for循环遍历文件句柄，逐行修改再逐行写入，最后删除原文件，将新文件命名为源文件名
'''
# 方式一
# with open(file=".//files//test.txt", mode="r+", encoding="utf-8") as f:
#     contents = f.read()
#     contents = contents.replace("zew", "erwei.zheng")
#
#     f.write(contents)

import os

with open(file=".//files//test.txt", mode="r", encoding="utf-8") as read_f, open(file=".//files//test1.txt", mode="w", encoding="utf-8") as write_f:
    for line in read_f:
        line = line.replace("erwei.zheng", "zew")
        write_f.write(line)

os.remove(".//files//test.txt")
os.rename(".//files//test1.txt", ".//files//test.txt")



