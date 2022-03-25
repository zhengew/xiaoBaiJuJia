# 17看代码求结果：（面试题）
def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g=test() # 生成器 每次取值 0 1 2 3

for n in [1,10]:
    g=(add(n,i) for i in g)
print(list(g))
'''
[20, 21, 22, 23]  这道题现在看不懂
'''