"""
转以空格为分隔符的字符串为两层列表嵌套
"""
import re


def change_str():
    with open('./str_origin.txt','r',encoding='UTF-8') as fp:
        str_1 = fp.read()
        str_1 = re.split('\n',str_1)
        # for i in range(len(str_1)):
        #     str_1[i] = [str_1]
        print(str_1)
    return str_1


if __name__ == '__main__':
    change_str()


