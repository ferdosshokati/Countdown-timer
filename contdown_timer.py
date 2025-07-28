from PyQt5.QtWidgets import QLineEdit,QLCDNumber,QLabel,QApplication,QMainWindow,QPushButton
import os,sys
from PyQt5.QtCore import QTime , QTimer

from PyQt5 import uic

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('Countdown.ui',self)

        # Define Widgets
        self.label = self.findChild(QLabel,'label')
        self.label_2 = self.findChild(QLabel,'label_2')
        self.hour = self.findChild(QLineEdit,'lineEdit_h')
        self.minute = self.findChild(QLineEdit,'lineEdit_m')
        self.lcd = self.findChild(QLCDNumber,'lcdNumber')
        self.startButton = self.findChild(QPushButton,'pushButton_start')
        self.stopButton = self.findChild(QPushButton,'pushButton_stop')
        self.clearButton = self.findChild(QPushButton,'pushButton_clear')
        # تغییراتی بایداعمال شود

        # connect button
        self.startButton.clicked.connect(self.start_timer)
        self.stopButton.clicked.connect(self.stop_timer)
        self.clearButton.clicked.connect(self.clear_timer)
        self.show()


        # Creat Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.count_timer)
        self.remaining_time = 0
    def stop_timer(self):
        self.timer.stop()
    def clear_timer(self):
        self.remaining_time = 0
        self.lcd.display("00:00:00")
        self.hour.setText("")
        self.minute.setText("")

    def start_timer(self):
        try:
            h = int(self.hour.text())
            m = int(self.minute.text())
        except ValueError:
            return
        self.remaining_time = h * 3600 + m * 60

        if self.remaining_time > 0 :
            self.timer.start(1000)
        print("start")

    def count_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            h = self.remaining_time // 3600
            m = (self.remaining_time % 3600) // 60
            s = self.remaining_time % 60
            self.lcd.setDigitCount(8)
            self.lcd.display(f"{h:02d}:{m:02d}:{s:02d}")

        else:
            self.timer.stop()









os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"F:\aferdos\پایتون\GUI\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms"
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
