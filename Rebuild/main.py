from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from Viewer.mainui import *
from Control.maincontrol import *
import sys

class ViewControl(Ui_MainWindow):
    def __init__(self):
        super().__init__()

class MainApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowIcon(QIcon('logo.ico'))

def main():
    app = QApplication(sys.argv)
    mainwindows = MainApp()

    widgets = ViewControl()
    widgets.setupUi(mainwindows)

    model_obj = Control(widgets)
    mainwindows.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
