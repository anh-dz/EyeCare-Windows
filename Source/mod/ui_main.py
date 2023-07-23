from PyQt6.QtCore import QRect, QSize, QMetaObject
from PyQt6.QtGui import QFontDatabase, QIcon, QPixmap, QFont, QIntValidator
from PyQt6.QtWidgets import QComboBox, QFrame, QStackedWidget, QWidget, QLabel, QLineEdit, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QGridLayout, QVBoxLayout, QCheckBox, QTextBrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(710, 380)
        font = QFontDatabase
        font.addApplicationFont("font/Roboto-Regular.ttf")
        font.addApplicationFont("font/Roboto-Light.ttf")
        font.addApplicationFont("font/Roboto-Medium.ttf")
        font.addApplicationFont("font/Social Media Circled.otf")
        MainWindow.setWindowIcon(QIcon('logo.ico'))
        MainWindow.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.Page_Stack = QStackedWidget(MainWindow)
        self.Page_Stack.setGeometry(QRect(140, 0, 571, 411))
        self.page_0 = QWidget()
        self.work = QLabel(self.page_0)
        self.work.setGeometry(QRect(80, 90, 160, 61))
        self.work.setStyleSheet("font: 30pt \"Roboto\"")
        self.relax = QLabel(self.page_0)
        self.relax.setGeometry(QRect(160, 160, 90, 61))
        self.relax.setStyleSheet("font: 30pt \"Roboto\";")
        self.work_h = QLineEdit(self.page_0)
        self.work_h.setGeometry(QRect(270, 100, 51, 43))
        self.work_h.setStyleSheet("font: 30pt \"Roboto\";border:0px")
        self.work_m = QLineEdit(self.page_0)
        self.work_m.setGeometry(QRect(350, 100, 51, 43))
        self.work_m.setStyleSheet("font: 30pt \"Roboto\";border:0px")
        self.work_s = QLineEdit(self.page_0)
        self.work_s.setGeometry(QRect(430, 100, 51, 43))
        self.work_s.setStyleSheet("font: 30pt \"Roboto\";border:0px")
        self.non_1 = QLabel(self.page_0)
        self.non_1.setGeometry(QRect(330, 100, 16, 41))
        self.non_1.setStyleSheet("font: 30pt \"Roboto\"")
        self.non_2 = QLabel(self.page_0)
        self.non_2.setGeometry(QRect(410, 100, 16, 41))
        self.non_2.setStyleSheet("font: 30pt \"Roboto\"")
        self.non_3 = QLabel(self.page_0)
        self.non_3.setGeometry(QRect(330, 170, 16, 41))
        self.non_3.setStyleSheet("font: 30pt \"Roboto\"")
        self.relax_h = QLineEdit(self.page_0)
        self.relax_h.setGeometry(QRect(270, 170, 51, 43))
        self.relax_h.setStyleSheet("font: 30pt \"Roboto\";border:0px")
        self.relax_m = QLineEdit(self.page_0)
        self.relax_m.setGeometry(QRect(350, 170, 51, 43))
        self.relax_m.setStyleSheet("font: 30pt \"Roboto\";border:0px")
        self.relax_s = QLineEdit(self.page_0)
        self.relax_s.setGeometry(QRect(430, 170, 51, 43))
        self.relax_s.setStyleSheet("font: 30pt \"Roboto\";border:0px")
        self.non_4 = QLabel(self.page_0)
        self.non_4.setGeometry(QRect(410, 170, 16, 41))
        self.non_4.setStyleSheet("font: 30pt \"Roboto\"")
        self.horizontalLayoutWidget = QWidget(self.page_0)
        self.horizontalLayoutWidget.setGeometry(QRect(170, 240, 171, 71))
        self.start_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.start_layout.setContentsMargins(0, 0, 0, 0)
        self.button_pause = QPushButton(self.horizontalLayoutWidget)
        self.button_pause.setStyleSheet("border: 0px")
        self.button_pause.setText("")
        self.button_pause.setIcon(QIcon(QPixmap("qrc/pause.png")))
        self.button_pause.setIconSize(QSize(50, 50))
        self.button_pause.setVisible(False)
        self.start_layout.addWidget(self.button_pause)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.start_layout.addItem(spacerItem)
        self.start = QPushButton(self.horizontalLayoutWidget)
        self.start.setStyleSheet("border: 0px;")
        self.start.setText("")
        self.start.setIcon(QIcon(QPixmap("qrc/start.png")))
        self.start.setIconSize(QSize(50, 50))
        self.start_layout.addWidget(self.start)
        self.edit = QPushButton(self.page_0)
        self.edit.setGeometry(QRect(470, 20, 54, 50))
        self.edit.setStyleSheet("border: 0px;")
        self.edit.setText("")
        self.edit.setIcon(QIcon(QPixmap("qrc/draw_lock.png")))
        self.edit.setIconSize(QSize(50, 50))
        self.time_left = QLabel(self.page_0)
        self.time_left.setGeometry(QRect(420, 340, 131, 31))
        self.time_left.setStyleSheet("font: 16pt \"Roboto Medium\"")
        self.lock_screen = QPushButton(self.page_0)
        self.lock_screen.setGeometry(QRect(50, 340, 201, 31))
        self.lock_screen.setIcon(QIcon(QPixmap("qrc/screen.png")))
        self.lock_screen.setIconSize(QSize(30, 30))
        self.lock_screen.setStyleSheet("font: 16pt \"Roboto Medium\";border:0px")
        self.Page_Stack.addWidget(self.page_0)

        self.page_1 = QWidget()
        self.star = QPushButton(self.page_1)
        self.star.setGeometry(QRect(15, 0, 125, 125))
        self.star.setStyleSheet("border: 0px")
        self.star.setIcon(QIcon(QPixmap("qrc/star.png")))
        self.star.setIconSize(QSize(110, 110))
        self.wake = QLabel(self.page_1)
        self.wake.setGeometry(QRect(120, 100, 70, 61))
        self.wake.setStyleSheet("font: 30pt \"Roboto\"")
        self.sleep = QLabel(self.page_1)
        self.sleep.setGeometry(QRect(120, 170, 80, 61))
        self.sleep.setStyleSheet("font: 30pt \"Roboto\";")
        self.wake_h = QLineEdit(self.page_1)
        self.wake_h.setGeometry(QRect(220, 110, 51, 43))
        self.wake_h.setStyleSheet("font: 30pt \"Roboto\";border:0px")
        self.wake_m = QLineEdit(self.page_1)
        self.wake_m.setGeometry(QRect(330, 110, 51, 43))
        self.wake_m.setStyleSheet("font: 30pt \"Roboto\";border:0px")
        self.non_sleep_1 = QLabel(self.page_1)
        self.non_sleep_1.setGeometry(QRect(300, 110, 16, 41))
        self.non_sleep_1.setStyleSheet("font: 30pt \"Roboto\"")
        self.non_sleep_2 = QLabel(self.page_1)
        self.non_sleep_2.setGeometry(QRect(300, 180, 16, 41))
        self.non_sleep_2.setStyleSheet("font: 30pt \"Roboto\"")
        self.sleep_h = QLineEdit(self.page_1)
        self.sleep_h.setGeometry(QRect(220, 180, 51, 43))
        self.sleep_h.setStyleSheet("font: 30pt \"Roboto\";border:0px")
        self.sleep_m = QLineEdit(self.page_1)
        self.sleep_m.setGeometry(QRect(330, 180, 51, 43))
        self.sleep_m.setStyleSheet("font: 30pt \"Roboto\";border:0px")
        self.start_sleep = QPushButton(self.page_1)
        self.start_sleep.setGeometry(QRect(270, 260, 50, 50))
        self.start_sleep.setStyleSheet("border: 0px;")
        self.start_sleep.setText("")
        self.start_sleep.setIcon(QIcon(QPixmap("qrc/start.png")))
        self.start_sleep.setIconSize(QSize(50, 50))
        self.edit_sleep = QPushButton(self.page_1)
        self.edit_sleep.setGeometry(QRect(470, 20, 54, 50))
        self.edit_sleep.setStyleSheet("border: 0px;")
        self.edit_sleep.setText("")
        self.edit_sleep.setIcon(QIcon(QPixmap("qrc/draw_lock.png")))
        self.edit_sleep.setIconSize(QSize(50, 50))
        self.AM_text = QLabel(self.page_1)
        self.AM_text.setGeometry(QRect(460, 110, 60, 43))
        self.AM_text.setStyleSheet("font: 30pt \"Roboto\"")
        self.AM_text.setText("AM")
        self.PM_text = QLabel(self.page_1)
        self.PM_text.setGeometry(QRect(460, 180, 60, 43))
        self.PM_text.setStyleSheet("font: 30pt \"Roboto\"")
        self.PM_text.setText("PM")
        self.sound_on = QCheckBox(self.page_1)
        self.sound_on.setGeometry(QRect(420, 280, 131, 31))
        self.sound_on.setStyleSheet("font: 14pt \"Roboto\"")
        self.auto_on = QCheckBox(self.page_1)
        self.auto_on.setGeometry(QRect(420, 310, 131, 31))
        self.auto_on.setStyleSheet("font: 14pt \"Roboto\"")
        self.password_on = QCheckBox(self.page_1)
        self.password_on.setGeometry(QRect(420, 340, 131, 31))
        self.password_on.setStyleSheet("font: 14pt \"Roboto\"")
        self.ngu_qua_gio = QPushButton(self.page_1)
        self.ngu_qua_gio.setGeometry(QRect(50, 340, 200, 31))
        self.ngu_qua_gio.setIcon(QIcon(QPixmap("qrc/tired.png")))
        self.ngu_qua_gio.setIconSize(QSize(35, 35))
        self.ngu_qua_gio.setStyleSheet("font: 16pt \"Roboto Medium\";background-color:pink;border:1px soild grey;border-radius:5px")
        self.ngu_qua_gio.hide()
        self.Page_Stack.addWidget(self.page_1)
        
        self.page_2 = QWidget()
        self.gridLayoutWidget = QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QRect(-5, 20, 580, 400))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.chon_bieu_do = QComboBox(self.page_2)
        self.chon_bieu_do.setGeometry(QRect(50, 7, 100, 22))
        self.chon_bieu_do.setStyleSheet("QComboBox{background-color: rgb(255,255,255);border: 1px solid grey;border-radius: 5px}QComboBox::drop-down{border:0px}QComboBox QAbstractItemView{background-color: rgb(255, 255, 255)}")
        self.chon_bieu_do.addItem("Biểu đồ Giờ")
        self.chon_bieu_do.addItem("Biểu đồ Phút")
        self.chon_bieu_do.addItem("Biểu đồ Ngủ")
        self.save = QPushButton(self.page_2)
        self.save.setGeometry(QRect(195, 7, 120, 22))
        self.save.setStyleSheet("QPushButton{color: rgb(56, 56, 56);background-color: rgb(255, 255, 155);border: 1px soild grey;border-radius: 5px;font: 13pt \"Roboto\"}QPushButton:hover{background-color: rgb(255, 255, 105)}")
        self.dele = QPushButton(self.page_2)
        self.dele.setGeometry(QRect(360, 7, 50, 22))
        self.dele.setStyleSheet("QPushButton{color: rgb(56, 56, 56);background-color: rgb(255, 255, 155);border: 1px soild grey;border-radius: 5px;font: 13pt \"Roboto\"}QPushButton:hover{background-color: rgb(255, 255, 105)}")
        self.Page_Stack.addWidget(self.page_2)

        self.page_3 = QWidget()
        self.Setting_Layout_Size = QWidget(self.page_3)
        self.Setting_Layout_Size.setGeometry(QRect(30, 30, 331, 291))
        self.Setting_Layout = QVBoxLayout(self.Setting_Layout_Size)
        self.Setting_Layout.setContentsMargins(0, 0, 0, 0)
        self.start_with = QCheckBox(self.Setting_Layout_Size)
        self.start_with.setStyleSheet("font: 16pt \"Roboto\"")
        self.Setting_Layout.addWidget(self.start_with)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.Setting_Layout.addItem(spacerItem1)
        self.open_with = QCheckBox(self.Setting_Layout_Size)
        self.open_with.setStyleSheet("font: 16pt \"Roboto\"")
        self.Setting_Layout.addWidget(self.open_with)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.Setting_Layout.addItem(spacerItem2)
        self.sound = QCheckBox(self.Setting_Layout_Size)
        self.sound.setStyleSheet("font: 16pt \"Roboto\";")
        self.Setting_Layout.addWidget(self.sound)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.Setting_Layout.addItem(spacerItem3)
        self.picture = QCheckBox(self.Setting_Layout_Size)
        self.picture.setStyleSheet("font: 16pt \"Roboto\";")
        self.Setting_Layout.addWidget(self.picture)
        spacerItem4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.Setting_Layout.addItem(spacerItem4)
        self.password = QCheckBox(self.Setting_Layout_Size)
        self.password.setStyleSheet("font:16pt \"Roboto\"")
        self.Setting_Layout.addWidget(self.password)
        self.file_edit = QPushButton(self.page_3)
        self.file_edit.setGeometry(QRect(80, 255, 41, 23))
        self.file_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(191, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
        self.text_edit = QPushButton(self.page_3)
        self.text_edit.setGeometry(QRect(140, 255, 41, 23))
        self.text_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(191, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color: rgb(211, 211, 211)}")
        self.password_edit = QPushButton(self.page_3)
        self.password_edit.setGeometry(QRect(80, 320, 41, 23))
        self.password_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(191, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color: rgb(211, 211, 211)}")
        self.check_update = QPushButton(self.page_3)
        self.check_update.setGeometry(QRect(250, 335, 180, 30))
        self.check_update.setStyleSheet("QPushButton{color: rgb(56, 56, 56);background-color: rgb(255, 255, 155);border: 1px soild grey;border-radius: 5px;font: 13pt \"Roboto Medium\"}QPushButton:hover{background-color: rgb(255, 255, 105)}")
        self.check_update.setIcon(QIcon(QPixmap("qrc/bird.png")))
        self.check_update.setIconSize(QSize(35, 35))
        self.eyes = QLabel(self.page_3)
        self.eyes.setGeometry(QRect(440, 265, 121, 121))
        self.eyes.setText("")
        self.eyes.setPixmap(QPixmap("qrc/eyes.png"))
        self.eyes.setScaledContents(True)
        self.Page_Stack.addWidget(self.page_3)

        self.page_4 = QWidget()
        self.text_about = QTextBrowser(self.page_4)
        self.text_about.setGeometry(QRect(10, 10, 552, 337))
        self.text_about.setStyleSheet("QTextBrowser{"
"    border:0px;"
"}"
"QScrollBar:vertical {"
"    border: 0px;"
"    background:white;"
"    width:5px;"
"    border-radius: 5px;"
"    margin: 0px;"
"}"
"QScrollBar::handle:vertical {"
"    min-height: 0px;"
"    border: 0px;"
"    border-radius: 5px;"
"    background-color: black;"
"}"
"QScrollBar::add-line:vertical {"
"    height: 0px;"
"    subcontrol-position: bottom;"
"    subcontrol-origin: margin;"
"}"
"QScrollBar::sub-line:vertical {"
"    height: 0px;"
"    subcontrol-position: top;"
"    subcontrol-origin: margin;"
"}")
        self.Social_Layout_Size = QWidget(self.page_4)
        self.Social_Layout_Size.setGeometry(QRect(40, 350, 191, 31))
        self.social_layout = QHBoxLayout(self.Social_Layout_Size)
        self.social_layout.setContentsMargins(0, 0, 0, 0)
        self.website = QPushButton(self.Social_Layout_Size)
        font = QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.website.setFont(font)
        self.website.setStyleSheet("border: 0px")
        self.social_layout.addWidget(self.website)
        self.youtube = QPushButton(self.Social_Layout_Size)
        self.youtube.setFont(font)
        self.youtube.setStyleSheet("border: 0px")
        self.social_layout.addWidget(self.youtube)
        self.blogspot = QPushButton(self.Social_Layout_Size)
        self.blogspot.setFont(font)
        self.blogspot.setStyleSheet("border: 0px")
        self.social_layout.addWidget(self.blogspot)
        self.facebook = QPushButton(self.Social_Layout_Size)
        self.facebook.setFont(font)
        self.facebook.setStyleSheet("border: 0px")
        self.social_layout.addWidget(self.facebook)
        self.insta = QPushButton(self.Social_Layout_Size)
        self.insta.setFont(font)
        self.insta.setStyleSheet("border: 0px")
        self.social_layout.addWidget(self.insta)
        self.mail = QPushButton(self.Social_Layout_Size)
        self.mail.setFont(font)
        self.mail.setStyleSheet("border: 0px")
        self.social_layout.addWidget(self.mail)
        self.Page_Stack.addWidget(self.page_4)

        self.left_widget = QFrame(MainWindow)
        self.left_widget.setGeometry(QRect(0, 0, 142, 411))
        self.left_widget.setStyleSheet("background-color: rgb(233, 233, 233);")
        self.left_widget.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_widget.setFrameShadow(QFrame.Shadow.Raised)
        self.Left_Layout_Size = QWidget(self.left_widget)
        self.Left_Layout_Size.setGeometry(QRect(0, 15, 142, 241))
        self.set_layout = QVBoxLayout(self.Left_Layout_Size)
        self.set_layout.setContentsMargins(0, 0, 0, 0)
        self.set_time = QPushButton(self.Left_Layout_Size)
        self.set_time.setMinimumSize(QSize(0, 40))
        self.set_time.setStyleSheet("QPushButton{color: rgb(56, 56, 56);font: 14pt \"Roboto\";border: 0px;text-align: left}QPushButton:hover{background-color: rgb(191, 191, 191)}")
        self.set_time.setIcon(QIcon(QPixmap("qrc/time.png")))
        self.set_time.setIconSize(QSize(35, 35))
        self.set_layout.addWidget(self.set_time)

        self.set_sleep = QPushButton(self.Left_Layout_Size)
        self.set_sleep.setMinimumSize(QSize(0, 40))
        self.set_sleep.setStyleSheet("QPushButton{color: rgb(56, 56, 56);font: 14pt \"Roboto\";border: 0px;text-align: left}QPushButton:hover{background-color: rgb(191, 191, 191)}")
        self.set_sleep.setIcon(QIcon(QPixmap("qrc/night.png")))
        self.set_sleep.setIconSize(QSize(35, 35))
        self.set_layout.addWidget(self.set_sleep)

        self.set_chart = QPushButton(self.Left_Layout_Size)
        self.set_chart.setMinimumSize(QSize(0, 40))
        self.set_chart.setStyleSheet("QPushButton{color: rgb(56, 56, 56);font: 14pt \"Roboto\";border: 0px;text-align: left}QPushButton:hover{background-color: rgb(191, 191, 191)}")
        self.set_chart.setIcon(QIcon(QPixmap("qrc/chart.png")))
        self.set_chart.setIconSize(QSize(35, 35))
        self.set_layout.addWidget(self.set_chart)
        self.set_setting = QPushButton(self.Left_Layout_Size)
        self.set_setting.setMinimumSize(QSize(0, 40))
        self.set_setting.setStyleSheet("QPushButton{color: rgb(56, 56, 56);font: 14pt \"Roboto\";border: 0px;text-align: left}QPushButton:hover{background-color: rgb(191, 191, 191)}")
        self.set_setting.setIcon(QIcon(QPixmap("qrc/setting.png")))
        self.set_setting.setIconSize(QSize(35, 35))
        self.set_layout.addWidget(self.set_setting)
        self.set_about = QPushButton(self.Left_Layout_Size)
        self.set_about.setMinimumSize(QSize(0, 40))
        self.set_about.setStyleSheet("QPushButton{color: rgb(56, 56, 56);font: 14pt \"Roboto\";border: 0px;text-align: left}QPushButton:hover{background-color: rgb(191, 191, 191)}")
        self.set_about.setIcon(QIcon(QPixmap("qrc/about.png")))
        self.set_about.setIconSize(QSize(35, 35))
        self.set_layout.addWidget(self.set_about)

        self.work_h.setValidator(QIntValidator())
        self.work_m.setValidator(QIntValidator())
        self.work_s.setValidator(QIntValidator())
        self.relax_h.setValidator(QIntValidator())
        self.relax_m.setValidator(QIntValidator())
        self.relax_s.setValidator(QIntValidator())
        self.work_h.setReadOnly(True)
        self.work_m.setReadOnly(True)
        self.work_s.setReadOnly(True)
        self.relax_h.setReadOnly(True)
        self.relax_m.setReadOnly(True)
        self.relax_s.setReadOnly(True)
        self.work_h.setMaxLength(2)
        self.work_m.setMaxLength(2)
        self.work_s.setMaxLength(2)
        self.relax_h.setMaxLength(2)
        self.relax_m.setMaxLength(2)
        self.relax_s.setMaxLength(2)

        self.wake_h.setValidator(QIntValidator())
        self.wake_m.setValidator(QIntValidator())
        self.sleep_h.setValidator(QIntValidator())
        self.sleep_m.setValidator(QIntValidator())
        self.wake_h.setReadOnly(True)
        self.wake_m.setReadOnly(True)
        self.sleep_h.setReadOnly(True)
        self.sleep_m.setReadOnly(True)
        self.wake_h.setMaxLength(2)
        self.wake_m.setMaxLength(2)
        self.sleep_h.setMaxLength(2)
        self.sleep_m.setMaxLength(2)
        QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("EyeCare")
        self.work.setText("Làm Việc")
        self.relax.setText("Nghỉ")
        self.non_1.setText(":")
        self.non_2.setText(":")
        self.non_3.setText(":")
        self.non_4.setText(":")
        self.non_sleep_1.setText(":")
        self.non_sleep_2.setText(":")
        self.password_edit.setText("Sửa")
        self.time_left.setText("Còn 00:00:00")
        self.lock_screen.setText(" Khóa màn hình")
        self.ngu_qua_gio.setText("Ngủ quá giờ rồi!!")
        self.wake.setText("Dậy")
        self.sleep.setText("Ngủ")
        self.start_with.setText("Khởi động cùng hệ thống")
        self.open_with.setText("Mở giao diện app khi khởi động")
        self.sound.setText("Âm Thanh")
        self.picture.setText("Hình chờ")
        self.password.setText("Mật khẩu")
        self.file_edit.setText("File")
        self.text_edit.setText("Chữ")
        self.check_update.setText("Kiểm tra cập nhật")
        self.website.setText("K")
        self.youtube.setText("M")
        self.blogspot.setText("N")
        self.facebook.setText("E")
        self.insta.setText("Q")
        self.mail.setText("k")
        self.set_time.setText("Đặt thời gian")
        self.set_sleep.setText("Đặt TG ngủ")
        self.set_chart.setText("Thống kê")
        self.set_setting.setText("Cài đặt")
        self.set_about.setText("Giới Thiệu")
        self.save.setText("Lưu (theo Giờ)")
        self.dele.setText("Xóa")
        self.sound_on.setText("Âm Thanh")
        self.auto_on.setText("Tự khởi động")
        self.password_on.setText("Mật khẩu")
        self.Page_Stack.setCurrentIndex(0)
        self.text_about.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Light\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"font-family:\'Roboto Medium\'; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">EyeCare 1.0</span></p>"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Copyright ©2021 EyeCare _ MINK</span></p>"
"<p style=\" font-family:\'Roboto Medium\'; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\"> Tầm quan trọng của việc bảo vệ mắt</span></p>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> “Đôi mắt là cửa sổ tâm hồn”, thế nhưng vì nhiều mục đích như làm việc, tra cứu, học tập mà bạn phải ngồi hàng giờ liền trên máy vi tính. Việc này tác động nhiều đến đôi mắt của bạn, thậm chí gây nguy hiểm cho mắt. Vậy làm thế nào để bảo vệ, ngăn ngừa, giảm mỏi mắt khi dùng máy tính?</span></p>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Với những người dùng máy vi tính, đặc biệt là dân văn phòng thì tình trạng nhức mỏi mắt là vấn đề thường xuyên xảy ra. Nhiều nghiên cứu chỉ ra tới 50–90% người dùng máy vi tính bị hiện tượng mỏi mắt và các triệu chứng thị giác khó chịu khác.</span></p>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Những vấn đề này sẽ ảnh hưởng nhiều đến sức khỏe, nó khiến bạn mệt mỏi về thể chất, tinh thần giảm hiệu suất làm việc. Thậm chí, dùng máy tính một thời gian dài cũng gây những vấn đề về mắt rất khó chịu như co giật mắt, tăng độ cận, mắt đỏ…</span></p>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Vấn đề này có lẽ chúng ta đều đã biết, nhưng vì ở thời đại 4.0, công việc bắt buộc phải dùng máy tính, chúng ta chỉ còn cách tự bảo vệ mắt của mình. Chúng ta thường chú ý đến việc ngồi cách xa màn hình máy tính, ngồi đúng tư thế mà quên mất việc cho đôi mắt nghỉ ngơi một chút khi làm việc vất vả. Vì vậy, chương trình EyeCare ra đời nhằm giải quyết vấn đề đó. EyeCare giúp chúng ta đặt lịch nghỉ ngơi tự động sau một khoảng thời gian, khi đến thời gian nghỉ chương trình sẽ thông báo với bạn, chủ động khóa máy tính để bạn có thể đảm bảo việc nghỉ ngơi một cách tốt nhất. Trong thời gian đó, bạn hãy gác lại công việc, có thể làm một tách cafe, chớp mắt, một cốc sữa, massage cho mắt, ... Sau đó, bạn có thể quay lại làm việc, đôi mắt sẽ được nghỉ ngơi một khoảng thời gian nhất định, sẽ không còn bị mỏi, đau mắt nữa.</span></p>"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>"
"<p style=\" font-family:\'Roboto Medium\'; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\"> Đề xuất: Nguyên tắc 20 – 20 – 20 bảo vệ mắt</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Cứ mỗi 20 phút làm việc với máy tính, hãy bỏ 20 giây không dùng máy tính để nhìn ra xa 20 feet (&lt;=&gt; 609.6 cm). Điều này giúp mắt bạn được nghỉ ngơi hợp lý, thư giãn mắt, chống mỏi mắt.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Mặc định, EyeCare sẽ được cài đặt chế độ nghỉ ngơi theo nguyên tắc trên.</span></p>"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>"
"<p style=\" font-family:\'Roboto Medium\'; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\"> Ngoài ra...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> EyeCare còn hỗ trợ bạn thiết lập thời gian đi ngủ! Khi bạn ngủ đủ giấc, bạn sẽ làm việc một cách hiệu quả hơn!</span></p>"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\"> &quot;EyeCare - Vì đôi mắt của bạn&quot;</span></p></body></html>")
