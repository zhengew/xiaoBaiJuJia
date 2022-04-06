lst = [('test1', 'python'), ('test1', 'python'),('test2', 'python'), ('test2', 'java'),]
dic1 = {}
for i in range(len(lst)):
    # print(lst[i])
    name, value = lst[i]
    dic1.setdefault(name, set())

for key, value in lst:
    dic1[key].add(value)
print(dic1)

for k, v in dic1.items():
    print(k, v)
