# f = open("test.txt", mode="r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()

with open("test.txt", mode="r", encoding="utf-8") as f:
    # msg = f.readline()
    # print(msg.strip("\n"))
    #
    # msgs = f.readlines()
    # print(msgs)

    for line in f:
        print(line.strip())