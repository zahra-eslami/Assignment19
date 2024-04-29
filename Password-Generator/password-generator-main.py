
import sys
import random

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from my_pass import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.ui.h_Slider.setMinimum(6)
        self.ui.h_Slider.setMaximum(20)

        self.ui.chB_upper.stateChanged.connect(self.generate_random_string)
        self.ui.chB_lower.stateChanged.connect(self.generate_random_string)
        self.ui.chB_nums.stateChanged.connect(self.generate_random_string)
        self.ui.chB_chr.stateChanged.connect(self.generate_random_string)
        self.ui.h_Slider.valueChanged.connect(self.generate_random_string)  
        self.ui.h_Slider.setValue(6)  
        self.generate_random_string()

        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)

    def update_slider_value(self, value):
        self.ui.lbl_length.setText(str(value))
        self.generate_random_string(value)

    def generate_random_string(self):

        checked_count = sum([self.ui.chB_upper.isChecked(),
                    self.ui.chB_lower.isChecked(),
                    self.ui.chB_nums.isChecked(),
                    self.ui.chB_chr.isChecked()])
                

        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if self.ui.chB_upper.isChecked() else ''
        lower_case = 'abcdefghijklmnopqrstuvwxyz' if self.ui.chB_lower.isChecked() else ''
        numbers = '0123456789' if self.ui.chB_nums.isChecked() else ''
        special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/' if self.ui.chB_chr.isChecked() else ''

        all_chars = upper_case + lower_case + numbers + special_chars

        if not all_chars:
            all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        password_length = self.ui.h_Slider.value()
        random_password = ''.join(random.choices(all_chars, k=password_length))

        self.ui.lineEdit.setText(random_password)

        # if any(c.isupper() for c in random_password) and \
        #    any(c.islower() for c in random_password) and \
        #    any(c.isdigit() for c in random_password) and \
        #    any(c in special_chars for c in random_password):
        #     password_strength = 'STRONG'

        password_strength = 'WEAK'

        if checked_count == 4:
            password_strength = 'STRONG'

        elif checked_count == 1 or (any(c.islower() for c in random_password) and \
                                    any(c.isdigit() for c in random_password) and checked_count == 2):
            password_strength = 'WEAK'
        
        else:
            password_strength ='AVERAGE'

        self.ui.lbl_msg.setText(f" * YOU CREATE A {password_strength} PASSWORD")


    
    def copy_to_clipboard(self):
        msg_box=QMessageBox()
        msg_box.setText("your password copy to clipboard (●'◡'●)")
        msg_box.exec()

        text = self.ui.lineEdit.text()

        clipboard = QApplication.clipboard()
        clipboard.setText(text)

my_app = QApplication(sys.argv)
my_window = MainWindow()
my_window.ui.chB_lower.setChecked(True)

my_window.show()
my_app.exec()
