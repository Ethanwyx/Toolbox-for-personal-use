# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toolbox.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(522, 303)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menuList = QListWidget(self.centralwidget)
        QListWidgetItem(self.menuList)
        QListWidgetItem(self.menuList)
        self.menuList.setObjectName(u"menuList")

        self.horizontalLayout.addWidget(self.menuList, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_subtitle = QWidget()
        self.page_subtitle.setObjectName(u"page_subtitle")
        self.verticalLayout_subtitle = QVBoxLayout(self.page_subtitle)
        self.verticalLayout_subtitle.setObjectName(u"verticalLayout_subtitle")
        self.btn_select_subtitle = QPushButton(self.page_subtitle)
        self.btn_select_subtitle.setObjectName(u"btn_select_subtitle")

        self.verticalLayout_subtitle.addWidget(self.btn_select_subtitle)

        self.txt_output_subtitle = QTextEdit(self.page_subtitle)
        self.txt_output_subtitle.setObjectName(u"txt_output_subtitle")

        self.verticalLayout_subtitle.addWidget(self.txt_output_subtitle, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_select_output_subtitle = QPushButton(self.page_subtitle)
        self.btn_select_output_subtitle.setObjectName(u"btn_select_output_subtitle")

        self.verticalLayout_subtitle.addWidget(self.btn_select_output_subtitle)

        self.btn_convert_subtitle = QPushButton(self.page_subtitle)
        self.btn_convert_subtitle.setObjectName(u"btn_convert_subtitle")

        self.verticalLayout_subtitle.addWidget(self.btn_convert_subtitle)

        self.stackedWidget.addWidget(self.page_subtitle)
        self.page_mp4 = QWidget()
        self.page_mp4.setObjectName(u"page_mp4")
        self.verticalLayout_mp4 = QVBoxLayout(self.page_mp4)
        self.verticalLayout_mp4.setObjectName(u"verticalLayout_mp4")
        self.btn_select_mp4 = QPushButton(self.page_mp4)
        self.btn_select_mp4.setObjectName(u"btn_select_mp4")

        self.verticalLayout_mp4.addWidget(self.btn_select_mp4)

        self.txt_output_mp4 = QTextEdit(self.page_mp4)
        self.txt_output_mp4.setObjectName(u"txt_output_mp4")

        self.verticalLayout_mp4.addWidget(self.txt_output_mp4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.btn_select_output_mp3 = QPushButton(self.page_mp4)
        self.btn_select_output_mp3.setObjectName(u"btn_select_output_mp3")

        self.verticalLayout_mp4.addWidget(self.btn_select_output_mp3)

        self.btn_convert_mp4 = QPushButton(self.page_mp4)
        self.btn_convert_mp4.setObjectName(u"btn_convert_mp4")

        self.verticalLayout_mp4.addWidget(self.btn_convert_mp4)

        self.progress_mp4 = QProgressBar(self.page_mp4)
        self.progress_mp4.setObjectName(u"progress_mp4")
        self.progress_mp4.setValue(0)

        self.verticalLayout_mp4.addWidget(self.progress_mp4, 0, Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget.addWidget(self.page_mp4)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\u7bb1", None))

        __sortingEnabled = self.menuList.isSortingEnabled()
        self.menuList.setSortingEnabled(False)
        ___qlistwidgetitem = self.menuList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u5e55\u8f6c\u7eaf\u6587\u672c", None));
        ___qlistwidgetitem1 = self.menuList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"MP4 \u8f6c MP3", None));
        self.menuList.setSortingEnabled(__sortingEnabled)

        self.btn_select_subtitle.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5b57\u5e55\u6587\u4ef6", None))
        self.btn_select_output_subtitle.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f93\u51fa\u8def\u5f84", None))
        self.btn_convert_subtitle.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
        self.btn_select_mp4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9 MP4 \u6587\u4ef6", None))
        self.btn_select_output_mp3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f93\u51fa\u8def\u5f84", None))
        self.btn_convert_mp4.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
    # retranslateUi

