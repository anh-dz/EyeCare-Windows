# -*- coding: utf-8 -*-
__author__ = "Mink Alex Vina"
__copyright__ = "Copyright 2021, EyeCare"
__credits__ = "Mink Alex Vina"
__license__ = "EyeCare"
__version__ = "1.0"
__email__ = "nmnanh1235@gmail.com"

import psutil, sys
from mod import *
if tuple(p.name() for p in psutil.process_iter()).count("EyeCare.exe")>1:
    Notifi().show_toast("EyeCare is still running!")
    sys.exit()

start = time.time()

_time = open_time()
_time[0], _time[1] = [i.zfill(2) for i in _time[0]], [i.zfill(2) for i in _time[1]]
_setting, _pass = open_setting()
_time_sleep, _setting_sleep = open_sleep()
sleep_data = open_sleep_data()
_det = open_det()
_setting_const, _det_const, _pass_const, _time_sleep_const, _setting_sleep_const = tuple(_setting.copy()), tuple(_det.copy()), "%s" %_pass, tuple(_time_sleep.copy()), tuple(_setting_sleep.copy())
days, data = open_data()
date_today = time.strftime("%d/%m/%y", time.localtime())
if days == None: days, data = [date_today], [0.1]
sleep_list = create_sleep_list(sleep_data, days)

class Time_COUNT(QThread):
    def run(self):
        time__about__temp = time__about.copy()
        while not start__:
            while pause_: pass
            if start__: break
            widgets.time_left.setText(f"{str(time__about__temp[0]).zfill(2)}:{str(time__about__temp[1]).zfill(2)}:{str(time__about__temp[2]).zfill(2)} Left")
            if start__: break
            time.sleep(1)
            if start__: break
            time__about__temp[2]-=1
            if time__about__temp[0] == 0 and time__about__temp[1] == 0 and time__about__temp[2] == 5:
                Notifi().show_toast("Your eye need to rest now! Remember to save your work <3")
            if time__about__temp[2]<1:
                if time__about__temp[1]>0:
                    time__about__temp[1]-=1
                    time__about__temp[2] = 59
                elif time__about__temp[0]>0:
                    time__about__temp[0]-=1
                    time__about__temp[1], time__about__temp[2] = 59, 59
                else:
                    time__about__temp = time__about.copy()
                    focus(_setting[3], _setting[2], _det, tim_wait)
        time__about__temp.clear()
class Time_SLEEP(QThread):
    def run(self):
        self.hour_wake = int(widgets.wake_h.text())
        self.min_wake = int(widgets.wake_m.text())
        self.hour_sleep = int(widgets.sleep_h.text())+12
        self.min_sleep = int(widgets.sleep_m.text())
        self.local_time = time.localtime()
        time_left = self.sleep_count()
        while not __sleep_start__:
            self.sleep_check(time_left)
            if time_left == 15: Notifi().show_toast("15 minutes left. Prepare to sleep!!!")
            elif time_left == 5: Notifi().show_toast("5 minutes left. Prepare to sleep!!!")
            elif time_left == 1: Notifi().show_toast("1 minutes left. Good night <3")
            time.sleep(60)
            time_left-=1
    def sleep_count(self):
        sec_left = (self.hour_sleep-self.local_time.tm_hour)*3600+(self.min_sleep-self.local_time.tm_min)*60+self.local_time.tm_sec
        return round(sec_left/60)
    def sleep_check(self, time_left):
        if time_left<=0 or self.local_time.tm_hour<self.hour_wake:
            sleep_lock(_setting_sleep[0], _setting_sleep[2], _pass)
            self.dectect()
        elif self.local_time.tm_hour==self.hour_wake:
            if self.local_time.tm_min<self.min_wake:
                sleep_lock(_setting_sleep[0], _setting_sleep[2], _pass)
                self.dectect()
    def dectect(self):
        global __sleep_start__
        __sleep_start__ = True
        if sleep_data == [] or sleep_data[-1] != days[-1]:
            sleep_data.append(date_today)
            sleep_list[-1] = 1
            write_sleep_data(user, 'sleep_data', sleep_data)
        widgets.ngu_qua_gio.show()
        widgets.start_sleep.setIcon(QIcon(QPixmap("qrc/start.png")))
        Notifi().show_toast("Ngủ muộn không tốt cho sức khỏe đâu :(")

class Main_APP(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.tray_icon()
        self.bieu_do(0)

        self.edit_sleep_, self.edit_ = False, False

        widgets.chon_bieu_do.currentIndexChanged.connect(lambda: self.bieu_do(widgets.chon_bieu_do.currentIndex()))

        widgets.start_with.setChecked(_setting[0])
        widgets.open_with.setChecked(_setting[1])
        widgets.sound.setChecked(_setting[2])
        widgets.picture.setChecked(_setting[3])
        widgets.password.setChecked(_setting[4])

        widgets.start_with.clicked.connect(self.start_with_active)
        widgets.open_with.clicked.connect(self.open_with_active)
        widgets.sound.clicked.connect(self.sound_active)
        widgets.picture.clicked.connect(self.picture_active)
        widgets.password.clicked.connect(self.password_active)
        widgets.file_edit.clicked.connect(self.file_edit_active)
        widgets.text_edit.clicked.connect(self.text_edit_active)
        widgets.password_edit.clicked.connect(self.password_edit_active)

        #ABOUT
        widgets.website.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://anh-dz.github.io/eyecare/")))
        widgets.youtube.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://youtube.com/minkalexvina")))
        widgets.blogspot.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://chuyendanit.blogspot.com")))
        widgets.facebook.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://facebook.com/minkalexvina")))
        widgets.insta.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://instagram.com/minkalexvina")))
        widgets.mail.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("mailto:nmnanh1235@gmail.com")))

        if _setting[3] == 1: widgets.file_edit.setStyleSheet("QPushButton{background-color:rgb(101, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
        elif _setting[3] == 2: widgets.text_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(101, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")

        widgets.set_time.clicked.connect(lambda: widgets.Page_Stack.setCurrentIndex(0))
        widgets.set_sleep.clicked.connect(lambda: widgets.Page_Stack.setCurrentIndex(1))
        widgets.set_chart.clicked.connect(lambda: widgets.Page_Stack.setCurrentIndex(2))
        widgets.set_about.clicked.connect(lambda: widgets.Page_Stack.setCurrentIndex(4))
        widgets.set_setting.clicked.connect(self.set_setting_open)

        widgets.start_sleep.clicked.connect(self.start_sleep_active)
        widgets.start.clicked.connect(self.start_active)
        widgets.button_pause.clicked.connect(self.pause_active)
        widgets.check_update.clicked.connect(self.update_active)
        widgets.edit.clicked.connect(self.edit_active)
        widgets.edit_sleep.clicked.connect(self.edit_sleep_active)
        widgets.lock_screen.clicked.connect(lambda: lock_lock(_pass))
        widgets.save.clicked.connect(lambda: self.save_active(widgets.chon_bieu_do.currentIndex()))
        widgets.dele.clicked.connect(lambda: self.dele_active(widgets.chon_bieu_do.currentIndex()))

        widgets.work_h.setText(_time[0][0])
        widgets.work_m.setText(_time[0][1])
        widgets.work_s.setText(_time[0][2])
        widgets.relax_h.setText(_time[1][0])
        widgets.relax_m.setText(_time[1][1])
        widgets.relax_s.setText(_time[1][2])

        widgets.wake_h.setText(_time_sleep[0][0])
        widgets.wake_m.setText(_time_sleep[0][1])
        widgets.sleep_h.setText(_time_sleep[1][0])
        widgets.sleep_m.setText(_time_sleep[1][1])

        widgets.sound_on.setChecked(_setting_sleep[0])
        widgets.auto_on.setChecked(_setting_sleep[1])
        widgets.password_on.setChecked(_setting_sleep[2])
        widgets.sound_on.clicked.connect(self.sound_on_active)
        widgets.auto_on.clicked.connect(self.auto_on_active)
        widgets.password_on.clicked.connect(self.password_on_active)

        self.installEventFilter(self)

        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon("logo.ico"))
        self.msg.setWindowTitle("EyeCare")
        self.show() if _setting[1] else widgets.start.click()
        if _setting_sleep[1]: widgets.start_sleep.click()

#MAIN FUNTION
    def start_active(self):
        global start__
        if start__:
            global tim_cout, tim_wait
            global time__about
            time__about = [widgets.work_h.text(), widgets.work_m.text(), widgets.work_s.text()]
            wait_time = [widgets.relax_h.text(), widgets.relax_m.text(), widgets.relax_s.text()]
            for i in range(3):
                if time__about[i]=="": time__about[i]=0
                else: time__about[i]=int(time__about[i])
                if wait_time[i]=="": wait_time[i]=0
                else: wait_time[i]=int(wait_time[i])
            tim_cout = 1000*(time__about[0]*3600+time__about[1]*60+time__about[2])
            tim_wait = 1000*(wait_time[0]*3600+wait_time[1]*60+wait_time[2])
            if tim_cout == 0 and tim_wait == 0:
                time__about[0], time__about[1], time__about[2] = 0, 20, 0
                wait_time[0], wait_time[1], wait_time[2] = 0, 0, 20
                self.active()
            elif tim_cout<10000 or tim_wait<10000:
                self.msg.setText("Work and rest time must be over 10 seconds")
                self.msg.exec()
            elif tim_wait>3600000 and not self.isHidden():
                self.msg.setText("Warning: Too much break time. When the break time is active, you will not be able to use the computer")
                self.msg.exec()
                self.active()
            else: self.active()
        else:
            _temp_pass = False
            if _setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_==_pass: _temp_pass = True
                else: self.wrong_password()
            else: _temp_pass = True
            if _temp_pass: self.call_stop()
    def active(self):
        global start__
        start__ = False
        widgets.button_pause.setVisible(True)
        widgets.start.setIcon(QIcon(QPixmap("qrc/stop.png")))
        self.pause_app = QAction("Pause")
        self.start_app = QAction("Stop")
        self.tray_menu.addAction(self.pause_app)
        self.tray_menu.addAction(self.start_app)
        self.pause_app.triggered.connect(self.pause_click)
        self.start_app.triggered.connect(self.start_click)
        self.COUNT = Time_COUNT()
        self.COUNT.start()
    def call_stop(self):
        global start__, pause_
        start__, pause_ = True, False
        widgets.button_pause.setVisible(False)
        widgets.start.setIcon(QIcon(QPixmap("qrc/start.png")))
        widgets.button_pause.setIcon(QIcon(QPixmap("qrc/pause.png")))
        self.start_app = QAction("Start")
        self.tray_menu.removeAction(self.pause_app)
        self.tray_menu.addAction(self.start_app)
        self.start_app.triggered.connect(self.start_click)

    #JUST A BUTTON
    def pause_active(self):
        global pause_
        if not pause_:
            _temp_pass = False
            if _setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_ == _pass:  _temp_pass = True
                else: self.wrong_password()
            else: _temp_pass = True
            if _temp_pass:
                widgets.button_pause.setIcon(QIcon(QPixmap("qrc/start.png")))
                self.pause_app = QAction("Tiếp tục")
                self.start_app = QAction("Dừng")
                self.tray_menu.addAction(self.pause_app)
                self.tray_menu.addAction(self.start_app)
                self.pause_app.triggered.connect(self.pause_click)
                self.start_app.triggered.connect(self.start_click)
                pause_ = True
        else:
            widgets.button_pause.setIcon(QIcon(QPixmap("qrc/pause.png")))
            self.pause_app = QAction("Tạm dừng")
            self.start_app = QAction("Dừng")
            self.tray_menu.addAction(self.pause_app)
            self.tray_menu.addAction(self.start_app)
            self.pause_app.triggered.connect(self.pause_click)
            self.start_app.triggered.connect(self.start_click)
            pause_ = False
    def edit_active(self):
        if self.edit_:
            widgets.edit.setIcon(QIcon(QPixmap("qrc/draw_lock.png")))
            widgets.work_h.setReadOnly(True)
            widgets.work_m.setReadOnly(True)
            widgets.work_s.setReadOnly(True)
            widgets.relax_h.setReadOnly(True)
            widgets.relax_m.setReadOnly(True)
            widgets.relax_s.setReadOnly(True)
            self.edit_ = False
        else:
            _temp_pass = False
            if _setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_ == _pass: _temp_pass = True
                else: self.wrong_password()
            else: _temp_pass = True
            if _temp_pass:
                widgets.edit.setIcon(QIcon(QPixmap("qrc/draw_un.png")))
                widgets.work_h.setReadOnly(False)
                widgets.work_m.setReadOnly(False)
                widgets.work_s.setReadOnly(False)
                widgets.relax_h.setReadOnly(False)
                widgets.relax_m.setReadOnly(False)
                widgets.relax_s.setReadOnly(False)
                self.edit_ = True

#SLEEP
    def start_sleep_active(self):
        global __sleep_start__
        if __sleep_start__:
            if 0<int(widgets.wake_h.text())<13 or 0<int(widgets.wake_m.text())<13 or 0<int(widgets.sleep_h.text())<13 or 0<int(widgets.sleep_m.text())<13:
                self.SLEEP = Time_SLEEP()
                self.SLEEP.start()
                widgets.start_sleep.setIcon(QIcon(QPixmap("qrc/stop.png")))
                __sleep_start__ = False
            else:
                self.msg.setText("Thời gian không hợp lệ!")
                self.msg.exec()
        else:
            _temp_pass = False
            if _setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_ == _pass: _temp_pass = True
                else: self.wrong_password()
            else: _temp_pass = True
            if _temp_pass:
                widgets.start_sleep.setIcon(QIcon(QPixmap("qrc/start.png")))
                __sleep_start__ = True
    def edit_sleep_active(self):
        if self.edit_sleep_:
            widgets.edit_sleep.setIcon(QIcon(QPixmap("qrc/draw_lock.png")))
            widgets.wake_h.setReadOnly(True)
            widgets.wake_m.setReadOnly(True)
            widgets.sleep_h.setReadOnly(True)
            widgets.sleep_m.setReadOnly(True)
            self.edit_sleep_ = False
        else:
            _temp_pass = False
            if _setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_ == _pass: _temp_pass = True
                else: self.wrong_password()
            else: _temp_pass = True
            if _temp_pass:
                widgets.edit_sleep.setIcon(QIcon(QPixmap("qrc/draw_un.png")))
                widgets.wake_h.setReadOnly(False)
                widgets.wake_m.setReadOnly(False)
                widgets.sleep_h.setReadOnly(False)
                widgets.sleep_m.setReadOnly(False)
                self.edit_sleep_ = True
    def sound_on_active(self):
        if _setting_sleep[0] == 0:
            _setting_sleep[0] = 1
        else:
            if _setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_ == _pass:
                    _setting_sleep[0] = 0
                else:
                    widgets.sound_on.setChecked(True)
                    self.wrong_password()
            else:
                _setting_sleep[0] = 0
    def auto_on_active(self):
        if _setting_sleep[1] == 0:
            _setting_sleep[1] = 1
        else:
            if _setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_ == _pass:
                    _setting_sleep[1] = 0
                else:
                    widgets.auto_on.setChecked(True)
                    self.wrong_password()
            else:
                _setting_sleep[1] = 0
    def password_on_active(self):
        if _setting_sleep[2] == 0:
            _setting_sleep[2] = 1
        else:
            if _setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_ == _pass:
                    _setting_sleep[2] = 0
                else:
                    widgets.password_on.setChecked(True)
                    self.wrong_password()
            else:
                _setting_sleep[2] = 0

#CHART
    def bieu_do(self, num):
        text = widgets.chon_bieu_do.currentText()
        widgets.save.setText(f"Save")
        gio = QBarSet(text[:6])
        if not num: data_temp = data
        elif num==1: data_temp = [i*60 for i in data]
        else:
            gio = QBarSet("Sleep Too Late!!!")
            data_temp = sleep_list
        gio.append(data_temp)
        series = QBarSeries()
        series.append(gio)
        chart = QChart()
        chart.setTitle(text)
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        axisX = QValueAxis()
        chart.addAxis(axisX, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axisX)
        axisY = QBarCategoryAxis()
        axisY.append(days)
        chart.addAxis(axisY, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axisY)
        axisX.applyNiceNumbers()
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.chartview_chart = QChartView(chart)
        if widgets.gridLayout.count(): widgets.gridLayout.itemAt(0).widget().setParent(None)
        widgets.gridLayout.addWidget(self.chartview_chart)
    def save_active(self, num):
        name = QFileDialog.getSaveFileName(parent = None, caption = 'File Save', filter ="Text (*.txt)")
        if name!=('', ''):
            st = ""
            if not num:
                for i, j in zip(days, data):
                    temp = f"{i} {j:.3f}\n"
                    st+=temp
            elif num==1:
                for i, j in zip(days, [i*60 for i in data]):
                    temp = f"{i} {j:.3f}\n"
                    st+=temp
            elif num==2:
                st = "Slep Fail\n"
                for i in sleep_data:
                    st+=(i+"\n")
            write_chart_file(name[0], st)
            self.msg.setText("Success!")
            self.msg.exec()
    def dele_active(self, num):
        if self.areusure():
            if num!=2:
                global days, data
                days, data = [date_today], [0.1]
            else:
                global sleep_data
                sleep_data, sleep_list = [], []
            self.bieu_do(num)

#SETTING
    def set_setting_open(self):
        _temp_pass = False
        if _setting[4]:
            self._pass = GET_PASS(self)
            self._pass.exec()
            if self._pass._pass_check_==_pass: _temp_pass = True
            else: self.wrong_password()
        else: _temp_pass = True
        if _temp_pass: widgets.Page_Stack.setCurrentIndex(3)
    def open_with_active(self):
        if _setting[1]: _setting[1] = 0
        else: _setting[1] = 1
    def sound_active(self):
        if _setting[2]: _setting[2] = 0
        else: _setting[2] = 1
    def picture_active(self):
        if _setting[3]: _setting[3] = 0
        else: _setting[3] = 1
    def password_active(self):
        if _setting[4]:
            self._pass = GET_PASS(self)
            self._pass.exec()
            if self._pass._pass_check_ == _pass:
                _setting[4] = 0
            else:
                widgets.password.setChecked(True)
                self.wrong_password()
        else:
            _setting[4] = 1
    def start_with_active(self):
        if _setting[0]:
            _setting[0] = 0
            delete_file("Microsoft//Windows//Start Menu//Programs//Startup//EyeCare.lnk")
        else:
            if create_shortcut(f'C://Users//{user}//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup', "EyeCare.lnk"):
                _setting[0] = 1
            else:
                widgets.start_with.setChecked(False)
                self.msg.setText("Lỗi khởi tạo, vui lòng thử lại")
                self.msg.exec()
    def file_edit_active(self):
        dirr = _det[0]
        name = QFileDialog.getOpenFileName(parent = None, caption = 'File Selected', directory = dirr, filter ="Pictures (*.jpg *.png *.bmp)")
        if name != ('', ''):
            _setting[3] = 1
            _det[0] = name[0]
            widgets.text_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(191, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
            widgets.file_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(101, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
    def text_edit_active(self):
        self._word = GET_WORD(self, _det[1])
        self._word.exec()
        if self._word._word_check_ == '':
            _setting[3] = 2
            widgets.file_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(191, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
            widgets.text_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(101, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
        elif self._word._word_check_ != None:
            _setting[3] = 2
            _det[1] = self._word._word_check_
            widgets.file_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(191, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
            widgets.text_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(101, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
    def password_edit_active(self):
        global _pass
        self._pass = GET_PASS(self)
        self._pass.exec()
        if self._pass._pass_check_ == _pass:
            self._change_pass = GET_PASS(self, "--New password--")
            self._change_pass.exec()
            _pass_temp_ = '%s' %self._change_pass._pass_check_
            if _pass_temp_ == None or _pass_temp_ == "":
                self.msg.setText("Password need to be fill!!!")
                self.msg.exec()
                return
            _change_pass_check = GET_PASS(self, "--Enter your password again--")
            _change_pass_check.exec()
            if _pass_temp_ == _change_pass_check._pass_check_:
                pass
            else:
                while _pass_temp_ != _change_pass_check._pass_check_:
                    _change_pass_check._pass_check_ = None
                    _change_pass_check = GET_PASS(self, "--Please Try Again--")
                    _change_pass_check.exec()
                    if _change_pass_check._pass_check_ == None:
                        self.msg.setText("Change Fail")
                        self.msg.exec()
                        return
            _pass = '%s' %_pass_temp_
            self.msg.setText("Success")
            self.msg.exec()
        else:
            self.wrong_password()

#ANOTHER
    def wrong_password(self):
        self.msg.setText("~Wrong Password~")
        self.msg.exec()
    def update_active(self):
        try:
            if urlopen('https://anh-dz.github.io/eyecare/version.html').read() != b'1\n': self.msg.setText("Found a new version. Please go to our homepage to update now!")
            else: self.msg.setText("No update available")
        except: self.msg.setText("Can't connect to server. Please try again!")
        self.msg.exec()
    def areusure(self):
        box = QMessageBox()
        box.setWindowTitle('EyeCare')
        box.setWindowIcon(QIcon("logo.ico"))
        box.setIconPixmap(QIcon("qrc/bird.png").pixmap(35, 35))
        box.setText('Are you sure?')
        box.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        buttonY = box.button(QMessageBox.StandardButton.Yes)
        buttonY.setText('Yes')
        buttonN = box.button(QMessageBox.StandardButton.No)
        buttonN.setText('Nope')
        box.exec()
        if box.clickedButton() == buttonY:
            return True
        return False

#EVENT
    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if self.isMinimized():
                self.hide()
        return False
    def closeEvent(self, event):
        global _time_const, _sleep_const
        if _setting[4]:
            self.show_eyecare()
            event.ignore()
            _temp_pass = False
            self._pass = GET_PASS(self)
            self._pass.exec()
            if self._pass._pass_check_ == _pass: _temp_pass = True
            else: self.wrong_password()
        else: _temp_pass = True
        if _temp_pass:
            event.accept()
            _time_const = ((widgets.work_h.text(), widgets.work_m.text(), widgets.work_s.text()), (widgets.relax_h.text(), widgets.relax_m.text(), widgets.relax_s.text()))
            _sleep_const = ((widgets.wake_h.text(), widgets.wake_m.text()), (widgets.sleep_h.text(), widgets.sleep_m.text()))
    def show_eyecare(self):
        self.show()
        if self.isMinimized():
            self.showNormal()

#TRAY ICON
    def start_click(self):
        if _setting[4] and not start__: self.show_eyecare()
        widgets.start.click()
    def pause_click(self):
        self.show_eyecare()
        widgets.button_pause.click()
    def tray_icon(self):
        def _show(reason): #Show the app
            if reason == self.tray.ActivationReason.Trigger: self.show_eyecare()
        self.tray_menu = QMenu()
        self.show_app = QAction("Show")
        self.hide_app = QAction("Hide")
        self.quit_app = QAction("Exit")
        self.start_app = QAction("Start")
        self.show_app.triggered.connect(self.show_eyecare)
        self.hide_app.triggered.connect(self.hide)
        self.quit_app.triggered.connect(self.close)
        self.start_app.triggered.connect(self.start_click)
        self.tray_menu.addAction(self.show_app)
        self.tray_menu.addAction(self.hide_app)
        self.tray_menu.addAction(self.quit_app)
        self.tray_menu.addAction(self.start_app)
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon('logo.ico'))
        self.tray.setContextMenu(self.tray_menu)
        self.tray.activated.connect(_show)
        self.tray.show()

start__, pause_, __sleep_start__  = True, False, True

app = QApplication(sys.argv)
ui = Main_APP()
app.exec()

end = time.time()

time_use = (end-start)/3600
try:
    if days[-1] == date_today:
        time_use = "{:0.6f}".format(time_use + data[-1])
        data[-1] = time_use
    else:
        days.append(date_today)
        data.append("{:0.6f}".format(time_use))
except:
    days.append(date_today)
    data.append("{:0.6f}".format(time_use))
data = [str(i) for i in data]
write_data(user, days[len(days)-7:], data[len(data)-7:])

if _setting_const != tuple(_setting) or _pass_const != _pass:
    write_two_file(user, "setting", " ".join([str(i) for i in _setting]), _pass)
if  _time_const != tuple(_time):
    write_two_file(user, "time", " ".join([i for i in _time_const[0]]), " ".join([str(i) for i in _time_const[1]]))
if _det_const != tuple(_det):
    write_two_file(user, "det", _det[0], _det[1])
if _setting_sleep_const != tuple(_setting_sleep) or _sleep_const != tuple(_time_sleep):
    temp=[]
    for i in _sleep_const:
        temp.append(i[0])
        temp.append(i[1])
    write_sleep_data(user, "sleep", temp+[str(i) for i in _setting_sleep])