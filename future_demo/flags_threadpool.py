from concurrent import futures
from flags import get_flag, main, show, save_flag

MAX_WORKERS = 20


def download_on(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_on, sorted(cc_list))
    return len(list(res))


if __name__ == "__main__":
    main(download_many)
