from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget
from PyQt5.QtCore import Qt, QEvent, QObject, QTimer,  pyqtSlot, QDateTime
from PyQt5.QtGui import QIcon, QPixmap

from form.mainWindow_ui import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # 设置按钮的边框不可见
        self.pushButton.setFlat(True)
        self.pushButton_4.setFlat(True)
        self.pushButton_5.setFlat(True)

        # 设置大小和样式
        self.label.setPixmap(QPixmap('src/image/BRAIN SIMULATION.png'))
        self.pushButton_3.setIcon(QIcon('src/icon/pause.png'))
        self.label_9.setPixmap(QPixmap('src/icon/volume-on.png'))
        self.label_3.setPixmap(QPixmap('src/icon/setting.png'))
        self.pushButton_11.setIcon(QIcon('src/icon/file.png'))
        self.label_20.setPixmap(QPixmap('src/icon/collect.png'))
        self.pushButton_11.resize(35, 25)

        self.label.setGeometry(60, 30, 100, 100)
        self.label.setScaledContents(True)  # 设置缩放
        self.label_2.setGeometry(50, 150, 131, 16)

        # 初始化视频播放器
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.widget)
        self.horizontalSlider_2.setValue(20)
        self.player.setVolume(self.horizontalSlider_2.value())
        self.signalBindSlot()
        self.widget.installEventFilter(self)

        # 设置相关
        curDateTime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(curDateTime)
        self.spinBox.setValue(20)
        self.radioButton.setChecked(True)
        self.lineEdit.setPlaceholderText("实验描述")
        self.lineEdit_2.setPlaceholderText("名字缩写")

    def signalBindSlot(self):
        """
             信号和槽函数绑定
        """
        self.pushButton.clicked.connect(self.switchPage)
        self.pushButton_4.clicked.connect(self.switchPage)
        self.pushButton_5.clicked.connect(self.switchPage)

        # 播放器相关槽函数绑定：按钮
        self.pushButton_2.clicked.connect(self.selectVideo)
        self.pushButton_3.clicked.connect(self.playPause)
        self.pushButton_9.clicked.connect(self.fullScreen)

        # 进度条
        self.player.durationChanged.connect(self.getDuration)
        self.player.positionChanged.connect(self.getPosition)
        self.horizontalSlider.sliderMoved.connect(self.updatePosition)
        self.horizontalSlider_2.valueChanged.connect(self.setVolumeFunc)

        # # 设置相关
        # self.pushButton_11.clicked.connect(self.selectPath)
        # self.pushButton_6.clicked.connect(self.confirmSetting)
        # self.pushButton_7.clicked.connect(self.resetSetting)

    def switchPage(self):
        """
            tabWidget切换页码
        """

        button = self.sender()

        # 切换页面
        if button == self.pushButton:
            print(1)
            self.stackedWidget.setCurrentIndex(0)
        elif button == self.pushButton_4:
            print(2)
            self.stackedWidget.setCurrentIndex(1)
        elif button == self.pushButton_5:
            print(3)
            self.stackedWidget.setCurrentIndex(2)
        elif button == self.pushButton_6:
            self.stackedWidget.setCurrentIndex(3)
        elif button == self.pushButton_7:
            self.stackedWidget.setCurrentIndex(4)
        elif button == self.pushButton_8:
            self.stackedWidget.setCurrentIndex(5)

    def selectVideo(self):
        """
        选择视频按钮的槽函数
        """
        selected_video = QFileDialog.getOpenFileUrl(filter="Video files (*.mp4 *.avi *.mkv)")[0]
        if not selected_video.isEmpty():
            self.player.setMedia(QMediaContent(selected_video))
            self.player.play()

    def playPause(self):
        """
        播放/暂停视频
        """
        if self.player.state() == 1:
            self.pushButton_3.setIcon(QIcon('src/icon/play.png'))
            self.player.pause()
        else:
            self.pushButton_3.setIcon(QIcon('src/icon/pause.png'))
            self.player.play()

    def setVolumeFunc(self):
        """
        设置音量
        """
        self.player.setVolume(self.horizontalSlider_2.value())

    def getDuration(self, d):
        """
        视频总时长获取
        :param d: 获取到的视频总时长（ms）
        """
        self.horizontalSlider.setRange(0, d)
        self.horizontalSlider.setEnabled(True)
        self.displayTime(d)

        total_hours = int(d / 3600000)
        total_minutes = int((d - total_hours * 3600000) / 60000)
        total_seconds = int((d - total_hours * 3600000 - total_minutes * 60000) / 1000)
        total_time_str = '{:02d}:{:02d}:{:02d}'.format(total_hours, total_minutes, total_seconds)
        self.label_11.setText(total_time_str)

    def getPosition(self, p):
        """
        视频实时位置获取
        :param p: 视频实时位置
        """
        self.horizontalSlider.setValue(p)
        self.displayTime(p)

    def displayTime(self, ms):
        """
        显示剩余时间
        :param ms: 剩余时间
        """
        hours = int(ms / 3600000)
        minutes = int((ms - hours * 3600000) / 60000)
        seconds = int((ms - hours * 3600000 - minutes * 60000) / 1000)
        time_str = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        self.label_10.setText(time_str)

    def updatePosition(self, v):
        """
        用进度条更新视频位置
        :param v: 进度条拖动的位置
        """
        self.player.setPosition(v)
        self.displayTime(self.horizontalSlider.maximum() - v)

    def fullScreen(self):
        """
            设置全屏
        """
        self.widget.setFullScreen(True)

    def selectPath(self):
        """
            选择保存路径
        """
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.DirectoryOnly)
        path = file_dialog.getExistingDirectory()
        self.lineEdit_3.setText(path)

    def confirmSetting(self):
        """
            设置确认，设置保存路径
        """
        settingDescription = self.lineEdit.text()
        subjectNum = self.lineEdit_2.text()
        if settingDescription == '':
            settingDescription = '实验描述'
        if subjectNum == '':
            subjectNum = '受试者编号'

        sex = '男'
        if self.radioButton.isChecked():
            sex = '男'
        if self.radioButton_2.isChecked():
            sex = '女'

        matFile, npyFile = False, True   # 如果不选的话，默认是保存为.npy文件
        if self.checkBox.isChecked():
            matFile = True
        if self.checkBox_2.isChecked():
            npyFile = True

        expTime = self.dateTimeEdit.text()
        datetime_obj = QDateTime.fromString(expTime, 'yyyy/MM/dd HH:mm')
        expTime = datetime_obj.toString('yyyy_MM_dd_HH_mm')

        father_path = self.lineEdit_3.text()
        if father_path != '':
            father_path = father_path + '/'

        matFileName, npyFileName = '', ''
        if matFile:
            matFileName = father_path + settingDescription + '-' + subjectNum + '-' + sex + '-' + expTime + '.mat'
        if npyFile:
            npyFileName = father_path + settingDescription + '-' + subjectNum + '-' + sex + '-' + expTime + '.npy'

        print(matFileName)
        print(npyFileName)

    def resetSetting(self):
        curDateTime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(curDateTime)
        self.spinBox.setValue(20)
        self.radioButton.setChecked(True)
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')

    def eventFilter(self, watched, event):
        """
            事件过滤器，设置打开或者关闭全屏
        """
        if watched != self.widget:
            return super().eventFilter(watched, event)

        # 鼠标左键按下时，暂停或继续播放
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                if self.player.state() == QMediaPlayer.PlayingState:
                    self.player.pause()
                    self.pushButton_3.setIcon(QIcon('src/icon/play.png'))
                else:
                    self.player.play()
                    self.pushButton_3.setIcon(QIcon('src/icon/pause.png'))

        # 全屏状态时，按ESC键退出全屏
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Escape:
                if self.widget.isFullScreen():
                    self.widget.setFullScreen(False)
                    self.widget.setGeometry(20, 13, 1011, 391)

        # 双击事件，打开或关闭全屏
        if event.type() == QEvent.MouseButtonDblClick:
            if event.button() == Qt.LeftButton:
                if not self.widget.isFullScreen():
                    self.widget.setFullScreen(True)
                else:
                    self.widget.setFullScreen(False)
                    self.widget.setGeometry(20, 13, 1011, 391)

        return super().eventFilter(watched, event)

