import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QMdiArea, QMdiSubWindow, QTextEdit, QToolBar, QStatusBar

#TRIED ADDING STATUS BAR

class Ui_Window(QMainWindow):
    count = 0

    def __init__(self):
        super().__init__()
        self.MDI = QMdiArea()
        self.setCentralWidget(self.MDI)
        self.setWindowTitle("MainWindow")
        menu = self.menuBar()
        file = menu.addMenu("File")

        new = file.addAction("New")
        new.triggered.connect(self.New_Window)

        close = file.addAction("Close")
        close.triggered.connect(self.close)

        out = menu.addAction("Quit")
        out.triggered.connect(self.close)

        self.show()

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        new_window = toolbar.addAction("New Window")
        new_window.triggered.connect(self.New_Window)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def New_Window(self):
        Ui_Window.count = Ui_Window.count + 1
        sub_window = QMdiSubWindow()
        sub_window.setWidget(QTextEdit())
        sub_window.setWindowTitle(f"Sub Window{Ui_Window.count}.txt")
        self.MDI.addSubWindow(sub_window)
        self.statusBar.showMessage("To Add New Sub Window", 3000)
        self.statusBar.show()
        sub_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_Window()
    window.resize(800,600)
    sys.exit(app.exec())

