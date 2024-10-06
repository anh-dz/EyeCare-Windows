from PyQt6.QtCore import QThread, Qt, QUrl, QEvent, QTranslator
from PyQt6.QtGui import QIcon, QPixmap, QAction, QDesktopServices
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QFileDialog, QMessageBox, QMainWindow, QPushButton
from PyQt6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from urllib.request import urlopen
from playsound import playsound
import time

from . ui_main import *
from . ui_pin import Ui_Dialog
from . readed import open_time, open_un, open_setting, open_sleep, open_sleep_data, open_det, open_data, delete_file, user
from . endl import write_sleep_data, write_chart_file, write_data, write_two_file
from . password_input import GET_PASS, GET_WORD
from . notifi import Notifi, focus, lock_lock, sleep_lock, lang_focus
from . other import create_shortcut, create_sleep_list