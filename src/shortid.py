import uuid
import string


def generate_short_id(length=17):
    # 生成一个UUID
    uuid_value = uuid.uuid4()

    # 将UUID转换为整数
    uuid_int = uuid_value.int

    # 定义字符集
    charset = string.digits + string.ascii_uppercase

    # 将整数转换为Base62字符串
    short_id = ""
    while uuid_int > 0:
        uuid_int, remainder = divmod(uuid_int, len(charset))
        short_id = charset[remainder] + short_id

    # 如果生成的ID长度不足，在前面补0
    short_id = short_id.zfill(length)

    # 返回指定长度的ID
    return short_id[:length]


print(generate_short_id())
