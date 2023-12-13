# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1268, 830)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 222, 851))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 190, 221, 156))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"    text-align: right; \n"
"padding-right: 40px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#pushButton:focus{\n"
"    border:1px solid white;\n"
"    background-color: white;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 345, 221, 156))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"#pushButton_4:focus{\n"
"    border:1px solid white;\n"
"    background-color: white;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.buttonGroup.addButton(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 500, 221, 161))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("\n"
"#pushButton_5:focus{\n"
"    border:1px solid white;\n"
"    background-color: white;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.buttonGroup.addButton(self.pushButton_5)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 50, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 190, 220, 1))
        self.frame_2.setStyleSheet("QFrame {\n"
"    border: none;\n"
"    background-color: #C0C0C0;\n"
"    height: 1px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 660, 220, 1))
        self.frame_3.setStyleSheet("QFrame {\n"
"    border: none;\n"
"    background-color: #C0C0C0;\n"
"    height: 1px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(20, 243, 54, 50))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("../src/icon/collect.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(220, 0, 1051, 851))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("#stackedWidget{\n"
"    background-color: white;\n"
"}")
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setMidLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(870, 430, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QVideoWidget(self.page)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(20, 13, 1011, 391))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: black;\n"
"}")
        self.widget.setObjectName("widget")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(80, 435, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.page)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(740, 433, 111, 18))
        self.horizontalSlider_2.setStyleSheet("QSlider {\n"
"    padding-left: 0;  /* 左侧端点离左边的距离 */\n"
"    padding-right: 0;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color: #7A7B79;\n"
"    height: 5px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #FF7826;\n"
"    height: 5px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background: transparent;\n"
"    height: 6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0px -4px 0px;\n"
"    border-radius: 7px;\n"
"    background: white;\n"
"}")
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setTracking(True)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(700, 427, 30, 30))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../src/icon/volume.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.horizontalSlider = QtWidgets.QSlider(self.page)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 403, 1011, 18))
        self.horizontalSlider.setStyleSheet("QSlider {\n"
"    background-color: black;\n"
"    padding-left: 15px;  /* 左侧端点离左边的距离 */\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color: #7A7B79;\n"
"    height: 5px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #FF7826;\n"
"    height: 5px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background: transparent;\n"
"    height: 6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0px -4px 0px;\n"
"    border-radius: 7px;\n"
"    background: white;\n"
"}")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 428, 61, 31))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/icon/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(160, 435, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(150, 435, 8, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_9 = QtWidgets.QPushButton(self.page)
        self.pushButton_9.setGeometry(QtCore.QRect(950, 430, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.frame_31 = QtWidgets.QFrame(self.page)
        self.frame_31.setGeometry(QtCore.QRect(380, 470, 651, 331))
        self.frame_31.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_31.setObjectName("frame_31")
        self.frame_4 = QtWidgets.QFrame(self.page)
        self.frame_4.setGeometry(QtCore.QRect(20, 470, 341, 331))
        self.frame_4.setStyleSheet("QFrame{\n"
"\n"
"border-radius:10px; \n"
"background-color:#F0F0F0;\n"
"border-width: 0.5px;\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton.setGeometry(QtCore.QRect(150, 110, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_2.setGeometry(QtCore.QRect(230, 110, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.spinBox.setGeometry(QtCore.QRect(150, 150, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setSuffix("")
        self.spinBox.setObjectName("spinBox")
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox.setGeometry(QtCore.QRect(150, 180, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 253, 31, 21))
        self.pushButton_11.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../src/icon/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setObjectName("pushButton_11")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_2.setGeometry(QtCore.QRect(220, 180, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 253, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 290, 61, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 290, 61, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 80, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 25, 25))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../src/icon/setting.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame_4)
        self.dateTimeEdit.setGeometry(QtCore.QRect(150, 220, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.widget1 = QtWidgets.QWidget(self.frame_4)
        self.widget1.setGeometry(QtCore.QRect(10, 40, 91, 241))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel {\n"
"    border-style: none;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel {\n"
"    border-style: none;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("QLabel {\n"
"    border-style: none;\n"
"}")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel {\n"
"    border-style: none;\n"
"}")
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_18 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel {\n"
"    border-style: none;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("QLabel {\n"
"    border-style: none;\n"
"}")
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.label_17 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel {\n"
"    border-style: none;\n"
"}")
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.frame_4.raise_()
        self.pushButton_2.raise_()
        self.widget.raise_()
        self.label_10.raise_()
        self.horizontalSlider_2.raise_()
        self.label_9.raise_()
        self.horizontalSlider.raise_()
        self.pushButton_3.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.pushButton_9.raise_()
        self.frame_3.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(480, 310, 54, 16))
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(250, 350, 54, 16))
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_7 = QtWidgets.QLabel(self.page_5)
        self.label_7.setGeometry(QtCore.QRect(250, 310, 54, 16))
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_8 = QtWidgets.QLabel(self.page_6)
        self.label_8.setGeometry(QtCore.QRect(340, 450, 54, 16))
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(230, 390, 54, 16))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "信号采集"))
        self.pushButton_4.setText(_translate("Form", "数据分析"))
        self.pushButton_5.setText(_translate("Form", "在线检测"))
        self.label_2.setText(_translate("Form", "脑电采集平台"))
        self.pushButton_2.setText(_translate("Form", "选择视频"))
        self.label_10.setText(_translate("Form", "00:00:00"))
        self.label_11.setText(_translate("Form", "00:00:00"))
        self.label_12.setText(_translate("Form", "/"))
        self.pushButton_9.setText(_translate("Form", "全屏播放"))
        self.radioButton.setText(_translate("Form", "男"))
        self.radioButton_2.setText(_translate("Form", "女"))
        self.checkBox.setText(_translate("Form", ".mat"))
        self.checkBox_2.setText(_translate("Form", ".npy"))
        self.pushButton_6.setText(_translate("Form", "确定"))
        self.pushButton_7.setText(_translate("Form", "重置"))
        self.label_13.setText(_translate("Form", "实验描述"))
        self.label_14.setText(_translate("Form", "受试者编号"))
        self.label_15.setText(_translate("Form", "性别"))
        self.label_16.setText(_translate("Form", "年龄"))
        self.label_18.setText(_translate("Form", "保存格式"))
        self.label_19.setText(_translate("Form", "实验时间"))
        self.label_17.setText(_translate("Form", "保存路径"))
        self.label_5.setText(_translate("Form", "第三页"))
        self.label_6.setText(_translate("Form", "第四页"))
        self.label_7.setText(_translate("Form", "第五页"))
        self.label_8.setText(_translate("Form", "第六页"))
        self.label_4.setText(_translate("Form", "第二页"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
