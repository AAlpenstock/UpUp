import json
import random


def test():
    with open('./knowledge/interview_one.txt', 'r', encoding='UTF-8') as f:
        # 替换成""包裹的字符串，方便使用json
        content = f.read().replace("'", '"')
        print(content)
        # json.loads 将字符串文本转换 json数据结构（可字典or元组)
        # 注意一次加载字符串数量是有限的大概为300多
        long_list_data = json.loads(content)
        # 随机获取列表里一个小列表，[0]是为去括号，因为loads转换时会加一层括号
        short_list_data = random.choices(long_list_data)[0]
        # 使用choices生成的也是列表
        data = random.choices(short_list_data)[0]
        print(data)

        # 对子序列操作是无法对原有文件产生作用,要直接对内容进行覆盖操作
        num = long_list_data.index(short_list_data)
        # 删子列表里数据
        short_list_data.remove(data)
        # 若无数据则转空
        if short_list_data == []:
            del long_list_data[num]
            if long_list_data == []:
                print('已经刷完')

        # 若有数据则进行覆盖
        else:
            long_list_data[num] = short_list_data
        with open('./knowledge/interview_one.txt', 'w', encoding='UTF-8') as f:
            # 重新写入内容
            f.write(str(long_list_data))


if __name__ == '__main__':
    while True:
        test()
