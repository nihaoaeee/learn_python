# coding=utf-8

def simple_coroutine2(a):
    print("-> Start a = ", a)
    b = yield a
    print("-> Received b = ", b)
    c = yield a + b
    print("-> Received c = ", c)

my_corou = simple_coroutine2(14)
from inspect import getgeneratorstate
print(getgeneratorstate(my_corou))
next(my_corou)

print(getgeneratorstate(my_corou))
my_corou.send(28)
my_corou.send(99)

