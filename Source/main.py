# -*- coding: utf-8 -*-
__author__ = "Mink Alex Vina"
__copyright__ = "Copyright 2021, EyeCare"
__credits__ = "Mink Alex Vina"
__license__ = "EyeCare"
__version__ = "1.5"
__email__ = "nmnanh1235@gmail.com"

import psutil, sys
import keyboard
from mod import *

s, nlang, language = lang_focus()

with open('qrc//additionals.txt', 'r', encoding='utf-8') as f:
    language = f.read().split('\\')
    language[0] = language[0].splitlines()
    language[1] = language[1].splitlines()
    language[1].pop(0)

if tuple(p.name() for p in psutil.process_iter()).count("EyeCare.exe")>1:
    Notifi().show_toast(language[nlang][0])
    sys.exit()

isPwgsOn = False

class DialogFunc(Ui_Dialog):
    def __init__(self, main_app, start__):
        global Pwgs, isPwgsOn
        super().__init__()
        Pwgs = self
        self.main_app = main_app
        self.s = start__
        Pwgs.setupUi(self)
        Pwgs.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        Pwgs.pin_start.clicked.connect(self.pin_click)
        if self.s:
            Pwgs.pin_start.setIcon(QIcon(QPixmap("qrc/start.png")))
        else:
            Pwgs.pin_start.setIcon(QIcon(QPixmap("qrc/stop.png")))
        Pwgs.lb_time.setText(widgets.time_left.text().replace(' Left', '').replace('Còn ', ''))
        Pwgs.show()
        isPwgsOn = True
    
    def pin_click(self):
        widgets.start.click()

    def closeEvent(self, event):
        global isPwgsOn
        widgets.pin_btn.setIcon(QIcon("qrc/pin.png"))
        isPwgsOn = False
        if self.main_app.isHidden():
            event.ignore()
            self.main_app.show_eyecare()
            Pwgs.close()
class Time_COUNT(QThread):
    def __init__(self, _setting, _det, tim_wait, time__about, parent=None):
        super().__init__(parent)
        self._setting = _setting
        self._det = _det
        self.tim_wait = tim_wait
        self.time__about = time__about

    def run(self):
        time__about__temp = self.time__about.copy()
        while True:
            while pause_: pass
            if nlang == 0:
                widgets.time_left.setText(f"{str(time__about__temp[0]).zfill(2)}:{str(time__about__temp[1]).zfill(2)}:{str(time__about__temp[2]).zfill(2)} Left")
            else:
                widgets.time_left.setText(f"Còn {str(time__about__temp[0]).zfill(2)}:{str(time__about__temp[1]).zfill(2)}:{str(time__about__temp[2]).zfill(2)}")
            if isPwgsOn: Pwgs.lb_time.setText(f"{str(time__about__temp[0]).zfill(2)}:{str(time__about__temp[1]).zfill(2)}:{str(time__about__temp[2]).zfill(2)}")
            time.sleep(1)
            time__about__temp[2]-=1
            if time__about__temp[0] == 0 and time__about__temp[1] == 0 and time__about__temp[2] == 5:
                Notifi().show_toast(language[nlang][2])
            if time__about__temp[2]<1:
                if time__about__temp[1]>0:
                    time__about__temp[1]-=1
                    time__about__temp[2] = 59
                elif time__about__temp[0]>0:
                    time__about__temp[0]-=1
                    time__about__temp[1], time__about__temp[2] = 59, 59
                else:
                    time__about__temp = self.time__about.copy()
                    focus(self._setting[3], self._setting[2], self._det, self.tim_wait, nlang)

class Time_SLEEP(QThread):
    def __init__(self, _setting_sleep, _pass, sleep_data, days, date_today, sleep_list, parent=None):
        super().__init__(parent)
        self._setting_sleep = _setting_sleep
        self._pass = _pass
        self.sleep_data = sleep_data
        self.days = days
        self.date_today = date_today
        self.sleep_list = sleep_list

    def run(self):
        self.hour_wake = int(widgets.wake_h.text())
        self.min_wake = int(widgets.wake_m.text())
        self.hour_sleep = int(widgets.sleep_h.text()) + 12
        self.min_sleep = int(widgets.sleep_m.text())
        self.local_time = time.localtime()
        time_left = self.sleep_count()
        while not __sleep_start__:
            self.sleep_check(time_left)
            if time_left == 15: Notifi().show_toast(language[nlang][3])
            elif time_left == 5: Notifi().show_toast(language[nlang][4])
            elif time_left == 1: Notifi().show_toast(language[nlang][5])
            time.sleep(60)
            time_left -= 1

    def sleep_count(self):
        sec_left = (self.hour_sleep - self.local_time.tm_hour) * 3600 + (self.min_sleep - self.local_time.tm_min) * 60 + self.local_time.tm_sec
        return round(sec_left / 60)

    def sleep_check(self, time_left):
        if time_left <= 0 or self.local_time.tm_hour < self.hour_wake:
            sleep_lock(self._setting_sleep[0], self._setting_sleep[2], self._pass, nlang)
            self.detect()
        elif self.local_time.tm_hour == self.hour_wake:
            if self.local_time.tm_min < self.min_wake:
                sleep_lock(self._setting_sleep[0], self._setting_sleep[2], self._pass, nlang)
                self.detect()
    def detect(self):
        global __sleep_start__
        __sleep_start__ = True
        if self.sleep_data == [] or self.sleep_data[-1] != self.days[-1]:
            self.sleep_data.append(self.date_today)
            self.sleep_list[-1] = 1
            write_sleep_data(user, 'sleep_data', self.sleep_data)
        widgets.ngu_qua_gio.show()
        widgets.start_sleep.setIcon(QIcon(QPixmap("qrc/start.png")))
        Notifi().show_toast(language[nlang][6])

from PyQt6.QtCore import QThread, pyqtSignal
from urllib.request import urlopen

class UpdateCheckThread(QThread):
    update_result = pyqtSignal(str)

    def run(self):
        try:
            current_version = "1.5"
            response = urlopen('https://anh-dz.github.io/eyecare/version.html', timeout=1).read().decode().strip()
            if response != current_version:
                self.update_result.emit(language[nlang][26])
            else:
                self.update_result.emit(language[nlang][27])
        except:
            self.update_result.emit(language[nlang][28])

class Main_APP(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.ui.Page_Stack.setCurrentIndex(0)
        
        self.get_init_variable()

        self.tray_icon()
        self.bieu_do(0)

        widgets.language_combobox.currentIndexChanged.connect(self.change_language)
        self.change_language()
        
        widgets.chon_bieu_do.currentIndexChanged.connect(lambda: self.bieu_do(widgets.chon_bieu_do.currentIndex()))

        widgets.start_with.setChecked(self._setting[0])
        widgets.open_with.setChecked(self._setting[1])
        widgets.sound.setChecked(self._setting[2])
        widgets.picture.setChecked(self._setting[3])
        widgets.password.setChecked(self._setting[4])

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

        if self._setting[3] == 1: widgets.file_edit.setStyleSheet("QPushButton{background-color:rgb(101, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
        elif self._setting[3] == 2: widgets.text_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(101, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")

        widgets.set_time.clicked.connect(lambda: widgets.Page_Stack.setCurrentIndex(0))
        widgets.set_sleep.clicked.connect(lambda: widgets.Page_Stack.setCurrentIndex(1))
        widgets.set_chart.clicked.connect(lambda: widgets.Page_Stack.setCurrentIndex(2))
        widgets.set_about.clicked.connect(lambda: widgets.Page_Stack.setCurrentIndex(4))
        widgets.set_setting.clicked.connect(self.set_setting_open)

        widgets.start_sleep.clicked.connect(self.start_sleep_active)
        widgets.start.clicked.connect(self.start_active)
        widgets.pin_btn.clicked.connect(self.start_dialog)
        widgets.button_next.clicked.connect(self.next_active)
        widgets.button_pause.clicked.connect(self.pause_active)
        widgets.check_update.clicked.connect(self.update_active)
        widgets.edit.clicked.connect(self.edit_active)
        widgets.edit_sleep.clicked.connect(self.edit_sleep_active)
        widgets.lock_screen.clicked.connect(lambda: lock_lock(self._pass_remind, nlang))
        widgets.save.clicked.connect(lambda: self.save_active(widgets.chon_bieu_do.currentIndex()))
        widgets.dele.clicked.connect(lambda: self.dele_active(widgets.chon_bieu_do.currentIndex()))
        widgets.shortcut_button.clicked.connect(self.sc_change)

        widgets.work_h.setText(self._time[0][0])
        widgets.work_m.setText(self._time[0][1])
        widgets.work_s.setText(self._time[0][2])
        widgets.relax_h.setText(self._time[1][0])
        widgets.relax_m.setText(self._time[1][1])
        widgets.relax_s.setText(self._time[1][2])

        widgets.wake_h.setText(self._time_sleep[0][0])
        widgets.wake_m.setText(self._time_sleep[0][1])
        widgets.sleep_h.setText(self._time_sleep[1][0])
        widgets.sleep_m.setText(self._time_sleep[1][1])

        widgets.sound_on.setChecked(self._setting_sleep[0])
        widgets.auto_on.setChecked(self._setting_sleep[1])
        widgets.password_on.setChecked(self._setting_sleep[2])
        widgets.sound_on.clicked.connect(self.sound_on_active)
        widgets.auto_on.clicked.connect(self.auto_on_active)
        widgets.password_on.clicked.connect(self.password_on_active)

        widgets.shortcut_button.setText(s)
        widgets.language_combobox.setCurrentIndex(self.lang)

        self.installEventFilter(self)

        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon("logo.ico"))
        self.msg.setWindowTitle("EyeCare")
        self.show() if self._setting[1] else widgets.start.click()
        if self._setting_sleep[1]: widgets.start_sleep.click()

        keyboard.add_hotkey(s, self.hotkey_handler)

    def change_language(self):
        global nlang
        self.translator = QTranslator()
        nlang = self.ui.language_combobox.currentIndex()
        
        QApplication.removeTranslator(self.translator)
        
        self.translator = QTranslator()
        if self.translator.load(f"qrc/translations_{nlang}.qm"):
            QApplication.installTranslator(self.translator)
            widgets.retranslateUi(self)
            self.reload_tray()
        else:
            pass

    def get_init_variable(self):
        self.start = time.time()
        self.edit_sleep_= False
        self.edit_ = False
        self.pause_ = False
        self.start__ = True

        self._time = open_time()
        self._time[0], self._time[1] = [i.zfill(2) for i in self._time[0]], [i.zfill(2) for i in self._time[1]]
        self.lang = nlang
        self._setting, self._pass_remind = open_setting()
        self._time_sleep, self._setting_sleep = open_sleep()
        self.sleep_data = open_sleep_data()
        self._det = open_det()
        self._setting_const = tuple(self._setting.copy())
        self._det_const = tuple(self._det.copy())
        self._pass_const = str(self._pass_remind)
        self._time_sleep_const = tuple(self._time_sleep.copy())
        self._setting_sleep_const = tuple(self._setting_sleep.copy())
        self.days, self.data = open_data()
        self.date_today = time.strftime("%d/%m/%y", time.localtime())
        if self.days is None:
            self.days, self.data = [self.date_today], [0.1]
        self.sleep_list = create_sleep_list(self.sleep_data, self.days)
        self.nsc = s

#MAIN FUNTION
    def sc_change(self):
        widgets.shortcut_button.setStyleSheet("QPushButton{color: rgb(56, 56, 56);background-color: rgb(180, 202, 179);border: 1px soild grey;border-radius: 0px;font: 16pt \"Roboto\"}")
        QApplication.processEvents()
        self.change_hotkey()
    
    def change_hotkey(self):
        hotkey = keyboard.read_hotkey(suppress=False)

        if "+" in hotkey:
            keyboard.clear_all_hotkeys()
            keyboard.add_hotkey(hotkey, self.hotkey_handler)
            cap = hotkey.split('+')
            cap = [i.capitalize() for i in cap]
            hotkey = cap[0] + '+' + cap[1]
            widgets.shortcut_button.setText(hotkey)
            self.nsc = hotkey
        widgets.shortcut_button.setStyleSheet("QPushButton{color: rgb(56, 56, 56);background-color: rgb(220, 222, 220);border: 1px soild grey;border-radius: 0px;font: 16pt \"Roboto\"}")
    
    def start_active(self):
        if self.start__:
            self.time__about = [widgets.work_h.text(), widgets.work_m.text(), widgets.work_s.text()]
            wait_time = [widgets.relax_h.text(), widgets.relax_m.text(), widgets.relax_s.text()]
            for i in range(3):
                if self.time__about[i]=="": self.time__about[i]=0
                else: self.time__about[i]=int(self.time__about[i])
                if wait_time[i]=="": wait_time[i]=0
                else: wait_time[i]=int(wait_time[i])
            tim_cout = 1000*(self.time__about[0]*3600+self.time__about[1]*60+self.time__about[2])
            self.tim_wait = 1000*(wait_time[0]*3600+wait_time[1]*60+wait_time[2])
            if tim_cout == 0 and self.tim_wait == 0:
                self.time__about[0], self.time__about[1], self.time__about[2] = 0, 20, 0
                wait_time[0], wait_time[1], wait_time[2] = 0, 0, 20
                self.active()
            elif tim_cout<10000 or self.tim_wait<10000:
                self.msg.setText(language[nlang][7])
                self.msg.exec()
            elif self.tim_wait>3600000 and not self.isHidden():
                self.msg.setText(language[nlang][8])
                self.msg.exec()
                self.active()
            else: self.active()
        else:
            _temp_pass = False
            if self._setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_==self._pass_remind: _temp_pass = True
                else: self.wrong_password()
            else: _temp_pass = True
            if _temp_pass: self.call_stop()
    def active(self):
        self.start__ = False
        widgets.button_pause.setVisible(True)
        widgets.button_next.setVisible(True)
        widgets.start.setIcon(QIcon(QPixmap("qrc/stop.png")))
        if isPwgsOn:
            Pwgs.pin_start.setIcon(QIcon(QPixmap("qrc/stop.png")))
        self.pause_app = QAction(language[nlang][9])
        self.start_app = QAction(language[nlang][10])
        self.tray_menu.addAction(self.pause_app)
        self.tray_menu.addAction(self.start_app)
        self.pause_app.triggered.connect(self.pause_click)
        self.start_app.triggered.connect(self.start_click)
        self.COUNT = Time_COUNT(self._setting, self._det, self.tim_wait, self.time__about)
        self.COUNT.start()
    def call_stop(self):
        self.COUNT.terminate()
        global pause_
        self.start__, pause_ = True, False
        widgets.button_pause.setVisible(False)
        widgets.button_next.setVisible(False)
        widgets.start.setIcon(QIcon(QPixmap("qrc/start.png")))
        if isPwgsOn:
            Pwgs.pin_start.setIcon(QIcon(QPixmap("qrc/start.png")))
        widgets.button_pause.setIcon(QIcon(QPixmap("qrc/pause.png")))
        self.start_app = QAction(language[nlang][11])
        self.tray_menu.removeAction(self.pause_app)
        self.tray_menu.addAction(self.start_app)
        self.start_app.triggered.connect(self.start_click)
    
    def next_active(self):
        self.call_stop()
        focus(self._setting[3], self._setting[2], self._det, self.tim_wait, nlang)
        self.start_active()

    #JUST A BUTTON
    def pause_active(self):
        global pause_
        if not pause_:
            _temp_pass = False
            if self._setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_==self._pass_remind:  _temp_pass = True
                else: self.wrong_password()
            else: _temp_pass = True
            if _temp_pass:
                widgets.button_pause.setIcon(QIcon(QPixmap("qrc/start.png")))
                if isPwgsOn:
                    Pwgs.pin_start.setIcon(QIcon(QPixmap("qrc/start.png")))
                self.pause_app = QAction(language[nlang][12])
                self.start_app = QAction(language[nlang][13])
                self.tray_menu.addAction(self.pause_app)
                self.tray_menu.addAction(self.start_app)
                self.pause_app.triggered.connect(self.pause_click)
                self.start_app.triggered.connect(self.start_click)
                pause_ = True
        else:
            widgets.button_pause.setIcon(QIcon(QPixmap("qrc/pause.png")))
            if isPwgsOn:
                Pwgs.pin_start.setIcon(QIcon(QPixmap("qrc/stop.png")))
            self.pause_app = QAction(language[nlang][14])
            self.start_app = QAction(language[nlang][15])
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
            if self._setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_==self._pass_remind: _temp_pass = True
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
                self.SLEEP = Time_SLEEP(self._setting_sleep, self._pass_remind, self.sleep_data, self.days, self.date_today, self.sleep_list)
                self.SLEEP.start()
                widgets.start_sleep.setIcon(QIcon(QPixmap("qrc/stop.png")))
                __sleep_start__ = False
            else:
                self.msg.setText(language[nlang][16])
                self.msg.exec()
        else:
            _temp_pass = False
            if self._setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_==self._pass_remind: _temp_pass = True
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
            if self._setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_==self._pass_remind: _temp_pass = True
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
        if self._setting_sleep[0] == 0:
            self._setting_sleep[0] = 1
        else:
            if self._setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_==self._pass_remind:
                    self._setting_sleep[0] = 0
                else:
                    widgets.sound_on.setChecked(True)
                    self.wrong_password()
            else:
                self._setting_sleep[0] = 0
    def auto_on_active(self):
        if self._setting_sleep[1] == 0:
            self._setting_sleep[1] = 1
        else:
            if self._setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_==self._pass_remind:
                    self._setting_sleep[1] = 0
                else:
                    widgets.auto_on.setChecked(True)
                    self.wrong_password()
            else:
                self._setting_sleep[1] = 0
    def password_on_active(self):
        if self._setting_sleep[2] == 0:
            self._setting_sleep[2] = 1
        else:
            if self._setting[4]:
                self._pass = GET_PASS(self)
                self._pass.exec()
                if self._pass._pass_check_==self._pass_remind:
                    self._setting_sleep[2] = 0
                else:
                    widgets.password_on.setChecked(True)
                    self.wrong_password()
            else:
                self._setting_sleep[2] = 0

#CHART
    def bieu_do(self, num):
        text = widgets.chon_bieu_do.currentText()
        gio = QBarSet(text[:6])
        gio.setColor(QColor(13, 166, 244))
        if not num: data_temp = self.data
        elif num==1: data_temp = [i*60 for i in self.data]
        else:
            gio = QBarSet(language[nlang][17])
            gio.setColor(QColor(198, 66, 86))
            data_temp = self.sleep_list
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
        axisY.append(self.days)
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
                for i, j in zip(self.days, self.data):
                    temp = f"{i} {j:.3f}\n"
                    st+=temp
            elif num==1:
                for i, j in zip(self.days, [i*60 for i in self.data]):
                    temp = f"{i} {j:.3f}\n"
                    st+=temp
            elif num==2:
                st = "Sleep Fail\n"
                for i in self.sleep_data:
                    st+=(i+"\n")
            write_chart_file(name[0], st)
            self.msg.setText(language[nlang][18])
            self.msg.exec()
    def dele_active(self, num):
        if self.areusure():
            if num!=2:
                self.days, self.data = [self.date_today], [0.1]
            else:
                self.sleep_data, self.sleep_list = [], []
            self.bieu_do(num)

#SETTING
    def set_setting_open(self):
        _temp_pass = False
        if self._setting[4]:
            self._pass = GET_PASS(self)
            self._pass.exec()
            if self._pass._pass_check_==self._pass_remind: _temp_pass = True
            else: self.wrong_password()
        else: _temp_pass = True
        if _temp_pass: widgets.Page_Stack.setCurrentIndex(3)
    def open_with_active(self):
        if self._setting[1]: self._setting[1] = 0
        else: self._setting[1] = 1
    def sound_active(self):
        if self._setting[2]: self._setting[2] = 0
        else: self._setting[2] = 1
    def picture_active(self):
        if self._setting[3]: self._setting[3] = 0
        else: self._setting[3] = 1
    def password_active(self):
        if self._setting[4]:
            self._pass = GET_PASS(self)
            self._pass.exec()
            if self._pass._pass_check_==self._pass_remind:
                self._setting[4] = 0
            else:
                widgets.password.setChecked(True)
                self.wrong_password()
        else:
            self._setting[4] = 1
    def start_with_active(self):
        if self._setting[0]:
            self._setting[0] = 0
            delete_file("Microsoft//Windows//Start Menu//Programs//Startup//EyeCare.lnk")
        else:
            if create_shortcut(f'C://Users//{user}//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup', "EyeCare.lnk"):
                self._setting[0] = 1
            else:
                widgets.start_with.setChecked(False)
    def file_edit_active(self):
        dirr = self._det[0]
        name = QFileDialog.getOpenFileName(parent = None, caption = 'File Selected', directory = dirr, filter ="Pictures (*.jpg *.png *.bmp)")
        if name != ('', ''):
            self._setting[3] = 1
            self._det[0] = name[0]
            widgets.text_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(191, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
            widgets.file_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(101, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
    def text_edit_active(self):
        self._word = GET_WORD(self, self._det[1])
        self._word.exec()
        if self._word._word_check_ == '':
            self._setting[3] = 2
            widgets.file_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(191, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
            widgets.text_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(101, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
        elif self._word._word_check_ != None:
            self._setting[3] = 2
            self._det[1] = self._word._word_check_
            widgets.file_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(191, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
            widgets.text_edit.setStyleSheet("QPushButton{color:rgb(56, 56, 56);background-color:rgb(101, 191, 191);border: 1px soild grey;border-radius: 5px;font:11pt \"Roboto\"}QPushButton:hover{background-color:rgb(211, 211, 211)}")
    def password_edit_active(self):
        self._pass = GET_PASS(self)
        self._pass.exec()
        if self._pass._pass_check_==self._pass_remind:
            _change_pass = GET_PASS(self, language[nlang][19])
            _change_pass.exec()
            _pass_temp_ = str(_change_pass._pass_check_)
            if _pass_temp_ == None or _pass_temp_ == "":
                self.msg.setText(language[nlang][20])
                self.msg.exec()
                return
            _change_pass_check = GET_PASS(self, language[nlang][21])
            _change_pass_check.exec()
            if _pass_temp_ == str(_change_pass_check._pass_check_):
                pass
            else:
                _change_pass_check = GET_PASS(self, language[nlang][22])
                while _pass_temp_ != str(_change_pass_check._pass_check_):
                    _change_pass_check._pass_check_ = None
                    _change_pass_check.exec()
                    if _change_pass_check._pass_check_ == None:
                        self.msg.setText(language[nlang][23])
                        self.msg.exec()
                        return
            self._pass_remind = str(_pass_temp_)
            self.msg.setText(language[nlang][24])
            self.msg.exec()
        else:
            self.wrong_password()

#ANOTHER
    def wrong_password(self):
        self.msg.setText(language[nlang][25])
        self.msg.exec()
    def update_active(self):
        self.update_thread = UpdateCheckThread()
        widgets.check_update.setStyleSheet("QPushButton{color: rgb(56, 56, 56);background-color: rgb(255, 245, 105);border: 1px soild grey;border-radius: 5px;font: 13pt \"Roboto Medium\"}")
        self.update_thread.update_result.connect(self.show_update_result)
        self.update_thread.start()
    def show_update_result(self, message):
        if message == language[nlang][26]:
            playsound('sound//bell.wav', block=False)
        self.msg.setText(message)
        self.msg.exec()
        widgets.check_update.setStyleSheet("QPushButton{color: rgb(56, 56, 56);background-color: rgb(255, 255, 155);border: 1px soild grey;border-radius: 5px;font: 13pt \"Roboto Medium\"}QPushButton:hover{background-color: rgb(255, 245, 105)}")
    def areusure(self):
        box = QMessageBox()
        box.setWindowTitle('EyeCare')
        box.setWindowIcon(QIcon("logo.ico"))
        box.setIconPixmap(QIcon("qrc/bird.png").pixmap(35, 35))
        box.setText(language[nlang][29])
        box.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        buttonY = box.button(QMessageBox.StandardButton.Yes)
        buttonY.setText(language[nlang][30])
        buttonN = box.button(QMessageBox.StandardButton.No)
        buttonN.setText(language[nlang][31])
        box.exec()
        if box.clickedButton() == buttonY:
            return True
        return False

#EVENT
    def hotkey_handler(self):
        playsound('sound//bell.wav', block=False)
        widgets.start.click()
    
    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if self.isMinimized():
                self.hide()
        return False
    def closeEvent(self, event):
        if self._setting[4]:
            self.show_eyecare()
            event.ignore()
            _temp_pass = False
            _pass = GET_PASS(self)
            _pass.exec()
            if _pass._pass_check_ == self._pass_remind:
                _temp_pass = True
            else:
                self.wrong_password()
        else:
            _temp_pass = True

        if _temp_pass:
            self._time_const = ((widgets.work_h.text(), widgets.work_m.text(), widgets.work_s.text()),
                                (widgets.relax_h.text(), widgets.relax_m.text(), widgets.relax_s.text()))
            self._sleep_const = ((widgets.wake_h.text(), widgets.wake_m.text()),
                                 (widgets.sleep_h.text(), widgets.sleep_m.text()))
            
            if self.lang != nlang or s != self.nsc:
                write_two_file(user, 'un', self.nsc, nlang)
            if self._setting_const != tuple(self._setting) or self._pass_const != self._pass_remind:
                write_two_file(user, "setting", " ".join([str(i) for i in self._setting]), self._pass_remind)
            if self._time_const != tuple(self._time):
                write_two_file(user, "time", " ".join([i for i in self._time_const[0]]), " ".join([str(i) for i in self._time_const[1]]))
            if self._det_const != tuple(self._det):
                write_two_file(user, "det", self._det[0], self._det[1])
            if self._setting_sleep_const != tuple(self._setting_sleep) or self._sleep_const != tuple(self._time_sleep):
                temp = []
                for i in self._sleep_const:
                    temp.append(i[0])
                    temp.append(i[1])
                write_sleep_data(user, "sleep", temp + [str(i) for i in self._setting_sleep])

            end = time.time()
            time_use = (end - self.start) / 3600
            try:
                if self.days[-1] == self.date_today:
                    time_use = "{:0.6f}".format(time_use + self.data[-1])
                    self.data[-1] = time_use
                else:
                    self.days.append(self.date_today)
                    self.data.append("{:0.6f}".format(time_use))
            except:
                self.days.append(self.date_today)
                self.data.append("{:0.6f}".format(time_use))
            self.data = [str(i) for i in self.data]
            write_data(user, self.days[len(self.days)-7:], self.data[len(self.data)-7:])

            event.accept()


    def show_eyecare(self):
        self.show()
        if self.isMinimized():
            self.showNormal()
    def start_dialog(self):
        if isPwgsOn:
            self.diaLog.close()
            widgets.pin_btn.setIcon(QIcon("qrc/pin.png"))
        else:
            self.diaLog = DialogFunc(self, self.start__)
            widgets.pin_btn.setIcon(QIcon("qrc/unpin.png"))

#TRAY ICON
    def start_click(self):
        if self._setting[4] and not self.start__: self.show_eyecare()
        self.start_active()
    def pause_click(self):
        self.show_eyecare()
        self.pause_active()
    def tray_icon(self):
        def _show(reason): #Show the app
            if reason == self.tray.ActivationReason.Trigger: self.show_eyecare()
        self.tray_menu = QMenu()
        self.show_app = QAction(language[nlang][32])
        self.hide_app = QAction(language[nlang][33])
        self.quit_app = QAction(language[nlang][35])
        self.start_app = QAction(language[nlang][34])
        self.show_app.triggered.connect(self.show_eyecare)
        self.hide_app.triggered.connect(self.hide)
        self.quit_app.triggered.connect(self.close_app)
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
    def reload_tray(self):
        self.tray_menu.removeAction(self.show_app)
        self.tray_menu.removeAction(self.hide_app)
        self.tray_menu.removeAction(self.quit_app)
        self.tray_menu.removeAction(self.start_app)
        self.show_app = QAction(language[nlang][32])
        self.hide_app = QAction(language[nlang][33])
        self.quit_app = QAction(language[nlang][35])
        self.start_app = QAction(language[nlang][34])
        self.show_app.triggered.connect(self.show_eyecare)
        self.hide_app.triggered.connect(self.hide)
        self.quit_app.triggered.connect(self.close_app)
        self.start_app.triggered.connect(self.start_click)
        self.tray_menu.addAction(self.show_app)
        self.tray_menu.addAction(self.hide_app)
        self.tray_menu.addAction(self.quit_app)
        self.tray_menu.addAction(self.start_app)

        if not self.start__:
            self.pause_app = QAction(language[nlang][12])
            self.start_app = QAction(language[nlang][13])
            self.tray_menu.addAction(self.pause_app)
            self.tray_menu.addAction(self.start_app)
            self.pause_app.triggered.connect(self.pause_click)
            self.start_app.triggered.connect(self.start_click)
    
    def close_app(self):
        self.show_eyecare()
        self.close()

pause_, __sleep_start__  = False, True

app = QApplication(sys.argv)
ui = Main_APP()
app.exec()
