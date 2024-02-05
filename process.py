from multiprocessing import Process, Pool


def test(count):
    print("子进程： ", count)


def main():
    print("main ")
    p = Process(target=test, args=(1,))
    p.start()
    print("main end")


if __name__ == "__main__":
    main()
