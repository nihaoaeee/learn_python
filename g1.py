import random

a = ["a"]

b = {"a:b": 1, "b": 2}

a.extend(b)
aa = {"a": 1}


def funca(aa=None):
    pass


def funcb():
    for i_ in range(
        1,
        111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
    ):
        if i_ % 2 == 1:
            funca()
        else:
            funca(aa=aa)


class Test1(object):
    pass


if __name__ == "__main__":
    a = ["a", "b", "c"]

    for index_, ele in enumerate(a):
        print(ele)
    if index_ == 1:
        print(a)
