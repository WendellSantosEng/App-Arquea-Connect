# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(658, 479)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: \"#20B2AA\";\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_container.sizePolicy().hasHeightForWidth())
        self.left_container.setSizePolicy(sizePolicy)
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_left = QFrame(self.left_container)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setStyleSheet(u"#frame_left QPushButton {\n"
"    background-color: #006400; /* Cor de fundo padr\u00e3o */\n"
"	color: white;\n"
"}\n"
"\n"
"#frame_left QPushButton:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                                      stop: 0 #006400, stop: 1 #008000); \n"
"}")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_left)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(17)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_left)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font1 = QFont()
        font1.setPointSize(17)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.frame_left)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame_left)


        self.horizontalLayout.addWidget(self.left_container)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.frame_2)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.top_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(20, 20))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/C:/Workspace/Python/ProjetoAPP/icons/menu-bar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 25))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.frame_6 = QFrame(self.top_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 0, 201, 16))

        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.frame_2)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy2)
        self.main_frame.setStyleSheet(u"background-color: #008B8B;")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_6 = QVBoxLayout(self.page_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.page_home)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.page_home)
        self.page_codsup = QWidget()
        self.page_codsup.setObjectName(u"page_codsup")
        self.verticalLayout_7 = QVBoxLayout(self.page_codsup)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.page_codsup)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy3)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 13):
            self.tableWidget.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148,148,148);\n"
"	color: rgb(255,255,255);\n"
"	font:10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(252,252,252);\n"
"}")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,24,74);	\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"}\n"
"QFrame{\n"
"	background-color: rgb(230,230,230);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_import = QPushButton(self.frame_4)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(120, 30))
        self.btn_import.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(49,147,0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_import)

        self.btn_gerar = QPushButton(self.frame_4)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(120, 30))
        self.btn_gerar.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,170,0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_gerar)

        self.btn_saved = QPushButton(self.frame_4)
        self.btn_saved.setObjectName(u"btn_saved")
        self.btn_saved.setMinimumSize(QSize(120, 30))
        self.btn_saved.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: #4682B4;\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_saved)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.label)

        self.scrollArea = QScrollArea(self.frame_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 406, 1010))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_12.addWidget(self.frame_5)


        self.verticalLayout_11.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_codsup)
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.horizontalLayout_9 = QHBoxLayout(self.page_sobre)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_8 = QFrame(self.page_sobre)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setAutoFillBackground(False)

        self.verticalLayout_10.addWidget(self.pushButton_4)

        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_10.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.frame_8)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_10.addWidget(self.pushButton_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.horizontalLayout_9.addWidget(self.frame_8)

        self.stackedWidget_2 = QStackedWidget(self.page_sobre)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page1_Arquea = QWidget()
        self.page1_Arquea.setObjectName(u"page1_Arquea")
        self.page1_Arquea.setStyleSheet(u"\n"
"QWidget {\n"
"    background-image: url(C:\\Workspace\\Python\\ProjetoAPP\\icons\\logo_arquea.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.page1_Arquea)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_9 = QFrame(self.page1_Arquea)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 60, 101, 16))
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 80, 71, 16))

        self.verticalLayout_16.addWidget(self.frame_9)

        self.stackedWidget_2.addWidget(self.page1_Arquea)
        self.page_RenovaBio = QWidget()
        self.page_RenovaBio.setObjectName(u"page_RenovaBio")
        self.verticalLayout_15 = QVBoxLayout(self.page_RenovaBio)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_10 = QFrame(self.page_RenovaBio)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 50, 71, 16))
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(130, 80, 31, 16))

        self.verticalLayout_15.addWidget(self.frame_10)

        self.stackedWidget_2.addWidget(self.page_RenovaBio)
        self.page_Autor = QWidget()
        self.page_Autor.setObjectName(u"page_Autor")
        self.verticalLayout_14 = QVBoxLayout(self.page_Autor)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_7 = QFrame(self.page_Autor)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 60, 49, 16))
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 90, 31, 16))

        self.verticalLayout_14.addWidget(self.frame_7)

        self.stackedWidget_2.addWidget(self.page_Autor)

        self.horizontalLayout_9.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.page_sobre)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.frame_2)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NOME/LOGO", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Codigo Sup", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/C:/Workspace/Python/ProjetoAPP/icons/menu-bar.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ARQUEA Engenharia e Geotecnologia", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/C:/Workspace/Python/ProjetoAPP/icons/logo_arquea_completo.png\"/></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"COD_SUPR", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOM_PRODUT", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"CAR", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"SUP_PERIOD", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"DATA_SUP", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"INSER_2021", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"INSER_2022", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"INSER_2023", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ATIV_RENOV", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"OBS 1", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OBS 2", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"AREA_SUPR", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ANO_SUP", None));
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"Importar Planilha", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar Codigo", None))
        self.btn_saved.setText(QCoreApplication.translate("MainWindow", u"Salvar altera\u00e7\u00f5es", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Planilha", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"COMO FUNCIONA ?", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ut urna ac tellus ultrices commodo. Vivamus hendrerit purus id odio porta, nec scelerisque arcu tincidunt. Integer ut nulla in lectus bibendum interdum. Fusce fermentum nunc vel nisl facilisis, sit amet viverra elit consequat. Nam vehicula arcu id magna volutpat, id sagittis urna congue. Duis interdum, sapien sed scelerisque congue, justo orci ullamcorper sapien, sit amet tincidunt libero est id nunc. Sed in ligula sed ligula ullamcorper rhoncus eget nec orci. Proin id consequat orci. Quisque sodales quam vitae diam tempor, vel vestibulum nisi tristique. Nulla malesuada semper ex vel fermentum. In hac habitasse platea dictumst. Duis fermentum feugiat facilisis.\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ut urna ac tellus ultrices commodo. Vivamus hendrerit purus id odio porta, nec scelerisque arcu tincidunt. Integer ut nulla in lectus bibendum interdum. Fusce fermentum nunc vel nisl facilisis, sit amet viverra elit consequat. N"
                        "am vehicula arcu id magna volutpat, id sagittis urna congue. Duis interdum, sapien sed scelerisque congue, justo orci ullamcorper sapien, sit amet tincidunt libero est id nunc. Sed in ligula sed ligula ullamcorper rhoncus eget nec orci. Proin id consequat orci. Quisque sodales quam vitae diam tempor, vel vestibulum nisi tristique. Nulla malesuada semper ex vel fermentum. In hac habitasse platea dictumst. Duis fermentum feugiat facilisis.\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ut urna ac tellus ultrices commodo. Vivamus hendrerit purus id odio porta, nec scelerisque arcu tincidunt. Integer ut nulla in lectus bibendum interdum. Fusce fermentum nunc vel nisl facilisis, sit amet viverra elit consequat. Nam vehicula arcu id magna volutpat, id sagittis urna congue. Duis interdum, sapien sed scelerisque congue, justo orci ullamcorper sapien, sit amet tincidunt libero est id nunc. Sed in ligula sed ligula ullamcorper rhoncus eget nec orci. Proin id consequat orci. Quisque sodales quam vitae di"
                        "am tempor, vel vestibulum nisi tristique. Nulla malesuada semper ex vel fermentum. In hac habitasse platea dictumst. Duis fermentum feugiat facilisis.\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ut urna ac tellus ultrices commodo. Vivamus hendrerit purus id odio porta, nec scelerisque arcu tincidunt. Integer ut nulla in lectus bibendum interdum. Fusce fermentum nunc vel nisl facilisis, sit amet viverra elit consequat. Nam vehicula arcu id magna volutpat, id sagittis urna congue. Duis interdum, sapien sed scelerisque congue, justo orci ullamcorper sapien, sit amet tincidunt libero est id nunc. Sed in ligula sed ligula ullamcorper rhoncus eget nec orci. Proin id consequat orci. Quisque sodales quam vitae diam tempor, vel vestibulum nisi tristique. Nulla malesuada semper ex vel fermentum. In hac habitasse platea dictumst. Duis fermentum feugiat facilisis.\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ut urna ac tellus ultrices commodo. Vivamus hendrerit purus id odio porta, n"
                        "ec scelerisque arcu tincidunt. Integer ut nulla in lectus bibendum interdum. Fusce fermentum nunc vel nisl facilisis, sit amet viverra elit consequat. Nam vehicula arcu id magna volutpat, id sagittis urna congue. Duis interdum, sapien sed scelerisque congue, justo orci ullamcorper sapien, sit amet tincidunt libero est id nunc. Sed in ligula sed ligula ullamcorper rhoncus eget nec orci. Proin id consequat orci. Quisque sodales quam vitae diam tempor, vel vestibulum nisi tristique. Nulla malesuada semper ex vel fermentum. In hac habitasse platea dictumst. Duis fermentum feugiat facilisis.\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ut urna ac tellus ultrices commodo. Vivamus hendrerit purus id odio porta, nec scelerisque arcu tincidunt. Integer ut nulla in lectus bibendum interdum. Fusce fermentum nunc vel nisl facilisis, sit amet viverra elit consequat. Nam vehicula arcu id magna volutpat, id sagittis urna congue. Duis interdum, sapien sed scelerisque congue, justo orci ullamcorper sapien, s"
                        "it amet tincidunt libero est id nunc. Sed in ligula sed ligula ullamcorper rhoncus eget nec orci. Proin id consequat orci. Quisque sodales quam vitae diam tempor, vel vestibulum nisi tristique. Nulla malesuada semper ex vel fermentum. In hac habitasse platea dictumst. Duis fermentum feugiat facilisis.\"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Como Funciona?", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Sobre a Arquea", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"RenovaBio", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Sobre o autor", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SOBRE A ARQUEA", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://arqueageotec.com.br/\"><span style=\" text-decoration: underline; color:#0078d7;\">LINK DO SITE</span></a></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"RENOVA BIO", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://www.gov.br/anp/pt-br/assuntos/renovabio\"><span style=\" text-decoration: underline; color:#0078d7;\">GOV</span></a></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"GITHUB", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/WendellSantosEng/\"><span style=\" text-decoration: underline; color:#0078d7;\">LINK</span></a></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ArqueaConnect\u00a9", None))
    # retranslateUi

