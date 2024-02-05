import random

# 生成乱序列表
nums = list(range(1, 19))
random.shuffle(nums)

# 初始化结果列表
result = []

# 循环30次
while len(result) < 30:
    # 生成一个不重复的值
    num = random.choice(nums)

    # 如果结果列表长度小于5，直接添加到结果列表
    if len(result) < 5:
        result.append(num)
    else:
        # 如果当前值与前面连续五个值都不重复，添加到结果列表
        if num not in result[-5:]:
            result.append(num)


# 输出结果列表
print(result)
