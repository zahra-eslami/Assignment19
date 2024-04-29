import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from line_removal import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.ui.btn_remove_line.clicked.connect(self.remove_empty_lines)
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)
        self.ui.btn_reset.clicked.connect(self.reset_text)

    def remove_empty_lines(self):

        if self.ui.r_btn_line.isChecked():

            input_text = self.ui.txt_input.toPlainText()
            
            lines = input_text.split('\n')
            non_empty_lines = [line for line in lines if line.strip()]
            output_text = ' '.join(non_empty_lines)  


            # self.ui.txt_result.setPlainText(output_text)

        elif self.ui.r_btn_paragraph.isChecked():

            input_text = self.ui.txt_input.toPlainText()

            paragraphs = input_text.split('\n\n')
            cleaned_paragraphs = []
            for paragraph in paragraphs:
                lines = paragraph.split('\n')
                non_empty_lines = [line for line in lines if line.strip()]
                cleaned_paragraphs.append(' '.join(non_empty_lines))

            output_text = '\n\n'.join(cleaned_paragraphs)

        self.ui.txt_result.setPlainText(output_text)

    def copy_to_clipboard(self):
        msg_box=QMessageBox()
        msg_box.setText("Your text has been copied to the clipboard")
        msg_box.exec()

        text = self.ui.txt_result.toPlainText()

        clipboard = QApplication.clipboard()
        clipboard.setText(text)

    def reset_text(self):
        self.ui.txt_input.clear()
        self.ui.txt_result.clear()

app = QApplication(sys.argv)
my_window = MainWindow()
my_window.show()

my_window.ui.r_btn_line.setChecked(True)

sys.exit(app.exec())
