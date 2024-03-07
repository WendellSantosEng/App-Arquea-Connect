# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'implementfunc.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QToolBox,
    QVBoxLayout, QWidget)
import icons_final

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(806, 541)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: #178B8D;\n"
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
        self.left_container.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.left_container.setFont(font)
        self.left_container.setStyleSheet(u"left_container {\n"
" 	border-top: 2px solid red;\n"
"	border-bottom: 2px solid red;\n"
"}\n"
"left_container {\n"
"	border-left: 1px solid blue;\n"
"	border-right: 1px solid blue;\n"
"}")
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.left_container)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"\n"
"image: url(:/icons_/ARQUEA.png);")

        self.verticalLayout_2.addWidget(self.label_3)

        self.frame_left = QFrame(self.left_container)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setStyleSheet(u"#frame_left  QPushButton {\n"
"	background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 100, 0, 255), stop:1 rgba(0, 50, 0, 255));\n"
"	color: white;\n"
"	font-size: 18px;\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgba(0, 0, 0, 100);\n"
"	padding: 10px 20px;\n"
"}\n"
"#frame_left  QPushButton:hover {\n"
"	background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 120, 0, 255), stop:1 rgba(0, 70, 0, 255));\n"
"}\n"
"#frame_left  QPushButton:pressed {\n"
"	background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 80, 0, 255), stop:1 rgba(0, 40, 0, 255));\n"
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
        self.pushButton_2.setMaximumSize(QSize(120, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(False)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_9 = QPushButton(self.frame_left)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(120, 16777215))
        font2 = QFont()
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setStyleSheet(u"margin:5px, 20px,5px,20px;")

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_5 = QPushButton(self.frame_left)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(120, 16777215))
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.frame_left)


        self.horizontalLayout.addWidget(self.left_container)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMaximumSize(QSize(40, 40))
        font3 = QFont()
        font3.setPointSize(20)
        self.pushButton.setFont(font3)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"border-radius: 15px;\n"
"\n"
"margim-border: 0px;\n"
"image: url(:/icons_/menu-bar.png);")
        icon = QIcon()
        icon.addFile(u":/icons/menu-bar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 25))

        self.verticalLayout.addWidget(self.pushButton)

        self.main_frame = QFrame(self.frame_2)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy3)
        self.main_frame.setStyleSheet(u"background-color: #178B8D;")
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
        self.label_5.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout_6.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.page_home)
        self.page_shape = QWidget()
        self.page_shape.setObjectName(u"page_shape")
        self.horizontalLayout_11 = QHBoxLayout(self.page_shape)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.stackedWidget_3 = QStackedWidget(self.page_shape)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolBox_usinas = QToolBox(self.page)
        self.toolBox_usinas.setObjectName(u"toolBox_usinas")
        self.toolBox_usinas.setMinimumSize(QSize(0, 0))
        self.toolBox_usinas.setMaximumSize(QSize(16777215, 16777215))
        self.toolBox_usinas.setStyleSheet(u"/* Estilo para o container do Toolbox */\n"
"QToolBox {\n"
"    background-color: #f5f5f5; /* Cor de fundo */\n"
"    border: 1px solid #ccc; /* Borda */\n"
"    border-radius: 5px; /* Raio da borda */\n"
"	padding: 10px 0px 0px 10px;\n"
"}\n"
"\n"
"/* Estilo para os itens do Toolbox */\n"
"QToolBox::tab {\n"
"    background-color: #e0e0e0; /* Cor de fundo da aba */\n"
"    color: #333; /* Cor do texto */\n"
"    padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"    border-bottom: 1px solid #ccc; /* Borda inferior */\n"
"}\n"
"\n"
"/* Estilo para a aba selecionada */\n"
"QToolBox::tab:selected {\n"
"    background-color: #d8d8d8; /* Cor de fundo da aba selecionada */\n"
"    border: 1px solid #bbb; /* Borda da aba selecionada */\n"
"}\n"
"\n"
"/* Estilo para o \u00edcone da aba */\n"
"QToolBox::tab:!selected {\n"
"    color: #666; /* Cor do \u00edcone */\n"
"}\n"
"\n"
"/* Estilo para o \u00edcone da aba selecionada */\n"
"QToolBox::tab:selected {\n"
"    color: #333; /* Cor do \u00edcone na aba selecionada"
                        " */\n"
"}\n"
"\n"
"/* Estilo para o conte\u00fado do Toolbox */\n"
"QToolBox QWidget {\n"
"    background-color: #fff; /* Cor de fundo do conte\u00fado */\n"
"    border: 1px solid #ccc; /* Borda */\n"
"    border: none; /* Remover a borda superior */\n"
"    border-radius: 0 0 5px 5px; /* Raio da borda (somente na parte inferior) */\n"
"}\n"
"\n"
"/* Estilo para o bot\u00e3o dentro do Toolbox */\n"
"QToolBox QWidget QPushButton {\n"
"    background-color: #007bff; /* Cor de fundo */\n"
"    color: #fff; /* Cor do texto */\n"
"    border: 1px solid #007bff; /* Borda */\n"
"    border-radius: 3px; /* Raio da borda */\n"
"    padding: 5px 5px; /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"/* Estilo para o bot\u00e3o quando pressionado */\n"
"QToolBox QWidget QPushButton:pressed {\n"
"    background-color: #0056b3; /* Cor de fundo quando pressionado */\n"
"    border-color: #0056b3; /* Cor da borda quando pressionado */\n"
"}\n"
"\n"
"/* Estilo para o bot\u00e3o quando hover */\n"
"QToolBox QWidget QPushButton:ho"
                        "ver {\n"
"    background-color: #0056b3; /* Cor de fundo ao passar o mouse */\n"
"    border-color: #0056b3; /* Cor da borda ao passar o mouse */\n"
"}\n"
"")
        self.toolBox_usinas.setFrameShape(QFrame.StyledPanel)
        self.USINAS_page = QWidget()
        self.USINAS_page.setObjectName(u"USINAS_page")
        self.USINAS_page.setGeometry(QRect(0, 0, 545, 239))
        self.verticalLayout_33 = QVBoxLayout(self.USINAS_page)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_26 = QFrame(self.USINAS_page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 16777215))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_13 = QLabel(self.frame_26)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(354, 203))

        self.horizontalLayout_4.addWidget(self.label_13)


        self.verticalLayout_33.addWidget(self.frame_26)

        self.toolBox_usinas.addItem(self.USINAS_page, u"USINAS")
        self.page_CAR = QWidget()
        self.page_CAR.setObjectName(u"page_CAR")
        self.page_CAR.setGeometry(QRect(0, 0, 562, 235))
        self.verticalLayout_35 = QVBoxLayout(self.page_CAR)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_27 = QFrame(self.page_CAR)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_11 = QPushButton(self.frame_27)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_17.addWidget(self.pushButton_11)


        self.verticalLayout_35.addWidget(self.frame_27)

        self.toolBox_usinas.addItem(self.page_CAR, u"CAR")
        self.SRS_page = QWidget()
        self.SRS_page.setObjectName(u"SRS_page")
        self.SRS_page.setGeometry(QRect(0, 0, 562, 235))
        self.verticalLayout_22 = QVBoxLayout(self.SRS_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_17 = QFrame(self.SRS_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_8 = QPushButton(self.frame_17)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 0))
        self.pushButton_8.setMaximumSize(QSize(200, 30))
        font4 = QFont()
        font4.setPointSize(8)
        self.pushButton_8.setFont(font4)

        self.horizontalLayout_18.addWidget(self.pushButton_8)


        self.verticalLayout_22.addWidget(self.frame_17)

        self.toolBox_usinas.addItem(self.SRS_page, u"SRS")
        self.LRV_page = QWidget()
        self.LRV_page.setObjectName(u"LRV_page")
        self.LRV_page.setGeometry(QRect(0, 0, 562, 235))
        self.verticalLayout_23 = QVBoxLayout(self.LRV_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_18 = QFrame(self.LRV_page)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_10 = QPushButton(self.frame_18)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(200, 30))
        self.pushButton_10.setFont(font4)

        self.horizontalLayout_19.addWidget(self.pushButton_10)


        self.verticalLayout_23.addWidget(self.frame_18)

        self.toolBox_usinas.addItem(self.LRV_page, u"LRV")
        self.PDL_page = QWidget()
        self.PDL_page.setObjectName(u"PDL_page")
        self.PDL_page.setGeometry(QRect(0, 0, 562, 235))
        self.verticalLayout_24 = QVBoxLayout(self.PDL_page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_19 = QFrame(self.PDL_page)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_3 = QPushButton(self.frame_19)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(200, 30))
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.pushButton_3)


        self.verticalLayout_24.addWidget(self.frame_19)

        self.toolBox_usinas.addItem(self.PDL_page, u"PDL")

        self.gridLayout.addWidget(self.toolBox_usinas, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_25 = QHBoxLayout(self.page_5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_28 = QFrame(self.page_5)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy2.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy2)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_28)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tabWidget_4 = QTabWidget(self.frame_28)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_car_3 = QWidget()
        self.tab_car_3.setObjectName(u"tab_car_3")
        self.verticalLayout_40 = QVBoxLayout(self.tab_car_3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_33 = QFrame(self.tab_car_3)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.tableWidget_3 = QTableWidget(self.frame_33)
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

        self.horizontalLayout_29.addWidget(self.tableWidget_3)

        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(130, 0))
        self.frame_34.setMaximumSize(QSize(150, 16777215))
        self.frame_34.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,24,74);	\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"}\n"
"QFrame{\n"
"	background-color: \"#E0FFFF\";\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_34)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.btn_sicar = QPushButton(self.frame_34)
        self.btn_sicar.setObjectName(u"btn_sicar")
        self.btn_sicar.setMinimumSize(QSize(120, 30))
        self.btn_sicar.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(49,147,0);\n"
"}")

        self.verticalLayout_41.addWidget(self.btn_sicar)

        self.btn_selectCAR_SRS = QPushButton(self.frame_34)
        self.btn_selectCAR_SRS.setObjectName(u"btn_selectCAR_SRS")
        self.btn_selectCAR_SRS.setMinimumSize(QSize(120, 30))
        self.btn_selectCAR_SRS.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,170,0);\n"
"}")

        self.verticalLayout_41.addWidget(self.btn_selectCAR_SRS)

        self.btn_selectCAR_LRV = QPushButton(self.frame_34)
        self.btn_selectCAR_LRV.setObjectName(u"btn_selectCAR_LRV")
        self.btn_selectCAR_LRV.setMinimumSize(QSize(120, 30))
        self.btn_selectCAR_LRV.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,170,0);\n"
"}")

        self.verticalLayout_41.addWidget(self.btn_selectCAR_LRV)

        self.btn_exportCAR = QPushButton(self.frame_34)
        self.btn_exportCAR.setObjectName(u"btn_exportCAR")
        self.btn_exportCAR.setMinimumSize(QSize(120, 30))
        self.btn_exportCAR.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: #4682B4;\n"
"}")

        self.verticalLayout_41.addWidget(self.btn_exportCAR)

        self.label_aguarde = QLabel(self.frame_34)
        self.label_aguarde.setObjectName(u"label_aguarde")
        font5 = QFont()
        font5.setItalic(True)
        self.label_aguarde.setFont(font5)
        self.label_aguarde.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_aguarde)

        self.progressBar_sicar = QProgressBar(self.frame_34)
        self.progressBar_sicar.setObjectName(u"progressBar_sicar")
        self.progressBar_sicar.setMaximumSize(QSize(16777215, 20))
        self.progressBar_sicar.setValue(24)

        self.verticalLayout_41.addWidget(self.progressBar_sicar)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_15)

        self.btn_back_2 = QPushButton(self.frame_34)
        self.btn_back_2.setObjectName(u"btn_back_2")
        self.btn_back_2.setMinimumSize(QSize(120, 30))
        self.btn_back_2.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"    background-color: #FFD700;\n"
"    border-color: #FFD700;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#FFA500;\n"
"}\n"
"")

        self.verticalLayout_41.addWidget(self.btn_back_2)


        self.horizontalLayout_29.addWidget(self.frame_34)


        self.verticalLayout_40.addWidget(self.frame_33)

        self.tabWidget_4.addTab(self.tab_car_3, "")

        self.verticalLayout_18.addWidget(self.tabWidget_4)


        self.horizontalLayout_25.addWidget(self.frame_28)

        self.stackedWidget_3.addWidget(self.page_5)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget_2 = QTabWidget(self.page_2)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(30)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
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
        font6 = QFont()
        font6.setFamilies([u"MS Shell Dlg 2"])
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(False)
        self.btn_planilha_dados.setFont(font6)
        self.btn_planilha_dados.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_planilha_dados.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(49,147,0);\n"
"}")

        self.verticalLayout_13.addWidget(self.btn_planilha_dados)

        self.btn_filtrar = QPushButton(self.frame_11)
        self.btn_filtrar.setObjectName(u"btn_filtrar")
        self.btn_filtrar.setMinimumSize(QSize(120, 30))
        self.btn_filtrar.setFont(font6)
        self.btn_filtrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_filtrar.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: \"#2F4F4F\";\n"
"}")

        self.verticalLayout_13.addWidget(self.btn_filtrar)

        self.frame_filter = QFrame(self.frame_11)
        self.frame_filter.setObjectName(u"frame_filter")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_filter.sizePolicy().hasHeightForWidth())
        self.frame_filter.setSizePolicy(sizePolicy5)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_okfilter.sizePolicy().hasHeightForWidth())
        self.btn_okfilter.setSizePolicy(sizePolicy6)
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

        self.btn_back_3 = QPushButton(self.frame_11)
        self.btn_back_3.setObjectName(u"btn_back_3")
        self.btn_back_3.setMinimumSize(QSize(120, 30))
        self.btn_back_3.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"    background-color: #FFD700;\n"
"    border-color: #FFD700;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#FFA500;\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.btn_back_3)


        self.horizontalLayout_13.addWidget(self.frame_11)


        self.horizontalLayout_12.addWidget(self.frame_12)

        self.tabWidget_2.addTab(self.tab_5, "")
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

        self.btn_CSV = QPushButton(self.frame_16)
        self.btn_CSV.setObjectName(u"btn_CSV")
        self.btn_CSV.setMinimumSize(QSize(120, 30))
        self.btn_CSV.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,170,0);\n"
"}")

        self.verticalLayout_21.addWidget(self.btn_CSV)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)

        self.btn_back_1 = QPushButton(self.frame_16)
        self.btn_back_1.setObjectName(u"btn_back_1")
        self.btn_back_1.setMinimumSize(QSize(120, 30))
        self.btn_back_1.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"    background-color: #FFD700;\n"
"    border-color: #FFD700;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#FFA500;\n"
"}\n"
"")

        self.verticalLayout_21.addWidget(self.btn_back_1)


        self.horizontalLayout_15.addWidget(self.frame_16)


        self.verticalLayout_19.addWidget(self.frame_15)

        self.tabWidget_2.addTab(self.tab_safra, "")

        self.verticalLayout_7.addWidget(self.tabWidget_2)

        self.stackedWidget_3.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_31 = QVBoxLayout(self.page_4)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.tabWidget_3 = QTabWidget(self.page_4)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_21 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_20 = QFrame(self.tab_6)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(100, 0))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.tableWidget_LRV_dados = QTableWidget(self.frame_20)
        self.tableWidget_LRV_dados.setObjectName(u"tableWidget_LRV_dados")
        self.tableWidget_LRV_dados.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148,148,148);\n"
"	color: rgb(255,255,255);\n"
"	font:10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableWidget{\n"
"	background-color: \"#E0FFFF\";\n"
"}")
        self.tableWidget_LRV_dados.setColumnCount(0)

        self.horizontalLayout_22.addWidget(self.tableWidget_LRV_dados)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy4.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy4)
        self.frame_21.setMinimumSize(QSize(130, 0))
        self.frame_21.setMaximumSize(QSize(150, 16777215))
        self.frame_21.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,24,74);	\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"}\n"
"QFrame{\n"
"	background-color: \"#E0FFFF\";\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_21)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.btn_planilha_dados_LRV = QPushButton(self.frame_21)
        self.btn_planilha_dados_LRV.setObjectName(u"btn_planilha_dados_LRV")
        sizePolicy1.setHeightForWidth(self.btn_planilha_dados_LRV.sizePolicy().hasHeightForWidth())
        self.btn_planilha_dados_LRV.setSizePolicy(sizePolicy1)
        self.btn_planilha_dados_LRV.setMinimumSize(QSize(120, 30))
        self.btn_planilha_dados_LRV.setMaximumSize(QSize(16777215, 16777215))
        self.btn_planilha_dados_LRV.setFont(font6)
        self.btn_planilha_dados_LRV.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_planilha_dados_LRV.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(49,147,0);\n"
"}")

        self.verticalLayout_25.addWidget(self.btn_planilha_dados_LRV)

        self.btn_filtrar_LRV = QPushButton(self.frame_21)
        self.btn_filtrar_LRV.setObjectName(u"btn_filtrar_LRV")
        self.btn_filtrar_LRV.setMinimumSize(QSize(120, 30))
        self.btn_filtrar_LRV.setFont(font6)
        self.btn_filtrar_LRV.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_filtrar_LRV.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: \"#2F4F4F\";\n"
"}")

        self.verticalLayout_25.addWidget(self.btn_filtrar_LRV)

        self.frame_filter_2 = QFrame(self.frame_21)
        self.frame_filter_2.setObjectName(u"frame_filter_2")
        sizePolicy5.setHeightForWidth(self.frame_filter_2.sizePolicy().hasHeightForWidth())
        self.frame_filter_2.setSizePolicy(sizePolicy5)
        self.frame_filter_2.setMinimumSize(QSize(110, 0))
        self.frame_filter_2.setMaximumSize(QSize(110, 16777215))
        self.frame_filter_2.setStyleSheet(u"")
        self.frame_filter_2.setFrameShape(QFrame.StyledPanel)
        self.frame_filter_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_filter_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.select_column_LRV = QComboBox(self.frame_filter_2)
        self.select_column_LRV.setObjectName(u"select_column_LRV")
        self.select_column_LRV.setMinimumSize(QSize(90, 25))
        self.select_column_LRV.setMaximumSize(QSize(110, 30))

        self.verticalLayout_26.addWidget(self.select_column_LRV)

        self.search_filter_LRV = QLineEdit(self.frame_filter_2)
        self.search_filter_LRV.setObjectName(u"search_filter_LRV")
        self.search_filter_LRV.setMinimumSize(QSize(90, 15))
        self.search_filter_LRV.setMaximumSize(QSize(120, 30))
        self.search_filter_LRV.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.search_filter_LRV)

        self.btn_okfilter_LRV = QPushButton(self.frame_filter_2)
        self.btn_okfilter_LRV.setObjectName(u"btn_okfilter_LRV")
        sizePolicy6.setHeightForWidth(self.btn_okfilter_LRV.sizePolicy().hasHeightForWidth())
        self.btn_okfilter_LRV.setSizePolicy(sizePolicy6)
        self.btn_okfilter_LRV.setMinimumSize(QSize(90, 20))
        self.btn_okfilter_LRV.setMaximumSize(QSize(25, 25))
        self.btn_okfilter_LRV.setSizeIncrement(QSize(0, 0))
        self.btn_okfilter_LRV.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_okfilter_LRV.setStyleSheet(u"QPushButton{\n"
"	border-radius:5px;\n"
"	font:11pt \"Modern No. 20\";\n"
"}\n"
"QPushButton:hover{\n"
"	border-radius: 30px;\n"
"	background-color: \"#66CDAA\";\n"
"}")
        self.btn_okfilter_LRV.setAutoRepeatInterval(0)

        self.verticalLayout_26.addWidget(self.btn_okfilter_LRV, 0, Qt.AlignHCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_8)


        self.verticalLayout_25.addWidget(self.frame_filter_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_9)

        self.btn_back_LRV_1 = QPushButton(self.frame_21)
        self.btn_back_LRV_1.setObjectName(u"btn_back_LRV_1")
        self.btn_back_LRV_1.setMinimumSize(QSize(120, 30))
        self.btn_back_LRV_1.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"    background-color: #FFD700;\n"
"    border-color: #FFD700;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#FFA500;\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.btn_back_LRV_1)


        self.horizontalLayout_22.addWidget(self.frame_21)


        self.horizontalLayout_21.addWidget(self.frame_20)

        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_safra_2 = QWidget()
        self.tab_safra_2.setObjectName(u"tab_safra_2")
        self.verticalLayout_29 = QVBoxLayout(self.tab_safra_2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_24 = QFrame(self.tab_safra_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.tableWidget_LRVsafra = QTableWidget(self.frame_24)
        if (self.tableWidget_LRVsafra.columnCount() < 15):
            self.tableWidget_LRVsafra.setColumnCount(15)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(7, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(8, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(9, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(10, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(11, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(12, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(13, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_LRVsafra.setHorizontalHeaderItem(14, __qtablewidgetitem40)
        self.tableWidget_LRVsafra.setObjectName(u"tableWidget_LRVsafra")
        self.tableWidget_LRVsafra.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148,148,148);\n"
"	color: rgb(255,255,255);\n"
"	font:10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableWidget{\n"
"	background-color: \"#E0FFFF\";\n"
"}")

        self.horizontalLayout_24.addWidget(self.tableWidget_LRVsafra)

        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(130, 0))
        self.frame_25.setMaximumSize(QSize(150, 16777215))
        self.frame_25.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,24,74);	\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"}\n"
"QFrame{\n"
"	background-color: \"#E0FFFF\";\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_25)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.importDataSafra_LRV = QPushButton(self.frame_25)
        self.importDataSafra_LRV.setObjectName(u"importDataSafra_LRV")
        self.importDataSafra_LRV.setMinimumSize(QSize(120, 30))
        self.importDataSafra_LRV.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,170,0);\n"
"}")

        self.verticalLayout_30.addWidget(self.importDataSafra_LRV)

        self.exportSHPSafra_LRV = QPushButton(self.frame_25)
        self.exportSHPSafra_LRV.setObjectName(u"exportSHPSafra_LRV")
        self.exportSHPSafra_LRV.setMinimumSize(QSize(120, 30))
        self.exportSHPSafra_LRV.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: #4682B4;\n"
"}")

        self.verticalLayout_30.addWidget(self.exportSHPSafra_LRV)

        self.btn_CSV2 = QPushButton(self.frame_25)
        self.btn_CSV2.setObjectName(u"btn_CSV2")
        self.btn_CSV2.setMinimumSize(QSize(120, 30))
        self.btn_CSV2.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255,170,0);\n"
"}")

        self.verticalLayout_30.addWidget(self.btn_CSV2)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_11)

        self.btn_back_LRV_3 = QPushButton(self.frame_25)
        self.btn_back_LRV_3.setObjectName(u"btn_back_LRV_3")
        self.btn_back_LRV_3.setMinimumSize(QSize(120, 30))
        self.btn_back_LRV_3.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"    background-color: #FFD700;\n"
"    border-color: #FFD700;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#FFA500;\n"
"}\n"
"")

        self.verticalLayout_30.addWidget(self.btn_back_LRV_3)


        self.horizontalLayout_24.addWidget(self.frame_25)


        self.verticalLayout_29.addWidget(self.frame_24)

        self.tabWidget_3.addTab(self.tab_safra_2, "")

        self.verticalLayout_31.addWidget(self.tabWidget_3)

        self.stackedWidget_3.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_32 = QVBoxLayout(self.page_3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy7)
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
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem53)
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
        self.frame_4.setMinimumSize(QSize(130, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
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

        self.btn_back_SUP = QPushButton(self.frame_4)
        self.btn_back_SUP.setObjectName(u"btn_back_SUP")
        self.btn_back_SUP.setMinimumSize(QSize(120, 30))
        self.btn_back_SUP.setMaximumSize(QSize(16777215, 16777215))
        self.btn_back_SUP.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"    background-color: #FFD700;\n"
"    border-color: #FFD700;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#FFA500;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.btn_back_SUP)


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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 508, 286))
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

        self.verticalLayout_32.addWidget(self.tabWidget)

        self.stackedWidget_3.addWidget(self.page_3)

        self.horizontalLayout_11.addWidget(self.stackedWidget_3)

        self.stackedWidget.addWidget(self.page_shape)
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.horizontalLayout_9 = QHBoxLayout(self.page_sobre)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_7 = QFrame(self.page_sobre)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"#frame_7  QPushButton {\n"
"	background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 100, 0, 255), stop:1 rgba(0, 50, 0, 255));\n"
"	color: white;\n"
"	font-size: 18px;\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgba(0, 0, 0, 100);\n"
"	padding: 10px 20px;\n"
"}\n"
"#frame_7  QPushButton:hover {\n"
"	background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 120, 0, 255), stop:1 rgba(0, 70, 0, 255));\n"
"}\n"
"#frame_7  QPushButton:pressed {\n"
"	background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 80, 0, 255), stop:1 rgba(0, 40, 0, 255));\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_arquea = QPushButton(self.frame_7)
        self.btn_arquea.setObjectName(u"btn_arquea")
        self.btn_arquea.setMaximumSize(QSize(200, 50))
        self.btn_arquea.setAutoFillBackground(False)

        self.horizontalLayout_10.addWidget(self.btn_arquea)

        self.btn_github = QPushButton(self.frame_7)
        self.btn_github.setObjectName(u"btn_github")
        self.btn_github.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_10.addWidget(self.btn_github)


        self.horizontalLayout_9.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_sobre)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_frame)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.toolBox_usinas.setCurrentIndex(0)
        self.toolBox_usinas.layout().setSpacing(6)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons_/ARQUEA.png\"/></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"USINAS", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/C:/Workspace/Python/ProjetoAPP/icons/menu-bar.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons_/logo_arquea_completo.png\"/></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons_/logo-FS.png\"/></p></body></html>", None))
        self.toolBox_usinas.setItemText(self.toolBox_usinas.indexOf(self.USINAS_page), QCoreApplication.translate("MainWindow", u"USINAS", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"SELECIONAR CAR", None))
        self.toolBox_usinas.setItemText(self.toolBox_usinas.indexOf(self.page_CAR), QCoreApplication.translate("MainWindow", u"CAR", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Gerar Shape SRS", None))
        self.toolBox_usinas.setItemText(self.toolBox_usinas.indexOf(self.SRS_page), QCoreApplication.translate("MainWindow", u"SRS", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Gerar shape LRV", None))
        self.toolBox_usinas.setItemText(self.toolBox_usinas.indexOf(self.LRV_page), QCoreApplication.translate("MainWindow", u"LRV", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Codigo Sup", None))
        self.toolBox_usinas.setItemText(self.toolBox_usinas.indexOf(self.PDL_page), QCoreApplication.translate("MainWindow", u"PDL", None))
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
        self.btn_selectCAR_SRS.setText(QCoreApplication.translate("MainWindow", u"Selecionar SRS", None))
        self.btn_selectCAR_LRV.setText(QCoreApplication.translate("MainWindow", u"Selecionar LRV", None))
        self.btn_exportCAR.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.label_aguarde.setText(QCoreApplication.translate("MainWindow", u"Aguarde...", None))
        self.btn_back_2.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_car_3), QCoreApplication.translate("MainWindow", u"CAR", None))
        self.btn_planilha_dados.setText(QCoreApplication.translate("MainWindow", u"Buscar Planilha", None))
        self.btn_filtrar.setText(QCoreApplication.translate("MainWindow", u"Filtros", None))
        self.btn_okfilter.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.btn_back_3.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"DADOS DE ENTRADA SRS", None))
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
        self.btn_CSV.setText(QCoreApplication.translate("MainWindow", u"CSV Demonst.", None))
        self.btn_back_1.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_safra), QCoreApplication.translate("MainWindow", u"SAFRA", None))
        self.btn_planilha_dados_LRV.setText(QCoreApplication.translate("MainWindow", u"Buscar Planilha", None))
        self.btn_filtrar_LRV.setText(QCoreApplication.translate("MainWindow", u"Filtros", None))
        self.btn_okfilter_LRV.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.btn_back_LRV_1.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"DADOS DE ENTRADA LRV", None))
        ___qtablewidgetitem26 = self.tableWidget_LRVsafra.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"COD_PRODUT", None));
        ___qtablewidgetitem27 = self.tableWidget_LRVsafra.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"PLANT_USIN", None));
        ___qtablewidgetitem28 = self.tableWidget_LRVsafra.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"NOM_PRODUT", None));
        ___qtablewidgetitem29 = self.tableWidget_LRVsafra.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"CPF_CNPJ", None));
        ___qtablewidgetitem30 = self.tableWidget_LRVsafra.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ANO_SAFRA", None));
        ___qtablewidgetitem31 = self.tableWidget_LRVsafra.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"TIPO", None));
        ___qtablewidgetitem32 = self.tableWidget_LRVsafra.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"COD_IMOVEL", None));
        ___qtablewidgetitem33 = self.tableWidget_LRVsafra.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"COD_MAPA", None));
        ___qtablewidgetitem34 = self.tableWidget_LRVsafra.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem35 = self.tableWidget_LRVsafra.horizontalHeaderItem(9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"DATA_REGIS", None));
        ___qtablewidgetitem36 = self.tableWidget_LRVsafra.horizontalHeaderItem(10)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"SITUACAO", None));
        ___qtablewidgetitem37 = self.tableWidget_LRVsafra.horizontalHeaderItem(11)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"AREA_TOTAL", None));
        ___qtablewidgetitem38 = self.tableWidget_LRVsafra.horizontalHeaderItem(12)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"AREA_MAPA", None));
        ___qtablewidgetitem39 = self.tableWidget_LRVsafra.horizontalHeaderItem(13)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"SUPRESSAO", None));
        ___qtablewidgetitem40 = self.tableWidget_LRVsafra.horizontalHeaderItem(14)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"ELEGIBILID", None));
        self.importDataSafra_LRV.setText(QCoreApplication.translate("MainWindow", u"Importar Dados", None))
        self.exportSHPSafra_LRV.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.btn_CSV2.setText(QCoreApplication.translate("MainWindow", u"CSV Demonst.", None))
        self.btn_back_LRV_3.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_safra_2), QCoreApplication.translate("MainWindow", u"SAFRA", None))
        ___qtablewidgetitem41 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"COD_SUPR", None));
        ___qtablewidgetitem42 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"NOM_PRODUT", None));
        ___qtablewidgetitem43 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"CAR", None));
        ___qtablewidgetitem44 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"SUP_PERIOD", None));
        ___qtablewidgetitem45 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"DATA_SUP", None));
        ___qtablewidgetitem46 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"INSER_2021", None));
        ___qtablewidgetitem47 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"INSER_2022", None));
        ___qtablewidgetitem48 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"INSER_2023", None));
        ___qtablewidgetitem49 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"ATIV_RENOV", None));
        ___qtablewidgetitem50 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"OBS 1", None));
        ___qtablewidgetitem51 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"OBS 2", None));
        ___qtablewidgetitem52 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"AREA_SUPR", None));
        ___qtablewidgetitem53 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"ANO_SUP", None));
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"Importar Planilha", None))
        self.btn_importshp.setText(QCoreApplication.translate("MainWindow", u"Importar Shapefile", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar Codigo", None))
        self.btn_saved.setText(QCoreApplication.translate("MainWindow", u"Salvar em .xlsx", None))
        self.btn_savedshp.setText(QCoreApplication.translate("MainWindow", u" Salvar em Shapefile ", None))
        self.btn_back_SUP.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
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
        self.btn_arquea.setText(QCoreApplication.translate("MainWindow", u"Site ARQUEA", None))
        self.btn_github.setText(QCoreApplication.translate("MainWindow", u"Projeto no GITHUB", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ArqueaConnect\u00a9", None))
    # retranslateUi

