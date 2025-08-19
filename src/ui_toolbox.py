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
        MainWindow.resize(780, 520)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_root = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_root.setSpacing(8)
        self.horizontalLayout_root.setObjectName(u"horizontalLayout_root")
        self.horizontalLayout_root.setContentsMargins(8, 8, 8, 8)
        self.menuList = QListWidget(self.centralwidget)
        QListWidgetItem(self.menuList)
        QListWidgetItem(self.menuList)
        QListWidgetItem(self.menuList)
        self.menuList.setObjectName(u"menuList")
        self.menuList.setMinimumWidth(160)
        self.menuList.setMaximumWidth(220)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuList.sizePolicy().hasHeightForWidth())
        self.menuList.setSizePolicy(sizePolicy)

        self.horizontalLayout_root.addWidget(self.menuList)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_subtitle = QWidget()
        self.page_subtitle.setObjectName(u"page_subtitle")
        self.verticalLayout_subtitle = QVBoxLayout(self.page_subtitle)
        self.verticalLayout_subtitle.setSpacing(8)
        self.verticalLayout_subtitle.setObjectName(u"verticalLayout_subtitle")
        self.btn_select_subtitle = QPushButton(self.page_subtitle)
        self.btn_select_subtitle.setObjectName(u"btn_select_subtitle")

        self.verticalLayout_subtitle.addWidget(self.btn_select_subtitle)

        self.txt_output_subtitle = QTextEdit(self.page_subtitle)
        self.txt_output_subtitle.setObjectName(u"txt_output_subtitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.txt_output_subtitle.sizePolicy().hasHeightForWidth())
        self.txt_output_subtitle.setSizePolicy(sizePolicy1)

        self.verticalLayout_subtitle.addWidget(self.txt_output_subtitle)

        self.btn_select_output_subtitle = QPushButton(self.page_subtitle)
        self.btn_select_output_subtitle.setObjectName(u"btn_select_output_subtitle")

        self.verticalLayout_subtitle.addWidget(self.btn_select_output_subtitle)

        self.btn_convert_subtitle = QPushButton(self.page_subtitle)
        self.btn_convert_subtitle.setObjectName(u"btn_convert_subtitle")

        self.verticalLayout_subtitle.addWidget(self.btn_convert_subtitle)

        self.stackedWidget.addWidget(self.page_subtitle)
        self.page_danmu = QWidget()
        self.page_danmu.setObjectName(u"page_danmu")
        self.verticalLayout_danmu = QVBoxLayout(self.page_danmu)
        self.verticalLayout_danmu.setSpacing(8)
        self.verticalLayout_danmu.setObjectName(u"verticalLayout_danmu")
        self.btn_select_danmu = QPushButton(self.page_danmu)
        self.btn_select_danmu.setObjectName(u"btn_select_danmu")

        self.verticalLayout_danmu.addWidget(self.btn_select_danmu)

        self.txt_output_danmu = QTextEdit(self.page_danmu)
        self.txt_output_danmu.setObjectName(u"txt_output_danmu")
        sizePolicy1.setHeightForWidth(self.txt_output_danmu.sizePolicy().hasHeightForWidth())
        self.txt_output_danmu.setSizePolicy(sizePolicy1)

        self.verticalLayout_danmu.addWidget(self.txt_output_danmu)

        self.btn_select_output_danmu = QPushButton(self.page_danmu)
        self.btn_select_output_danmu.setObjectName(u"btn_select_output_danmu")

        self.verticalLayout_danmu.addWidget(self.btn_select_output_danmu)

        self.btn_convert_danmu = QPushButton(self.page_danmu)
        self.btn_convert_danmu.setObjectName(u"btn_convert_danmu")

        self.verticalLayout_danmu.addWidget(self.btn_convert_danmu)

        self.stackedWidget.addWidget(self.page_danmu)
        self.page_mp4 = QWidget()
        self.page_mp4.setObjectName(u"page_mp4")
        self.verticalLayout_mp4 = QVBoxLayout(self.page_mp4)
        self.verticalLayout_mp4.setSpacing(8)
        self.verticalLayout_mp4.setObjectName(u"verticalLayout_mp4")
        self.btn_select_mp4 = QPushButton(self.page_mp4)
        self.btn_select_mp4.setObjectName(u"btn_select_mp4")

        self.verticalLayout_mp4.addWidget(self.btn_select_mp4)

        self.txt_output_mp4 = QTextEdit(self.page_mp4)
        self.txt_output_mp4.setObjectName(u"txt_output_mp4")
        sizePolicy1.setHeightForWidth(self.txt_output_mp4.sizePolicy().hasHeightForWidth())
        self.txt_output_mp4.setSizePolicy(sizePolicy1)

        self.verticalLayout_mp4.addWidget(self.txt_output_mp4)

        self.btn_select_output_mp3 = QPushButton(self.page_mp4)
        self.btn_select_output_mp3.setObjectName(u"btn_select_output_mp3")

        self.verticalLayout_mp4.addWidget(self.btn_select_output_mp3)

        self.btn_convert_mp4 = QPushButton(self.page_mp4)
        self.btn_convert_mp4.setObjectName(u"btn_convert_mp4")

        self.verticalLayout_mp4.addWidget(self.btn_convert_mp4)

        self.progress_mp4 = QProgressBar(self.page_mp4)
        self.progress_mp4.setObjectName(u"progress_mp4")
        self.progress_mp4.setValue(0)
        self.progress_mp4.setTextVisible(True)

        self.verticalLayout_mp4.addWidget(self.progress_mp4)

        self.stackedWidget.addWidget(self.page_mp4)

        self.horizontalLayout_root.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\u7bb1", None))

        __sortingEnabled = self.menuList.isSortingEnabled()
        self.menuList.setSortingEnabled(False)
        ___qlistwidgetitem = self.menuList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u5e55\u8f6c\u7eaf\u6587\u672c", None));
        ___qlistwidgetitem1 = self.menuList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5f39\u5e55\u63d0\u53d6\u6587\u672c", None));
        ___qlistwidgetitem2 = self.menuList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"MP4 \u8f6c MP3", None));
        self.menuList.setSortingEnabled(__sortingEnabled)

        self.btn_select_subtitle.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5b57\u5e55\u6587\u4ef6", None))
        self.txt_output_subtitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u663e\u793a\u5904\u7406\u65e5\u5fd7 / \u7ed3\u679c", None))
        self.btn_select_output_subtitle.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f93\u51fa\u8def\u5f84", None))
        self.btn_convert_subtitle.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
        self.btn_select_danmu.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5f39\u5e55\u6587\u4ef6", None))
        self.txt_output_danmu.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u663e\u793a\u63d0\u53d6\u7684\u5f39\u5e55\u6216\u5904\u7406\u65e5\u5fd7", None))
        self.btn_select_output_danmu.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f93\u51fa\u8def\u5f84", None))
        self.btn_convert_danmu.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
        self.btn_select_mp4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9 MP4 \u6587\u4ef6", None))
        self.txt_output_mp4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8fd9\u91cc\u663e\u793a\u5904\u7406\u65e5\u5fd7 / \u7ed3\u679c", None))
        self.btn_select_output_mp3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f93\u51fa\u8def\u5f84", None))
        self.btn_convert_mp4.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
    # retranslateUi

