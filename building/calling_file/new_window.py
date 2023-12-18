from PySide6.QtWidgets import QWidget, QApplication
from ui_new_window import Ui_Form
import sys

class New_Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app_new = QApplication(sys.argv)
    new = New_Window()
    new.show()
    sys.exit(app_new.exec())