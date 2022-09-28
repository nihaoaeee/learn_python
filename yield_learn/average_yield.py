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


def grouper(results, key):
    while True:
        results[key] = yield from averager1()


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    print(results)
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    "girls;kg": [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

if __name__ == "__main__":
    # coro_average = average_yield()
    # for i_ in range(5):
    #     res = coro_average.send(5 * i_)
    #     print(res)

    main(data)
