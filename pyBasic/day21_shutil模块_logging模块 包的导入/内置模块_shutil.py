''' 内置模块 shutil
'''

import shutil

# 拷贝文件
# shutil.copy2('原文件', '现文件')
# shutil.copy2('file', 'temp')

# 拷贝目录
# shutil.copytree("原目录", "新目录", ignore=shutil.ignore_patterns("*.pyc"))
# shutil.copytree("/Users/jingliyang/PycharmProjects/面试题/常用模块/logging模块", "logging模块2", ignore=shutil.ignore_patterns("__init__.py"))

# 删除目录
# shutil.rmtree("temp", ignore_errors=True)
# shutil.rmtree("logging模块2", ignore_errors=True)

# 移动文件/目录
# shutil.move("logging模块", "logging2", copy_function=shutil.copy2)

# 获取磁盘使用空间  1024 * 1024 *1024
# total, used, free = shutil.disk_usage(".")
# print("当前磁盘共: %iGB, 已使用: %iGB, 剩余: %iGB"%(total / 1073741824, used / 1073741824, free / 1073741824))
#
# 压缩文件
# shutil.make_archive('压缩文件夹的名字', 'zip','待压缩的文件夹路径')
# shutil.make_archive('logging2', 'zip','/Users/jingliyang/PycharmProjects/面试题/常用模块/随机数')

# 解压文件
# shutil.unpack_archive('zip文件的路径.zip'，'解压到目的文件夹路径')
# shutil.unpack_archive('/Users/jingliyang/PycharmProjects/面试题/常用模块/shutil模块/logging2.zip','/Users/jingliyang/PycharmProjects/面试题/常用模块/shutil模块/tmp')