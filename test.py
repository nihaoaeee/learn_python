# codind:utf-8
from ast import For
from encodings import utf_8
from importlib.machinery import FrozenImporter
import keyword
from multiprocessing.sharedctypes import Value
import random
from tkinter.messagebox import NO

print(keyword.kwlist)


a = 102
b = 11
print(a if a > b else b)
c = [1, 2, 3]


print(c)

list = [random.randint(10, 100) for _ in range(10000)]
print(list.count(100))

tpe = 1, 2, 3
print(tpe)
print(tuple([1, 2, 3, 4]))
print(tpe[0: 3: 2])

num = (i for i in range(10))
for i in num:
    print(i)

print(tuple(num))

myMap = {"1": 1, None: 1, "2": None}
print(myMap)

mySet = {1, 1}
print(mySet)

dict1 = dict(zip([1, 2, 3], [1, 2, 3]))

print(dict1)

print(dict.__len__(dict1))

for key, value in dict1.items():
    print(key, value)

set1 = set("李国祥李国祥".encode("utf_8").decode("utf_8"))
print(set1)


def func_name():
    '''
    aaaaaaaaaaaaaaaaaaaaaa
    '''
    print("aaaaaaaaaaaaaaaaaa")


func_name()
