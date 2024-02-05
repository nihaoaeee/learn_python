class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]

    def __contains__(self, item):
        pass


if __name__ == "__main__":
    foo = Foo()
    print(foo[1])
    for i in foo:
        print(i)
    print(0 in foo)
