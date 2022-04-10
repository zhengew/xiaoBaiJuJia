lst = [('上传', 'uploads'),('下载','downloads')]
for i in enumerate(lst, 1):
    print(i[0], i[1][0])


dic = {'tmp.txt':800}
import json

with open('../db/dic.txt', mode='w', encoding='utf-8') as f:
    json.dump(dic,f)


with open('../db/dic.txt', mode='r', encoding='utf-8') as f:
    for i in f:
        dic = json.loads(i)

print(dic)
