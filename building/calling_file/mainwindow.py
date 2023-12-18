from PySide6.QtWidgets import QWidget, QMainWindow, QMdiSubWindow, QTextEdit
from ui_mainwindow import Ui_MainWindow
from new_window import New_Window
class MainWindow(QMainWindow, Ui_MainWindow):
    count = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionNew_Window.triggered.connect(self.new_folder)
        self.actionOpen.triggered.connect(self.open)
        self.actionName_Folder.triggered.connect(self.name_folder)

    def new_folder(self):
        print("hello, adding new window")
        MainWindow.count = MainWindow.count + 1
        subby = QMdiSubWindow()
        subby.setWidget(QTextEdit())
        self.mdiArea.addSubWindow(subby)
        subby.show()

    def open(self):
        print("Open folder")

    def name_folder(self):
        print("exsiting folder will show up")
        self.new = New_Window()
        self.new_widget = QWidget()
        self.new.setupUi(self.new_widget)
        self.mdiArea.addSubWindow(self.new_widget)
        self.new_widget.show()
