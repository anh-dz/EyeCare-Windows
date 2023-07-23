from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from time import sleep
from Model.maindata import *
# from Control.notify import *
#from Control.lockscreen import focus, lock_lock
from main import *

class sleepCount(QThread):
    def run(self):
        self.hour_wake = int(widgets.wakehInput.text())
        self.min_wake = int(widgets.wakemInput.text())
        self.hour_sleep = int(widgets.sleephInput.text())+12
        self.min_sleep = int(widgets.sleepmInput.text())
        self.local_time = time.localtime()
        time_left = self.sleep_count()
        while sleepCountActive:
            self.sleep_check(time_left)
            # if time_left == 15: Notifi().show_toast("Còn 15p nữa là đến giờ đi ngủ!!")
            # elif time_left == 5: Notifi().show_toast("Còn 5p nữa là đến giờ đi ngủ! Lưu lại công việc và thư giãn nào")
            # elif time_left == 1: Notifi().show_toast("Còn 1 nữa là đến giờ đi ngủ! Chúc ngủ ngon nha <3")
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

class Control:
    startStop = True

    def __init__(self, widgets: ViewControl):
        self.widgets = widgets
        self.workData = workData.copy()

        self.setupVar()

        self.widgets.left1.clicked.connect(lambda: self.widgets.page.setCurrentIndex(0))
        self.widgets.left2.clicked.connect(lambda: self.widgets.page.setCurrentIndex(1))
        self.widgets.left3.clicked.connect(lambda: self.widgets.page.setCurrentIndex(2))
        self.widgets.left4.clicked.connect(lambda: self.widgets.page.setCurrentIndex(3))
        self.widgets.left5.clicked.connect(lambda: self.widgets.page.setCurrentIndex(4))

        self.widgets.startMain.clicked.connect(self.startMain_active)
        self.widgets.btnRestart.clicked.connect(self.btnRestart_active)
        self.widgets.btnLock.clicked.connect(self.btnLock_active)

    #Setup
    def setupVar(self):
        self.widgets.timeChange.setText(f"{str(self.workData[0]).zfill(2)}:{str(self.workData[1]).zfill(2)}:{str(self.workData[2]).zfill(2)}")

    def setupDataRelax(self):
        self.relaxTime = workRelax[0]*3600+workRelax[1]*60+workRelax[2]*1000

    # Main
    def timeUpdate(self):
        if self.workData[2] > 0:
            self.workData[2] -= 1
        elif self.workData[1] > 0:
            self.workData[1] -= 1
            self.workData[2] = 59
        else:
            self.workData[0] -= 1
            self.workData[1] = 59
            self.workData[2] = 59
        if self.workData[2] == notiSec and self.workData[1] == 0 and self.workData[0] == 0:
            Notifi().show_toast("Chuẩn bị nghỉ ngơi, nhớ save công việc lại nha <3")
        if self.workData[2] == 0 and self.workData[1] == 0 and self.workData[0] == 0:
            #focus(setting['fileText'], setting['sound'], fileText, self.relaxTime)
            self.workData = workData.copy()
            self.setupVar()
        self.widgets.timeChange.setText(f"{str(self.workData[0]).zfill(2)}:{str(self.workData[1]).zfill(2)}:{str(self.workData[2]).zfill(2)}")

    def btnRestart_active(self):
        if self.areusure():
            self.workData = workData.copy()
            self.setupVar()

    def btnLock_active(self):
        pass
        #lock_lock(password)

    def startMain_active(self):
        if self.startStop:
            self.widgets.startMain.setIcon(QIcon(QPixmap("qrc/stop.png")))
            self.timer = QTimer()
            self.timer.timeout.connect(self.timeUpdate)
            self.timer.start(1000)
            self.setupDataRelax()
            self.startStop = False
        else:
            self.widgets.startMain.setIcon(QIcon(QPixmap("qrc/start.png")))
            self.timer.stop()
            self.startStop = True

    #Other
    def areusure(self):
        box = QMessageBox()
        box.setWindowTitle('EyeCare')
        box.setWindowIcon(QIcon("logo.ico"))
        box.setIconPixmap(QIcon("qrc/bird.png").pixmap(35, 35))
        box.setText('Bạn có chắc chắn?')
        box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        buttonY = box.button(QMessageBox.StandardButton.Yes)
        buttonY.setText('Có')
        buttonN = box.button(QMessageBox.StandardButton.No)
        buttonN.setText('Không')
        box.exec()
        if box.clickedButton() == buttonY:
            return True
        return False
