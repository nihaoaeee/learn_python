registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def main():
    print('running main()')
    print('registry -> ', registry)
    f1()
    f2()


if __name__ == "__main__":
    main()
