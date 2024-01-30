import random

a = [
    {
        "is_rare": 0,
        "max_times": 1,
        "min_times": 1,
        "id": "num_1",
        "prob": 10000
    },
    {
        "is_rare": 0,
        "max_times": 1,
        "min_times": 1,
        "id": "num_2",
        "prob": 10000
    },
    {
        "is_rare": 0,
        "max_times": 1,
        "min_times": 1,
        "id": "num_3",
        "prob": 10000
    },
    {
        "is_rare": 1,
        "max_times": 10,
        "min_times": 3,
        "id": "num_20",
        "prob": 2000
    },
    {
        "is_rare": 0,
        "max_times": 1,
        "min_times": 1,
        "id": "num_4",
        "prob": 10000
    },
    {
        "is_rare": 0,
        "max_times": 2,
        "min_times": 1,
        "id": "num_5",
        "prob": 8000
    },
    {
        "is_rare": 1,
        "max_times": 18,
        "min_times": 6,
        "id": "num_21",
        "prob": 1000
    },
    {
        "is_rare": 0,
        "max_times": 2,
        "min_times": 1,
        "id": "num_6",
        "prob": 8000
    },
    {
        "is_rare": 0,
        "max_times": 2,
        "min_times": 1,
        "id": "num_7",
        "prob": 8000
    },
    {
        "is_rare": 0,
        "max_times": 2,
        "min_times": 1,
        "id": "num_8",
        "prob": 8000
    },
    {
        "is_rare": 0,
        "max_times": 3,
        "min_times": 1,
        "id": "num_9",
        "prob": 6000
    },
    {
        "is_rare": 1,
        "max_times": 18,
        "min_times": 6,
        "id": "num_22",
        "prob": 1000
    },
    {
        "is_rare": 0,
        "max_times": 3,
        "min_times": 1,
        "id": "num_10",
        "prob": 6000
    },
    {
        "is_rare": 0,
        "max_times": 3,
        "min_times": 1,
        "id": "num_11",
        "prob": 6000
    },
    {
        "is_rare": 1,
        "max_times": 45,
        "min_times": 15,
        "id": "num_23",
        "prob": 400
    },
    {
        "is_rare": 0,
        "max_times": 3,
        "min_times": 1,
        "id": "num_12",
        "prob": 6000
    },
    {
        "is_rare": 0,
        "max_times": 5,
        "min_times": 1,
        "id": "num_13",
        "prob": 4000
    },
    {
        "is_rare": 0,
        "max_times": 5,
        "min_times": 1,
        "id": "num_14",
        "prob": 4000
    },
    {
        "is_rare": 0,
        "max_times": 5,
        "min_times": 1,
        "id": "num_15",
        "prob": 4000
    },
    {
        "is_rare": 0,
        "max_times": 5,
        "min_times": 1,
        "id": "num_16",
        "prob": 4000
    },
    {
        "is_rare": 0,
        "max_times": 10,
        "min_times": 3,
        "id": "num_17",
        "prob": 2000
    },
    {
        "is_rare": 1,
        "max_times": 45,
        "min_times": 15,
        "id": "num_24",
        "prob": 400
    },
    {
        "is_rare": 0,
        "max_times": 10,
        "min_times": 3,
        "id": "num_18",
        "prob": 2000
    },
    {
        "is_rare": 0,
        "max_times": 10,
        "min_times": 3,
        "id": "num_19",
        "prob": 2000
    },
    {
        "is_rare": 1,
        "max_times": 90,
        "min_times": 30,
        "id": "num_25",
        "prob": 200
    }
]


def get_normal_num(number_conf):
    """
    普通数字
    """
    normal_weight = 0
    for num_conf_ in number_conf:
        if not num_conf_["is_rare"]:
            normal_weight += num_conf_["prob"]
    normal_ch = random.randint(0, normal_weight)
    old_normal_ch = normal_ch
    for num_conf_ in number_conf:
        if not num_conf_["is_rare"]:
            if normal_ch < num_conf_["prob"]:
                return num_conf_
            else:
                normal_ch -= num_conf_["prob"]
    return None


if __name__ == "__main__":
    for _ in range(1000000000):
        if not get_normal_num(a):
            print("-----------------")
