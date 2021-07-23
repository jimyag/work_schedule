import copy
import pandas as pd
from scripts.table import Table
from PyQt5.QtWidgets import QMainWindow, QComboBox, QFileDialog
from scripts.open_file_dialog import OpenFileDialog
from scripts.parse import get_free_time_names, free_time_student
import os

_key_map = {1: '周一',
            2: '周二',
            3: '周三',
            4: '周四',
            5: '周五'}

table_data = {'次序': ['第1、2节课', '第3、4节课', '第5、6节课', '第7、8节课'], '周一': [], '周二': [], '周三': [], '周四': [], '周五': []}


class Schedule(QMainWindow):
    def __init__(self):
        super(Schedule, self).__init__()
        self.free_time_names = []
        self.table_data = copy.deepcopy(table_data)
        self.ui = Table()
        self.ui.setupUi(self)
        self.ui.input.clicked.connect(self.input_clicked)
        self.ui.output.clicked.connect(self.output_clicked)
        self._result_file_name = 'result.xls'
        self.students = {}

    def bind_combo_box(self):
        for col in range(5):
            for row in range(4):
                box = QComboBox()
                box.addItems(self.free_time_names[col * 4 + row])
                box.setStyleSheet("QComboBox{margin:3px};")
                self.ui.tableWidget.setCellWidget(row, col, box)
        pass

    def input_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(self, '选择文件', os.getcwd())
        print(file_name)
        data_frame: pd.DataFrame = pd.read_excel(file_name, sheet_name='Sheet1')

        data = data_frame.values.tolist()
        for i in data:
            value = list(i[1:])
            self.students[i[0]] = value

        get_free_time_names(self.students, self.free_time_names)
        self.bind_combo_box()
        pass

    def output_clicked(self):
        for col in range(5):
            for row in range(4):
                self.table_data[_key_map[col + 1]].append(self.ui.tableWidget.cellWidget(row, col).currentText())
        data_frame: pd.DataFrame = pd.DataFrame(self.table_data)
        data_frame.to_excel(self._result_file_name, index=False)
