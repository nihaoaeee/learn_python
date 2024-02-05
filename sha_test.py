def format_id_card(id_card):
    # 去除无效字符
    cleaned_id_card = id_card.replace("\xe2\x85\xa9", "")
    cleaned_id_card = cleaned_id_card.replace("\x85", "")

    # 检查长度
    if len(cleaned_id_card) != 18:
        return "无效的身份证格式"

    # 检查是否为数字
    if not cleaned_id_card[:-1].isdigit() or (
            cleaned_id_card[-1] != 'X' and cleaned_id_card[-1] != 'x' and not cleaned_id_card[-1].isdigit()):
        return "无效的身份证格式"

    return cleaned_id_card


id_card = "64222119871020341\xe2\x85\xa9"
formatted_id_card = format_id_card(id_card)
print(formatted_id_card)
import re


def check_id_card(id_card):
    pattern = r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|3[0-1])\d{3}([0-9Xx])$'
    match = re.match(pattern, id_card)
    return match is not None


# 测试示例
id_card1 = '51012319800101001X'
id_card2 = '32012319800101235'
id_card3 = '123456789012345678'
print(check_id_card(id_card1))  # 输出：True
print(check_id_card(id_card2))  # 输出：False
print(check_id_card(id_card3))  # 输出：False
