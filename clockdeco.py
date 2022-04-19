from ast import arg
from cgitb import reset
import time

from coroutil.coroutil import coroutine


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs]%s(%s)->%r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        print('-------------------------')
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == "__main__":
    coro_avg = averager()
    # next(coro_avg)
    print(coro_avg.send(10))
    print(coro_avg.send(30))
