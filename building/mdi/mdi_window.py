from PySide6.QtWidgets import QMainWindow, QApplication,QToolBar, QMdiArea, QMdiSubWindow, QTextEdit
from PySide6.QtCore import QSize
import sys


class Ui_Mainwindow(QMainWindow):
    count = 0

    def __init__(self):
        super().__init__()
        self.mdi_window = QMdiArea()
        self.setCentralWidget(self.mdi_window)
        self.setWindowTitle("Window_1")
        menu = self.menuBar()

        file = menu.addMenu("File")
        new = file.addAction("Some Action")
        new.triggered.connect(self.New_action)

        toolbar = QToolBar("Close")
        toolbar.setIconSize(QSize(16,16))

        self.addToolBar(toolbar)
        close = toolbar.addAction("Close")
        close.triggered.connect(self.close)

        sub_window = toolbar.addAction("New Window")
        sub_window.triggered.connect(self.New_Window)


    def New_action(self):
        print("clicked")

    def New_Window(self):
        Ui_Mainwindow.count = Ui_Mainwindow.count + 1
        sub_window = QMdiSubWindow()
        sub_window.setWidget(QTextEdit())
        sub_window.setWindowTitle(f"New Sub Window {Ui_Mainwindow.count}.txt")
        self.mdi_window.addSubWindow(sub_window)
        sub_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_Mainwindow()
    window.resize(500,400)
    window.show()
    sys.exit(app.exec())