''' random 模块常用方法

1. random.random() : 获取 [0.0, 1.0) 范围内的浮点数
2. random.randint(a, b): 获取[a, b] 范围内的一个整数
3. random.uniform(a, b): 获取[a, b) 范围内的浮点数
4. random.shuffle(x): 把参数指定的数据中的元素打乱。参数必须是一个可变的数据类型。
5. random.sample(x, k): 从x中随机抽取k个数据，组成一个列表返回
'''

import random

def main():
    # 获取 [0.0, 1.0) 范围内的浮点数,伪随机数
    print(random.random())

    # 获取[a, b) 范围内的浮点数
    print(random.uniform(3, 5))

    # 获取[a, b] 范围内的一个整数
    print(random.randint(1, 10))

    # 把参数指定的数据中的元素打乱。参数必须是一个可变的数据类型。
    lis = [i for i in range(10)]
    print(lis)
    random.shuffle(lis)
    print(lis)

    # 从x中随机抽取k个数据，组成一个列表返回
    # 可通过 sample变相打乱 元组
    tul = (1, 2, 3, 4)
    lis = random.sample(tul, len(tul))
    print(lis)
    tul = tuple(lis)
    print(tul)


if __name__ == '__main__':
    main()