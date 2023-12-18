# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowPyVPfE.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMdiArea, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew_Window = QAction(MainWindow)
        self.actionNew_Window.setObjectName(u"actionNew_Window")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionName_Folder = QAction(MainWindow)
        self.actionName_Folder.setObjectName(u"actionName_Folder")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionClose.triggered.connect(self.close)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")

        self.verticalLayout.addWidget(self.mdiArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew_Window)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionName_Folder)
        self.menuFile.addAction(self.actionClose)
        self.toolBar.addAction(self.actionNew_Window)
        self.toolBar.addAction(self.actionName_Folder)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_Window.setText(QCoreApplication.translate("MainWindow", u"New Window", None))
#if QT_CONFIG(tooltip)
        self.actionNew_Window.setToolTip(QCoreApplication.translate("MainWindow", u"New Window", None))
#endif // QT_CONFIG(tooltip)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionName_Folder.setText(QCoreApplication.translate("MainWindow", u"Name Folder", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

