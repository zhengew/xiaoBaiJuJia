# 先进后出队列 栈
# from queue import LifoQueue, Empty
#
# q = LifoQueue()
#
# for i in range(4):
#     q.put(i)
#
# for i in range(5):
#     try:
#         print(q.get_nowait())
#     except Empty:
#         print('栈队列为空')

# 解决三级菜单
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
l = [menu]

while l:
    for key in l[-1]:print(key)
    k = input('input>>').strip()   # 北京
    if k in l[-1].keys() and l[-1][k]:
        l.append(l[-1][k])
    elif k == 'b':l.pop()
    elif k == 'q':break