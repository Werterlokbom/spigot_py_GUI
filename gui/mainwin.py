import typing
import PyQt5
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle('测试')
    
    def start_win(self):
        form = MainWindow()
        form.show()
        sys.exit(app.exec_())
