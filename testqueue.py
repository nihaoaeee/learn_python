# -*-coding:utf-8-*-
from email import message
from importlib.machinery import FrozenImporter
from multiprocessing import Process, Queue
import time
from traceback import print_tb


def write_task(q):
    i = 0
    while True:
        if not q.full():
            i += 1
            message = "msg: " + str(i)
            time.sleep(0.1)
            q.put(message)
            print("message%s" % message)


def read_task(q):
    while True:
        if not q.empty():
            time.sleep(0.1)
            print("read: %s" % q.get())


if __name__ == "__main__":
    q = Queue(1000)
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()


