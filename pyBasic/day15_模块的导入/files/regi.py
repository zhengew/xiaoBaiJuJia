'''
测试在其他路径下导入模块
'''
import os
def reg(infos):
    with open(file=os.path.dirname(__file__)+ r"/test.txt", mode="a", encoding="utf-8") as write_f:
        write_f.seek(0,2)
        write_f.write(infos + "\n")
        write_f.flush()
        write_f.close()

def main():
    reg("zew")

if __name__ == '__main__':
    main()