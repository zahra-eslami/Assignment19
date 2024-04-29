import numpy as np
import sys
import random
from functools import partial

from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QTimer, QTime, QFile
from my_puzzle15 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.array=[]
        self.array_size=16
        

        self.buttons = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3,self.ui.btn_4],
           [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7,self.ui.btn_8],
           [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11,self.ui.btn_12],
           [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15,self.ui.btn_16]]
    
        # self.create_random_number()
        
    def create_random_number(self):
        while self.array_size!= len(self.array):
            x = random.randint(1,16)
            if x not in self.array:
                self.array.append(x)
        
        self.array = np.array(self.array).reshape(4, 4)

        for i in range(4):
            for j in range(4):
                r=self.array[i][j]
                self.buttons[i][j].setText(str(r))

                self.buttons[i][j].clicked.connect(partial(self.play,i,j))

                if r == 16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_i = i
                    self.empty_j = j


    def play(self, i ,j):
        # print(i,j)
         
        if (i == self.empty_i and abs(j - self.empty_j )== 1) or (j == self.empty_j and abs(i - self.empty_i ) == 1):

            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")

            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setVisible(False)

            self.empty_i = i
            self.empty_j = j

        if self.check_win() == True:
            msg_box=QMessageBox()
            msg_box.setText("you win the game(●'◡'●)")
            msg_box.exec_()


    def check_win(self):
        index = 1 
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                else:
                    index += 1
   
        return True
    
    def display_timer(self):
        global elapsed_time
        if not paused:
            elapsed_time = elapsed_time.addSecs(1)
            formatted_time = elapsed_time.toString("hh:mm:ss")
            self.ui.lineEdit.setText(formatted_time)


    def toggle_timer(self):
        global paused
        paused = not paused
        if paused:
            timer.stop()
        else:
            timer.start()


    def reset_timer(self):
        global elapsed_time

        elapsed_time = QTime(0, 0)
        formatted_time = elapsed_time.toString("hh:mm:ss")

        self.ui.lineEdit.setText(formatted_time)
        if not paused:
            timer.start()
        
            # self.create_random_number()
        

    def show_game_info(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("اطلاعات بازی")
        msg_box.setText("این بازی یک نسخه از بازی پازل 15 است. هدف این بازی این است که اعداد را به ترتیب از 1 تا 15 مرتب کنید. \n این بازی توسط زهرا اسلامی طراحی شده است..")
        msg_box.exec_()

    def reset_game(self):
        self.array = [] 
        self.buttons[self.empty_i][self.empty_j].setVisible(True)
        self.empty_i = None
        self.empty_j = None
        self.create_random_number() 
        self.reset_timer()


my_app = QApplication(sys.argv)

my_window = MainWindow()

my_window.show()

button_size = my_window.ui.btn_pause.size()
icon_size = QSize(button_size.width() - 10, button_size.height() - 10)

my_window.ui.btn_pause.setIconSize(icon_size)

my_window.ui.btn_pause.setIcon(QIcon("Puzzle15/pic/pause.png"))
my_window.ui.btn_info.setIconSize(icon_size)
my_window.ui.btn_info.setIcon(QIcon("Puzzle15/pic/info.png"))
my_window.ui.btn_new.setIconSize(icon_size)
my_window.ui.btn_new.setIcon(QIcon("Puzzle15/pic/new.png"))
my_window.ui.btn_close.setIconSize(icon_size)
my_window.ui.btn_close.setIcon(QIcon("Puzzle15/pic/close.png"))

elapsed_time = QTime(0, 0)
paused = False

timer = QTimer()
timer.timeout.connect(my_window.display_timer)
timer.start(1000)

my_window.create_random_number()

my_window.ui.btn_pause.clicked.connect(my_window.toggle_timer)
# my_window.ui.btn_new.clicked.connect(my_window.reset_timer)
my_window.ui.btn_info.clicked.connect(my_window.show_game_info)
my_window.ui.btn_new.clicked.connect(my_window.reset_game)
my_window.ui.btn_close.clicked.connect(my_window.close)


my_app.exec()

