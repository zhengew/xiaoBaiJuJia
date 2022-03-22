''' int bool str 之间的转换 '''

'''
int -> bool 非0即True
bool -> int True 1, False 0

int -> str  str()
str -> int  int()  必须全部由数字组成的字符串才能转换成int

str -> bool 非空即True
bool -> str  str(True) -> "True"
'''

''' str  list 之间的转换 '''
# str -> list
# str1 = "a b d"
# list1 = str1.split(" ")
# print(list1) # ['a', 'b', 'd']

# list -> str
# list2 = ['a', 'b', 'd']
# str2 = " ".join(list2)
# print(str2)

# 或者用循环
# str3 = ""
# for i in list2:
#     str3 += i + " "
# str3 = str3[:-1]
# print(str3)

''' list set 之间的转换 '''

# list -> set
list1 = [1, 2, 3]
set1 = set(list1)
print(set1, type(set1))

# set - > list
set2 = {1, 2, 3}
list2 = list(set2)
print(list2, type(list2))

''' str bytes 之间的转换 '''
# encode decode

# str - > bytes
str = "China中国"
byte_str = str.encode(encoding="utf-8")
print(byte_str) # b'China\xe4\xb8\xad\xe5\x9b\xbd'

# bytes -> str
str_byte = b'China\xe4\xb8\xad\xe5\x9b\xbd'
str = str_byte.decode(encoding="utf-8")
print(str)

''' 所有数据都可以转换为bool '''
# "", 0, (), {}, set(), [], None - > 转化成的布尔值都是False




