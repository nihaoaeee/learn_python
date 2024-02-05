from concurrent import futures
from flags import get_flag, main, show, save_flag

MAX_WORKERS = 20


def download_on(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many1(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_on, sorted(cc_list))
    return len(list(res))


def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_on, cc)
            to_do.append(future)
            msg = 'Scheduled for {}:{}'
            print(msg.format(cc, future))
        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    return len(res)


if __name__ == "__main__":
    main(download_many)
