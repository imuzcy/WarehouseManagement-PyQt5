# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 60, 781, 471))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 30, 781, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.title_LogIn = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.title_LogIn.setFont(font)
        self.title_LogIn.setObjectName("title_LogIn")
        self.horizontalLayout_2.addWidget(self.title_LogIn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_LogIn = QtWidgets.QPushButton(self.page)
        self.btn_LogIn.setGeometry(QtCore.QRect(320, 380, 141, 41))
        self.btn_LogIn.setObjectName("btn_LogIn")
        self.lbl_UserName = QtWidgets.QLabel(self.page)
        self.lbl_UserName.setGeometry(QtCore.QRect(150, 190, 71, 51))
        self.lbl_UserName.setObjectName("lbl_UserName")
        self.lbl_PassWord = QtWidgets.QLabel(self.page)
        self.lbl_PassWord.setGeometry(QtCore.QRect(150, 280, 81, 51))
        self.lbl_PassWord.setObjectName("lbl_PassWord")
        self.le_UserName = QtWidgets.QLineEdit(self.page)
        self.le_UserName.setGeometry(QtCore.QRect(240, 200, 301, 41))
        self.le_UserName.setObjectName("le_UserName")
        self.le_PassWord = QtWidgets.QLineEdit(self.page)
        self.le_PassWord.setGeometry(QtCore.QRect(240, 290, 301, 41))
        self.le_PassWord.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_PassWord.setObjectName("le_PassWord")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_2)
        self.stackedWidget_2.setGeometry(QtCore.QRect(10, 70, 761, 401))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.tableWidget = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 751, 381))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 20, 751, 381))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page_5)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 20, 761, 381))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.stackedWidget_2.addWidget(self.page_5)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 781, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btn_search_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_search_1.setObjectName("btn_search_1")
        self.horizontalLayout_3.addWidget(self.btn_search_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_search_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_search_2.setObjectName("btn_search_2")
        self.horizontalLayout_3.addWidget(self.btn_search_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btn_search_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_search_3.setObjectName("btn_search_3")
        self.horizontalLayout_3.addWidget(self.btn_search_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 781, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(2)
        self.btn_LogIn.clicked.connect(MainWindow.btn_LogIn_onClicked)
        self.btn_search_1.clicked.connect(MainWindow.btn_search1_onClicked)
        self.btn_search_2.clicked.connect(MainWindow.btn_search2_onClicked)
        self.btn_search_3.clicked.connect(MainWindow.btn_search3_onClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "仓库管理系统"))
        self.title_LogIn.setText(_translate("MainWindow", "登录界面"))
        self.btn_LogIn.setText(_translate("MainWindow", "登录"))
        self.lbl_UserName.setText(_translate("MainWindow", "账号:"))
        self.lbl_PassWord.setText(_translate("MainWindow", "密码:"))
        self.btn_search_1.setText(_translate("MainWindow", "查询一"))
        self.btn_search_2.setText(_translate("MainWindow", "查询二"))
        self.btn_search_3.setText(_translate("MainWindow", "查询三"))
        self.label.setText(_translate("MainWindow", "仓库管理系统"))