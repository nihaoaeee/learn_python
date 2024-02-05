import g1
from g1 import a


def print_info():
    g1.get_a = get_a
    g1.load_a = load_a
    print("g1", g1.get_a())
    print("t1", g1.a)
    g1.print_info()


def load_a():
    global a
    g1.a = 1000
    print("----------------------")


def get_a():
    if not g1.a:
        load_a()
    return g1.a


if __name__ == "__main__":
    print_info()
