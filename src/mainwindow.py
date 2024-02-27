# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modificatebutton.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(806, 541)
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
        self.left_container.setMaximumSize(QSize(9, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.left_container.setFont(font)
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
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(17)
        font1.setBold(False)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_left)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font2 = QFont()
        font2.setPointSize(17)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_8 = QPushButton(self.frame_left)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font2)

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_5 = QPushButton(self.frame_left)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font2)
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
        icon.addFile(u":/icons/menu-bar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 25))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.frame_6 = QFrame(self.top_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 0, 201, 16))

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
        self.page_shape = QWidget()
        self.page_shape.setObjectName(u"page_shape")
        self.horizontalLayout_11 = QHBoxLayout(self.page_shape)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tabWidget_2 = QTabWidget(self.page_shape)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_12 = QFrame(self.tab_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(100, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tableWidget_2 = QTableWidget(self.frame_12)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148,148,148);\n"
"	color: rgb(255,255,255);\n"
"	font:10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableWidget{\n"
"	background-color: \"#E0FFFF\";\n"
"}")
        self.tableWidget_2.setColumnCount(0)

        self.horizontalLayout_13.addWidget(self.tableWidget_2)

        self.frame_11 = QFrame(self.frame_12)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(30)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy3)
        self.frame_11.setMinimumSize(QSize(130, 0))
        self.frame_11.setMaximumSize(QSize(150, 16777215))
        self.frame_11.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,24,74);	\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"}\n"
"QFrame{\n"
"	background-color: \"#E0FFFF\";\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btn_planilha_dados = QPushButton(self.frame_11)
        self.btn_planilha_dados.setObjectName(u"btn_planilha_dados")
        sizePolicy1.setHeightForWidth(self.btn_planilha_dados.sizePolicy().hasHeightForWidth())
        self.btn_planilha_dados.setSizePolicy(sizePolicy1)
        self.btn_planilha_dados.setMinimumSize(QSize(120, 30))
        self.btn_planilha_dados.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.btn_planilha_dados.setFont(font3)
        self.btn_planilha_dados.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_planilha_dados.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(49,147,0);\n"
"}")

        self.verticalLayout_13.addWidget(self.btn_planilha_dados)

        self.btn_filtrar = QPushButton(self.frame_11)
        self.btn_filtrar.setObjectName(u"btn_filtrar")
        self.btn_filtrar.setMinimumSize(QSize(120, 30))
        self.btn_filtrar.setFont(font3)
        self.btn_filtrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_filtrar.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: \"#2F4F4F\";\n"
"}")

        self.verticalLayout_13.addWidget(self.btn_filtrar)

        self.frame_filter = QFrame(self.frame_11)
        self.frame_filter.setObjectName(u"frame_filter")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_filter.sizePolicy().hasHeightForWidth())
        self.frame_filter.setSizePolicy(sizePolicy4)
        self.frame_filter.setMinimumSize(QSize(110, 0))
        self.frame_filter.setMaximumSize(QSize(110, 16777215))
        self.frame_filter.setStyleSheet(u"")
        self.frame_filter.setFrameShape(QFrame.StyledPanel)
        self.frame_filter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_filter)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.select_column = QComboBox(self.frame_filter)
        self.select_column.setObjectName(u"select_column")
        self.select_column.setMinimumSize(QSize(90, 25))
        self.select_column.setMaximumSize(QSize(110, 30))

        self.verticalLayout_17.addWidget(self.select_column)

        self.search_filter = QLineEdit(self.frame_filter)
        self.search_filter.setObjectName(u"search_filter")
        self.search_filter.setMinimumSize(QSize(90, 15))
        self.search_filter.setMaximumSize(QSize(120, 30))
        self.search_filter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.search_filter)

        self.btn_okfilter = QPushButton(self.frame_filter)
        self.btn_okfilter.setObjectName(u"btn_okfilter")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_okfilter.sizePolicy().hasHeightForWidth())
        self.btn_okfilter.setSizePolicy(sizePolicy5)
        self.btn_okfilter.setMinimumSize(QSize(90, 20))
        self.btn_okfilter.setMaximumSize(QSize(25, 25))
        self.btn_okfilter.setSizeIncrement(QSize(0, 0))
        self.btn_okfilter.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_okfilter.setStyleSheet(u"QPushButton{\n"
"	border-radius:5px;\n"
"	font:11pt \"Modern No. 20\";\n"
"}\n"
"QPushButton:hover{\n"
"	border-radius: 30px;\n"
"	background-color: \"#66CDAA\";\n"
"}")
        self.btn_okfilter.setAutoRepeatInterval(0)

        self.verticalLayout_17.addWidget(self.btn_okfilter, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)


        self.verticalLayout_13.addWidget(self.frame_filter, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)


        self.horizontalLayout_13.addWidget(self.frame_11)


        self.horizontalLayout_12.addWidget(self.frame_12)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_car = QWidget()
        self.tab_car.setObjectName(u"tab_car")
        self.verticalLayout_18 = QVBoxLayout(self.tab_car)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_13 = QFrame(self.tab_car)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.tableWidget_3 = QTableWidget(self.frame_13)
        if (self.tableWidget_3.columnCount() < 11):
            self.tableWidget_3.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148,148,148);\n"
"	color: rgb(255,255,255);\n"
"	font:10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableWidget{\n"
"	background-color: \"#E0FFFF\";\n"
"}")

        self.horizontalLayout_14.addWidget(self.tableWidget_3)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(130, 0))
        self.frame_14.setMaximumSize(QSize(150, 16777215))
        self.frame_14.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,24,74);	\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"}\n"
"QFrame{\n"
"	background-color: \"#E0FFFF\";\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_14)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.btn_sicar = QPushButton(self.frame_14)
        self.btn_sicar.setObjectName(u"btn_sicar")
        self.btn_sicar.setMinimumSize(QSize(120, 30))
        self.btn_sicar.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(49,147,0);\n"
"}")

        self.verticalLayout_20.addWidget(self.btn_sicar)

        self.btn_selectCAR = QPushButton(self.frame_14)
        self.btn_selectCAR.setObjectName(u"btn_selectCAR")
        self.btn_selectCAR.setMinimumSize(QSize(120, 30))
        self.btn_selectCAR.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,170,0);\n"
"}")

        self.verticalLayout_20.addWidget(self.btn_selectCAR)

        self.btn_exportCAR = QPushButton(self.frame_14)
        self.btn_exportCAR.setObjectName(u"btn_exportCAR")
        self.btn_exportCAR.setMinimumSize(QSize(120, 30))
        self.btn_exportCAR.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: #4682B4;\n"
"}")

        self.verticalLayout_20.addWidget(self.btn_exportCAR)

        self.label_aguarde = QLabel(self.frame_14)
        self.label_aguarde.setObjectName(u"label_aguarde")
        font4 = QFont()
        font4.setItalic(True)
        self.label_aguarde.setFont(font4)
        self.label_aguarde.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_aguarde)

        self.progressBar_sicar = QProgressBar(self.frame_14)
        self.progressBar_sicar.setObjectName(u"progressBar_sicar")
        self.progressBar_sicar.setMaximumSize(QSize(16777215, 20))
        self.progressBar_sicar.setValue(24)

        self.verticalLayout_20.addWidget(self.progressBar_sicar)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_6)


        self.horizontalLayout_14.addWidget(self.frame_14)


        self.verticalLayout_18.addWidget(self.frame_13)

        self.tabWidget_2.addTab(self.tab_car, "")
        self.tab_safra = QWidget()
        self.tab_safra.setObjectName(u"tab_safra")
        self.verticalLayout_19 = QVBoxLayout(self.tab_safra)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_15 = QFrame(self.tab_safra)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tableWidget_4 = QTableWidget(self.frame_15)
        if (self.tableWidget_4.columnCount() < 15):
            self.tableWidget_4.setColumnCount(15)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(11, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(12, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(13, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(14, __qtablewidgetitem25)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148,148,148);\n"
"	color: rgb(255,255,255);\n"
"	font:10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableWidget{\n"
"	background-color: \"#E0FFFF\";\n"
"}")

        self.horizontalLayout_15.addWidget(self.tableWidget_4)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(130, 0))
        self.frame_16.setMaximumSize(QSize(150, 16777215))
        self.frame_16.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,24,74);	\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"}\n"
"QFrame{\n"
"	background-color: \"#E0FFFF\";\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_16)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.importDataSafra = QPushButton(self.frame_16)
        self.importDataSafra.setObjectName(u"importDataSafra")
        self.importDataSafra.setMinimumSize(QSize(120, 30))
        self.importDataSafra.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,170,0);\n"
"}")

        self.verticalLayout_21.addWidget(self.importDataSafra)

        self.exportSHPSafra = QPushButton(self.frame_16)
        self.exportSHPSafra.setObjectName(u"exportSHPSafra")
        self.exportSHPSafra.setMinimumSize(QSize(120, 30))
        self.exportSHPSafra.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: #4682B4;\n"
"}")

        self.verticalLayout_21.addWidget(self.exportSHPSafra)

        self.usina_info = QLabel(self.frame_16)
        self.usina_info.setObjectName(u"usina_info")
        font5 = QFont()
        font5.setBold(True)
        self.usina_info.setFont(font5)
        self.usina_info.setAlignment(Qt.AlignCenter)
        self.usina_info.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.usina_info)

        self.usina_name = QLabel(self.frame_16)
        self.usina_name.setObjectName(u"usina_name")
        font6 = QFont()
        font6.setFamilies([u"Russo One"])
        font6.setPointSize(15)
        self.usina_name.setFont(font6)
        self.usina_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.usina_name)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)


        self.horizontalLayout_15.addWidget(self.frame_16)


        self.verticalLayout_19.addWidget(self.frame_15)

        self.tabWidget_2.addTab(self.tab_safra, "")

        self.horizontalLayout_11.addWidget(self.tabWidget_2)

        self.stackedWidget.addWidget(self.page_shape)
        self.page_codsup = QWidget()
        self.page_codsup.setObjectName(u"page_codsup")
        self.verticalLayout_7 = QVBoxLayout(self.page_codsup)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.page_codsup)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy6)
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
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem38)
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
        self.btn_import.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_import.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(49,147,0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_import)

        self.btn_importshp = QPushButton(self.frame_4)
        self.btn_importshp.setObjectName(u"btn_importshp")
        self.btn_importshp.setMinimumSize(QSize(120, 30))
        self.btn_importshp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importshp.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(49,147,0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_importshp)

        self.btn_gerar = QPushButton(self.frame_4)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(120, 30))
        self.btn_gerar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,170,0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_gerar)

        self.btn_saved = QPushButton(self.frame_4)
        self.btn_saved.setObjectName(u"btn_saved")
        self.btn_saved.setMinimumSize(QSize(120, 30))
        self.btn_saved.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_saved.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: #4682B4;\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_saved)

        self.btn_savedshp = QPushButton(self.frame_4)
        self.btn_savedshp.setObjectName(u"btn_savedshp")
        self.btn_savedshp.setMinimumSize(QSize(120, 30))
        self.btn_savedshp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_savedshp.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: #4682B4;\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_savedshp)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 101, 89))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_6.addWidget(self.textBrowser)

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
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_8)


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
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_12)


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
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10)


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

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NOME/LOGO", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Codigo Sup", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Gerar Shape", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/C:/Workspace/Python/ProjetoAPP/icons/menu-bar.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ARQUEA Engenharia e Geotecnologia", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/logo_arquea_completo.png\"/></p></body></html>", None))
        self.btn_planilha_dados.setText(QCoreApplication.translate("MainWindow", u"Buscar Planilha", None))
        self.btn_filtrar.setText(QCoreApplication.translate("MainWindow", u"Filtros", None))
        self.btn_okfilter.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"DADOS DE ENTRADA", None))
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"cod_imovel", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"status_imo", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"dat_criaca", None));
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"area", None));
        ___qtablewidgetitem4 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"condicao", None));
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"uf", None));
        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"municipio", None));
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"cod_munici", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"m_fiscal", None));
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"tipo_imove", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"polygon", None));
        self.btn_sicar.setText(QCoreApplication.translate("MainWindow", u"SICAR-MT", None))
        self.btn_selectCAR.setText(QCoreApplication.translate("MainWindow", u"Realizar Sele\u00e7\u00e3o", None))
        self.btn_exportCAR.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.label_aguarde.setText(QCoreApplication.translate("MainWindow", u"Aguarde...", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_car), QCoreApplication.translate("MainWindow", u"CAR", None))
        ___qtablewidgetitem11 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"COD_PRODUT", None));
        ___qtablewidgetitem12 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"PLANT_USIN", None));
        ___qtablewidgetitem13 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"NOM_PRODUT", None));
        ___qtablewidgetitem14 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"CPF_CNPJ", None));
        ___qtablewidgetitem15 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ANO_SAFRA", None));
        ___qtablewidgetitem16 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"TIPO", None));
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"COD_IMOVEL", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"COD_MAPA", None));
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"DATA_REGIS", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(10)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"SITUACAO", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(11)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"AREA_TOTAL", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(12)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"AREA_MAPA", None));
        ___qtablewidgetitem24 = self.tableWidget_4.horizontalHeaderItem(13)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"SUPRESSAO", None));
        ___qtablewidgetitem25 = self.tableWidget_4.horizontalHeaderItem(14)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"ELEGIBILID", None));
        self.importDataSafra.setText(QCoreApplication.translate("MainWindow", u"Importar Dados", None))
        self.exportSHPSafra.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.usina_info.setText(QCoreApplication.translate("MainWindow", u"ESSE GRUPO PERTENCE A USINA", None))
        self.usina_name.setText(QCoreApplication.translate("MainWindow", u"LRV", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_safra), QCoreApplication.translate("MainWindow", u"SAFRA", None))
        ___qtablewidgetitem26 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"COD_SUPR", None));
        ___qtablewidgetitem27 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"NOM_PRODUT", None));
        ___qtablewidgetitem28 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"CAR", None));
        ___qtablewidgetitem29 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"SUP_PERIOD", None));
        ___qtablewidgetitem30 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"DATA_SUP", None));
        ___qtablewidgetitem31 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"INSER_2021", None));
        ___qtablewidgetitem32 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"INSER_2022", None));
        ___qtablewidgetitem33 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"INSER_2023", None));
        ___qtablewidgetitem34 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"ATIV_RENOV", None));
        ___qtablewidgetitem35 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"OBS 1", None));
        ___qtablewidgetitem36 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"OBS 2", None));
        ___qtablewidgetitem37 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"AREA_SUPR", None));
        ___qtablewidgetitem38 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"ANO_SUP", None));
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"Importar Planilha", None))
        self.btn_importshp.setText(QCoreApplication.translate("MainWindow", u"Importar Shapefile", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar Codigo", None))
        self.btn_saved.setText(QCoreApplication.translate("MainWindow", u"Salvar em .xlsx", None))
        self.btn_savedshp.setText(QCoreApplication.translate("MainWindow", u" Salvar em Shapefile ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Planilha", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"COMO FUNCIONA ?", None))
        self.label_4.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">O codigo \u00e9 gerado da seguinte forma:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" f"
                        "ont-size:11pt;\">1 - Vezes que o CAR aparece na tabela</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">2 - O index da vez que est\u00e1 aparecendo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">3 - Letra C, a qual simboliza a palavra CAR</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">4 - 5 \u00faltimos digitos do c\u00f3digo CAR</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">5 - A, representando a palavra antes, ou D, representando a palavra depois</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin"
                        "-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">6 - O numero 17, o qual representa o ano 2017.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">7 - Ano da supress\u00e3o, caso ocorra antes de 2017 (&lt;2017), o valor ser\u00e1 00</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">8 - Anos que ocorreram cultivo.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">EXEMPLO:<br />         026-001-C17575-A17-00-A-21-22-23</span></p>\n"
"<p style=\" margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">         026-002-C17575-A17-00-A-21-22-23</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">         026-003-C17575-A17-00-A-21-22-23</span></p></body></html>", None))
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

