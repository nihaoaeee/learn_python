import multiprocessing
import time
from multiprocessing import Pool, current_process, Value
from tqdm import tqdm


def worker(n_i):
    # n, index_ = n_i
    # 获取当前子进程的名字
    process_name = current_process().name
    # 创建子进程本地的tqdm对象
    # for _ in range(2000000):
    #     print(index_.value)
    #     index_.value += 1
    # return n
    return 0


def worker_tqdm(fire_times, index_):
    from tqdm import tqdm
    import time
    while True:
        pbar = tqdm(total=fire_times)
        num = index_.value
        print(num)
        pbar.n = num  # 设置当前值为50
        pbar.refresh()  # 更新显示
        time.sleep(1)  # 暂停一下，让效果更明显
        if num >= fire_times:
            break


def main():
    pool = Pool(processes=4)  # 创建一个4进程的进程池

    # 各子进程需要完成的任务数
    index_ = Value("i", 0)
    tasks = [[40, index_], [20, index_], [30, index_], [40, index_]]
    p = multiprocessing.Process(target=worker_tqdm, args=(8000000, index_))
    p.start()
    # map方法会阻塞主进程，直到所有子进程完成任务
    pool.map(worker, tasks)
    # for _ in range(10000):
    #     index_.value += 1
    #     print(index_.value)
    p.join()

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
