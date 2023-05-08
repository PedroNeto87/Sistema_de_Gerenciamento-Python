# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 578)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 10);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 35))
        font = QFont()
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_pg_importar = QPushButton(self.frame)
        self.btn_pg_importar.setObjectName(u"btn_pg_importar")
        self.btn_pg_importar.setMinimumSize(QSize(0, 35))
        self.btn_pg_importar.setFont(font)
        self.btn_pg_importar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_importar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")

        self.horizontalLayout.addWidget(self.btn_pg_importar)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 35))
        self.btn_tables.setFont(font)
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 35))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 35))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")

        self.horizontalLayout.addWidget(self.btn_contato)


        self.verticalLayout.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy)
        self.Pages.setCursor(QCursor(Qt.PointingHandCursor))
        self.Pages.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_3 = QVBoxLayout(self.pg_home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(0, 80, 121);")

        self.verticalLayout_3.addWidget(self.label)

        self.btn_pg_cadastro = QPushButton(self.pg_home)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setMinimumSize(QSize(0, 27))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_pg_cadastro.setFont(font1)
        self.btn_pg_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastro.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	 color:black\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_pg_cadastro)

        self.Pages.addWidget(self.pg_home)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.verticalLayout_10 = QVBoxLayout(self.pg_import)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_17 = QLabel(self.pg_import)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(20)
        self.label_17.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_17)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_file = QLineEdit(self.pg_import)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 28))
        font3 = QFont()
        font3.setPointSize(12)
        self.txt_file.setFont(font3)
        self.txt_file.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_file)

        self.btn_open_2 = QPushButton(self.pg_import)
        self.btn_open_2.setObjectName(u"btn_open_2")
        self.btn_open_2.setMinimumSize(QSize(120, 28))
        self.btn_open_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-top-right-radius: 15px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(170, 255, 255);\n"
"	 color:black\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_open_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.pg_import)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.btn_import = QPushButton(self.pg_import)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(0, 28))
        self.btn_import.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(170, 255, 255);\n"
"	 color:black\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_import)

        self.label_5 = QLabel(self.pg_import)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.progressBar = QProgressBar(self.pg_import)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font-size: 12px;\n"
"background-color: rgb(0, 70, 121);\n"
"\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_10.addWidget(self.progressBar)

        self.Pages.addWidget(self.pg_import)
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_2 = QVBoxLayout(self.pg_table)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tb_base = QTabWidget(self.pg_table)
        self.tb_base.setObjectName(u"tb_base")
        self.tb_base.setCursor(QCursor(Qt.PointingHandCursor))
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_8 = QVBoxLayout(self.tables)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_6.addWidget(self.tw_estoque)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")

        self.verticalLayout_5.addWidget(self.tw_saida)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_gerar = QPushButton(self.frame_2)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(100, 27))
        self.btn_gerar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
" 	color:black\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_gerar)

        self.btn_estorno = QPushButton(self.frame_2)
        self.btn_estorno.setObjectName(u"btn_estorno")
        self.btn_estorno.setMinimumSize(QSize(100, 27))
        self.btn_estorno.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estorno.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
" 	color:black\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_estorno)

        self.btn_importar = QPushButton(self.frame_2)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setMinimumSize(QSize(100, 27))
        self.btn_importar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
" 	color:black\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_importar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.tb_base.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_11.addWidget(self.label_18)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_chart = QPushButton(self.tab_2)
        self.btn_chart.setObjectName(u"btn_chart")
        self.btn_chart.setMinimumSize(QSize(0, 28))
        self.btn_chart.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
" 	color:black\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_chart)

        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 28))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
" 	color:black\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_excel)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setFont(font3)
        self.txt_filtro.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.txt_filtro)

        self.tb_estoque = QTableView(self.tab_2)
        self.tb_estoque.setObjectName(u"tb_estoque")

        self.verticalLayout_11.addWidget(self.tb_estoque)

        self.tb_base.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tb_base)

        self.Pages.addWidget(self.pg_table)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_16 = QLabel(self.pg_sobre)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMaximumSize(QSize(16777215, 80))
        self.label_16.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_16)

        self.label_19 = QLabel(self.pg_sobre)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_19)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_13 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_15 = QLabel(self.pg_contato)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_15)

        self.label_32 = QLabel(self.pg_contato)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_13.addWidget(self.label_32)

        self.label_31 = QLabel(self.pg_contato)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_13.addWidget(self.label_31)

        self.label_20 = QLabel(self.pg_contato)
        self.label_20.setObjectName(u"label_20")
        font4 = QFont()
        font4.setPointSize(16)
        self.label_20.setFont(font4)

        self.verticalLayout_13.addWidget(self.label_20)

        self.label_36 = QLabel(self.pg_contato)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_13.addWidget(self.label_36)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_26 = QLabel(self.pg_contato)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_18.addWidget(self.label_26)

        self.label_21 = QLabel(self.pg_contato)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 16777215))
        self.label_21.setFont(font4)

        self.horizontalLayout_18.addWidget(self.label_21)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer)


        self.verticalLayout_13.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_27 = QLabel(self.pg_contato)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"background-color: rgb(0, 80, 121);")

        self.horizontalLayout_16.addWidget(self.label_27)

        self.label_22 = QLabel(self.pg_contato)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)

        self.horizontalLayout_16.addWidget(self.label_22)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_28 = QLabel(self.pg_contato)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_15.addWidget(self.label_28)

        self.lbl_instagram = QLabel(self.pg_contato)
        self.lbl_instagram.setObjectName(u"lbl_instagram")
        self.lbl_instagram.setFont(font4)
        self.lbl_instagram.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_15.addWidget(self.lbl_instagram)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_15)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_3)

        self.label_33 = QLabel(self.pg_contato)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_20.addWidget(self.label_33)


        self.verticalLayout_13.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_29 = QLabel(self.pg_contato)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_14.addWidget(self.label_29)

        self.lbl_github = QLabel(self.pg_contato)
        self.lbl_github.setObjectName(u"lbl_github")
        self.lbl_github.setFont(font4)

        self.horizontalLayout_14.addWidget(self.lbl_github)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_14)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)

        self.label_34 = QLabel(self.pg_contato)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_21.addWidget(self.label_34)


        self.verticalLayout_13.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_30 = QLabel(self.pg_contato)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_13.addWidget(self.label_30)

        self.lbl_linkdin = QLabel(self.pg_contato)
        self.lbl_linkdin.setObjectName(u"lbl_linkdin")
        self.lbl_linkdin.setFont(font4)

        self.horizontalLayout_13.addWidget(self.lbl_linkdin)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_13)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_5)

        self.label_35 = QLabel(self.pg_contato)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_22.addWidget(self.label_35)


        self.verticalLayout_13.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.Pages.addWidget(self.pg_contato)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(10)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(25, -1, 25, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom:1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85, 115, 155, 0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_9.addWidget(self.txt_nome)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(25, -1, 25, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom:1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85, 115, 155, 0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_8.addWidget(self.txt_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(25, -1, 25, -1)
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom:1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85, 115, 155, 0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(25, -1, 25, -1)
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom:1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85, 115, 155, 0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(25, -1, 25, -1)
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy2)
        self.cb_perfil.setFont(font1)
        self.cb_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_perfil.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.cb_perfil)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        self.btn_cadastrar.setFont(font6)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 10);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
" 	color:black\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.Pages.addWidget(self.pg_cadastro)

        self.verticalLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tb_base.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_pg_importar.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">PEDRO_NETO</span></p><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">Sistema de Gerenciamento</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><img src=\"imgs/logo.png\"/></span></p></body></html>", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">IMPORTAR XML</span></p></body></html>", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com os arquivos XML ------>", None))
        self.btn_open_2.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_4.setText("")
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_5.setText("")
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Estoque</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Valor NFe", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Esp\u00e9cie", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"UN", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"C\u00f3d. Item", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"NFe", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Sa\u00edda</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Data Sa\u00edda", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"NFe", None));
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.btn_importar.setText("")
        self.tb_base.setTabText(self.tb_base.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Estoque</span></p></body></html>", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Sobre</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Esse sistema faz a importa\u00e7\u00e3o de arquivos XML e faz o controle de estoque de acordo com a entrada de notas e sa\u00eddas apontadas pelo usu\u00e1rio.</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Desenvolvido no curso Sistema de Gerenciamento com Python e QT Designer pelo YouTube no canal PyTax.</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Contatos</span></p></body></html>", None))
        self.label_32.setText("")
        self.label_31.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Desenvolvedor: Pedro Neto</span></p></body></html>", None))
        self.label_36.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"imgs/whatss.png\"/></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">(31)99398-8562</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"imgs/e_mail.png\"/></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">pedrofcn01@hotmail.com</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"imgs/instagram.png\"/></p></body></html>", None))
        self.lbl_instagram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://www.instagram.com/pedrofcn/\"><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">https://www.instagram.com/pedrofcn/</span></a></p></body></html>", None))
        self.label_33.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"imgs/github.png\"/></p></body></html>", None))
        self.lbl_github.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/PedroNeto87\"><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">https://github.com/PedroNeto87</span></a></p></body></html>", None))
        self.label_34.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"imgs/linkdin_nova.png\"/></p></body></html>", None))
        self.lbl_linkdin.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://www.linkedin.com/in/pedro-ferreira-cunha-neto/\"><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">https://www.linkedin.com/in/pedro-ferreira-cunha-neto/</span></a></p></body></html>", None))
        self.label_35.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Tela de Cadastro</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"imgs/user.png\"/></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Cadastrar Usu\u00e1rio</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Nome:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Usu\u00e1rio:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Repete senha:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Perfil:</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
    # retranslateUi

