# coding=utf-8


def simple_coroutine():
    print("-> coroutine start")
    x = yield
    print("-> coroutine receive ", x)

my_corou = simple_coroutine()
print(my_corou)
next(my_corou)
my_corou.send(42)

