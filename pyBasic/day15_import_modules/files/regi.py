'''
测试在其他路径下导入模块
'''
def reg(infos):
    print(infos)
    print(__name__)

def login():
    print("login")

def main():

    reg("zew")


if __name__ == '__main__':
    main()