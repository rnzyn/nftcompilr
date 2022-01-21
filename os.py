import os


def a(f):
    for i,o,p in os.walk(f):
        print("当前文件路径%s"%i)
        print("当前路径下所有子文件夹%s"%o)
        print("当前路径下所有文件%s"%p)
        pass
    pass

a("xxxxx")