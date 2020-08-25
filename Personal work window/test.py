import json
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys

class Test(QMainWindow):

    def __init__(self):
        super().__init__()
        self.iniUI()

    def iniUI(self):
        self.move(1100,0)
        self.setFixedSize(247, 725)
        self.button()
        self.show()

    def button(self):
        self.btko = QPushButton('显示知识库',self)


        self.btko.setGeometry(10, 30, 75, 23)

        self.open_knowledge()

        self.btko.clicked.connect(self.open_knowledge)


    def open_knowledge(self):
        """
        refer:btTarget:'当前目标'按键
        按当天情况输入当天目标核心
        :return:
        """
        with open('knowledge/interview_one.txt', 'r', encoding='UTF-8') as f:
            # 替换成""包裹的字符串，方便使用json
            content = f.read().replace("'", '"')
            # json.loads 将字符串文本转换 json数据结构（可字典or元组)
            # 注意一次加载字符串数量是有限的大概为300多
            long_list_data = json.loads(content)
            # 随机获取列表里一个小列表，[0]是为去括号，因为loads转换时会加一层括号
            short_list_data = random.choices(long_list_data)[0]
            # 使用choices生成的也是列表
            data = random.choices(short_list_data)[0]
            QMessageBox.about(self, '奖励窗口', data)

            # 对子序列操作是无法对原有文件产生作用,要直接对内容进行覆盖操作
            num = long_list_data.index(short_list_data)
            # 删子列表里数据
            short_list_data.remove(data)
            # 若无数据则转空
            if short_list_data == []:
                long_list_data.remove(num)
            # 若有数据则进行覆盖
            else:
                long_list_data[num] = short_list_data
            with open('knowledge/interview_one.txt', 'w', encoding='UTF-8') as f:
                # 重新写入内容
                f.write(str(long_list_data))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())


# 遇到问题：当删完列表后，空列表导致报错