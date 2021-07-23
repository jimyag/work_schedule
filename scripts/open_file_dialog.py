from scripts.open_file import OpenFile
from PyQt5.QtWidgets import QDialog, QFileDialog
import os


class OpenFileDialog(QDialog):
    """
    打开文件对话框
    """

    def __init__(self):
        super(OpenFileDialog, self).__init__()
        self.file_name = None
        self.ui = OpenFile()
        self.ui.setupUi(self)
        self.ui.open_file.clicked.connect(self.open_file_clicked)
        self.cwd = os.getcwd()

    def open_file_clicked(self):
        """
        点击按键之后打开文件
        """
        self.file_name, _ = QFileDialog.getOpenFileName(self, '选择课程表', self.cwd)
        print(self.file_name)
        self.setHidden(True)

    def hidden(self):
        if self.file_name is not None:
            self.setHidden(True)

    def closeEvent(self, event):
        """
        :param event:
        :return:
        """
        print("关闭")
        event.accept()
