# 7. 有如下数据类型(实战题)：
#
l1 = [ {'sales_volumn': 0},
    {'sales_volumn': 108},
    {'sales_volumn': 337},
    {'sales_volumn': 475},
    {'sales_volumn': 396},
    {'sales_volumn': 172},
    {'sales_volumn': 9},
    {'sales_volumn': 58},
    {'sales_volumn': 272},
    {'sales_volumn': 456},
    {'sales_volumn': 440},
    {'sales_volumn': 239},
]

# 将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
# 不会了 ...


# 13.求结果：（面试题，比较难，先做其他题）
def num():
    return [lambda x:i*x for i in range(4)]

print([m(2)for m in num()])