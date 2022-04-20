from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averaged():
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
        results[key] = yield from averaged()


def main(datas):
    results = {}
    for key, values in datas.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2],
    'girls;m':
        [1.6, 1.5, 1.4, 1.3, 1.41]
}

if __name__ == "__main__":
    main(data)
