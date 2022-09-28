# coding=utf-8
from collections import namedtuple

from coroutil.coroutil import coroutine


@coroutine
def average_yield():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        count += 1
        total += term
        average = total / count


Result = namedtuple('Result', 'count average')


def averager1():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count

    return Result(count, average)


if __name__ == "__main__":
    coro_average = average_yield()
    for i_ in range(5):
        res = coro_average.send(5 * i_)
        print(res)
