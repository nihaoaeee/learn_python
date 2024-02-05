from ast import arg
from cgitb import reset
import time
from collections import namedtuple

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


Result = namedtuple('Result', 'count average')


@coroutine
def averagterd():
    total = 0.0
    count = 0
    average = None
    while True:
        print('-------------------------')
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


class DemoException(Exception):
    ''''''


@coroutine
def demo_exc_handing():
    print('-> coroutine stared')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('->coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')


if __name__ == "__main__":
    coro_avg = averagterd()
    # next(coro_avg)
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    try:
        coro_avg.send(None)
    except StopIteration as e:
        print(e)
    print('-------')
    # print(coro_avg.send(None))
    #
    # demo = demo_exc_handing()
    # demo.send(10)
    # demo.close()
