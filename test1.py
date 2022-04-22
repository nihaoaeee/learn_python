import time

import testdescriptot
import os


def demo(obj=None):
    if obj == None:
        obj = []
    print(obj)
    obj.append(1)


def testfile():
    file = open("test.txt", "r+")
    print(file)
    file.write("1234567890qwertyuiopasdfghjklzxcvbnm")
    file.seek(19)
    print(file.read(13))


# class Test:

if __name__ == "__main__":
    # try:
    #     testfile()
    #     print(1)
    #     print(os.name)
    #     print(os.linesep)
    #     print(os.sep)
    #     print(os.getcwd())
    #     assert 1 == 2, "1!=2"
    # except AssertionError as e:
    #     print(e)

    from tqdm import tqdm

    for i in tqdm(range(1000)):
        time.sleep(0.001)
