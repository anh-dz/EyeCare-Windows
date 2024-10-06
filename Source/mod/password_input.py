from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QRect, QSize, QMetaObject

class GET_PASS(QDialog):
    _pass_check_ = None
    def __init__(self, parent=None, change_pass="--Enter your Password--"):
        super().__init__(parent)
        self._show = False
        self.setFixedSize(537, 105)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(5, 5, 500, 61))
        self.label.setStyleSheet("font: 22pt \"Roboto\";color: rgb(56,56,56);")
        self.enter = QLineEdit(self)
        self.enter.setGeometry(QRect(5, 55, 471, 41))
        self.enter.setStyleSheet("font: 18pt \"Roboto\";border : 2px solid rgb(56,56,56);border-radius : 5;")
        self.show_hide = QPushButton(self)
        self.show_hide.setGeometry(QRect(480, 50, 54, 50))
        self.show_hide.setStyleSheet("border: 0px;")
        self.show_hide.setIcon(QIcon(QPixmap("qrc/hide.png")))
        self.show_hide.setIconSize(QSize(50, 50))
        self.show_hide.clicked.connect(self.change_icon)
        self.OkOk = QPushButton(self)
        self.OkOk.setGeometry(QRect(450, 10, 50, 30))
        self.OkOk.setStyleSheet("QPushButton{color:rgb(225,225,225);background-color:rgb(59,68,131);border:1px rgb(59,68,131);border-radius:10;font:14pt \"Roboto Medium\"}QPushButton:hover{border:1px rgb(59,100,131);background-color:rgb(59,100,131)}")
        self.OkOk.clicked.connect(self.okela)
        self.enter.setPlaceholderText("Enter your Password")
        self.enter.setEchoMode(QLineEdit.EchoMode.Password)
        self.enter.returnPressed.connect(self.OkOk.click)

        QMetaObject.connectSlotsByName(self)
        self.setWindowTitle("EyeCare")

        self.label.setText(change_pass)
        self.OkOk.setText("Okay")
    def change_icon(self):
        if self._show:
            self.show_hide.setIcon(QIcon(QPixmap("qrc/hide.png")))   
            self.enter.setEchoMode(QLineEdit.EchoMode.Password)
            self._show = False
        else:
            self.show_hide.setIcon(QIcon(QPixmap("qrc/show.png")))   
            self.enter.setEchoMode(QLineEdit.EchoMode.Normal)
            self._show = True
    def okela(self):
        self._pass_check_ = self.enter.text()
        self.close()

class GET_WORD(QDialog):
    _word_check_ = None
    def __init__(self, parent=None, text_set=None):
        super().__init__(parent)
        self.setWindowTitle("EyeCare")
        self.setFixedSize(543, 105)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(5, 5, 241, 61))
        self.label.setStyleSheet("font: 22pt \"Roboto\";color: rgb(56,56,56);")
        self.word_get = QLineEdit(self)
        self.word_get.setGeometry(QRect(5, 55, 471, 41))
        self.word_get.setStyleSheet("font: 18pt \"Roboto\";border : 2px solid rgb(56,56,56);border-radius : 5;")
        self.word_get.setMaxLength(500)
        self.OkOk = QPushButton(self)
        self.OkOk.setGeometry(QRect(480, 60, 50, 30))
        self.OkOk.setStyleSheet("QPushButton{color:rgb(225,225,225);background-color:rgb(59,68,131);border:1px rgb(59,68,131);border-radius:10;font:14pt \"Roboto Medium\"}QPushButton:hover{border:1px rgb(59,100,131);background-color:rgb(59,100,131)}")
        self.OkOk.clicked.connect(self.okela)

        self.word_get.setEchoMode(QLineEdit.EchoMode.Normal)
        self.word_get.returnPressed.connect(self.OkOk.click)

        QMetaObject.connectSlotsByName(self)
        self.label.setText("--Enter Text--")
        self.word_get.setPlaceholderText(text_set)
        self.OkOk.setText("Okay")
    def okela(self):
        self._word_check_ = self.word_get.text()
        self.close()