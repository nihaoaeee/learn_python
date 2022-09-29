# coding=utf-8


from coroutil.coroutil import coroutine


@coroutine
def average_yield():
    total = 0.0
    count = 0
    average = None
    while True:
        trem = yield average
        count += 1
        total += trem
        average = total / count

coro_average = average_yield()
next(coro_average)
for i_ in range(5):
    res = coro_average.send(5*i_)
    print(res)

