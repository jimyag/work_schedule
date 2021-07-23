from scripts.schedule import Schedule
import sys
from PyQt5.QtWidgets import QDialog, QFileDialog, QApplication

if __name__ == '__main__':
    q_app = QApplication(sys.argv)
    schedule = Schedule()
    schedule.show()
    sys.exit(q_app.exec_())
