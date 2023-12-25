import mne
import scipy
import os.path
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from controller.selfAssessmentControl import SelfAssessment
from form.mainWindow_ui import Ui_Form
from PyQt5.QtCore import Qt, QDateTime, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QImage
from controller.getRealTimeData import GetRealTimeData
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from utils.utils import loadRawData, MyFigure, handleVideoPlayerEvents
from PyQt5.QtWidgets import QFileDialog, QWidget, QGraphicsScene, QMessageBox


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.clip = 1  # 保存数据的片段
        self.selfAssessmentDialog = None
        self.fatherPath = None
        self.expTime = None
        self.npyFile = True
        self.matFile = False
        self.sex = '男'
        self.settingDescription = '测试实验'
        self.subjectName = '测试受试者'
        self.npyFileName = None
        self.matFileName = None
        self.info_eeg = None
        self.my_thread = None
        self.trial = 1
        self.scene = None
        self.datasetType = None  # 展示数据的时候，加载的数据集类型
        self.filePath = None
        self.setupUi(self)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # 禁用最大化和拖拉
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.size())

        # 设置初始tab
        self.pushButton.setStyleSheet("border:1px solid transparent; background-color: white;text-align: "
                                      "right;padding-right: 40px;")
        self.pushButton_4.setStyleSheet("border:1px solid transparent; background-color: transparent; text-align: "
                                        "right; padding-right: 40px;")
        self.pushButton_5.setStyleSheet("border:1px solid transparent; background-color: transparent; text-align: "
                                        "right; padding-right: 40px;")
        self.stackedWidget.setCurrentIndex(0)

        # 设置按钮的边框不可见
        self.pushButton.setFlat(True)
        self.pushButton_4.setFlat(True)
        self.pushButton_5.setFlat(True)

        # 设置大小和样式
        self.label.setPixmap(QPixmap('src/image/BRAIN SIMULATION.png'))
        self.pushButton_3.setIcon(QIcon('src/icon/pause.png'))
        self.pushButton_3.setToolTip('暂停/播放')
        self.label_9.setPixmap(QPixmap('src/icon/volume-on.png'))
        self.label_9.setToolTip('音量')
        self.label_3.setPixmap(QPixmap('src/icon/setting.png'))
        self.label_3.setToolTip('实验采集设置')
        self.pushButton_11.setIcon(QIcon('src/icon/file.png'))
        self.label_20.setPixmap(QPixmap('src/icon/collect.png'))
        self.label_21.setPixmap(QPixmap('src/icon/analysis.png'))
        self.label_22.setPixmap(QPixmap('src/icon/watching.png'))
        self.pushButton_2.setIcon(QIcon('src/icon/select.png'))
        self.pushButton_2.setToolTip('选择文件')
        self.pushButton_9.setIcon(QIcon('src/icon/full.png'))
        self.pushButton_9.setToolTip('全屏')
        self.pushButton_11.resize(35, 25)
        self.label_23.setPixmap(QPixmap('src/icon/signal.png'))
        self.label_23.setToolTip('波形实时显示')
        self.label_24.setPixmap(QPixmap('src/image/whut.png'))
        self.pushButton_8.setIcon(QIcon('src/icon/data.png'))
        self.comboBox.addItem('DEAP')
        self.comboBox.addItem('SEED')
        self.comboBox.addItem('DREAMER')
        self.comboBox.addItem('SELF')
        self.comboBox.setCurrentIndex(0)
        self.pushButton_18.setIcon(QIcon('src/icon/pause.png'))
        self.pushButton_18.setToolTip('暂停/播放')
        self.label_48.setPixmap(QPixmap('src/icon/volume-on.png'))
        self.label_48.setToolTip('音量')
        self.pushButton_20.setIcon(QIcon('src/icon/select.png'))
        self.pushButton_20.setToolTip('选择文件')
        self.pushButton_19.setIcon(QIcon('src/icon/full.png'))
        self.pushButton_19.setToolTip('全屏')

        # 初始化视频播放器
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.widget)
        self.horizontalSlider_2.setValue(20)
        self.player.setVolume(self.horizontalSlider_2.value())
        self.widget.installEventFilter(self)

        # 在线检测的播放器初始化
        self.player_2 = QMediaPlayer()
        self.player_2.setVideoOutput(self.widget_2)
        self.horizontalSlider_7.setValue(20)
        self.player_2.setVolume(self.horizontalSlider_7.value())
        self.widget_2.installEventFilter(self)

        # 设置相关
        curDateTime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(curDateTime)
        self.spinBox.setValue(20)
        self.radioButton.setChecked(True)
        self.lineEdit.setPlaceholderText("实验描述")
        self.lineEdit_2.setPlaceholderText("姓名缩写")

        # 摄像头相关
        self.cam = cv.VideoCapture()
        self.timerCamera = QTimer()
        self.label_4.setPixmap(QPixmap('src/icon/camera.png'))
        self.label_4.setToolTip('打开/关闭摄像头')
        self.label_49.setPixmap(QPixmap('src/icon/camera-open.png'))

        self.signalBindSlot()
        self.selectDateset()  # 开始调用一次选择数据集，默认选择DEAP数据集
        self.confirmSetting()  # 开始就调用一次确认选择，文件将按照默认进行保存

    def signalBindSlot(self):
        """
        信号和槽函数绑定
        :return:
        """
        self.pushButton.clicked.connect(self.switchPage)
        self.pushButton_4.clicked.connect(self.switchPage)
        self.pushButton_5.clicked.connect(self.switchPage)

        # 播放器相关槽函数绑定：按钮
        self.pushButton_2.clicked.connect(self.selectVideo)
        self.pushButton_3.clicked.connect(self.playPause)
        self.pushButton_9.clicked.connect(self.fullScreen)
        self.pushButton_20.clicked.connect(self.selectVideo)
        self.pushButton_18.clicked.connect(self.playPause)
        self.pushButton_19.clicked.connect(self.fullScreen)

        # 进度条
        self.player.durationChanged.connect(self.getDuration)
        self.player.positionChanged.connect(self.getPosition)
        self.horizontalSlider.sliderMoved.connect(self.updatePosition)
        self.horizontalSlider_2.valueChanged.connect(self.setVolumeFunc)
        self.player_2.durationChanged.connect(self.getDuration)
        self.player_2.positionChanged.connect(self.getPosition)
        self.horizontalSlider_3.sliderMoved.connect(self.updatePosition)
        self.horizontalSlider_7.valueChanged.connect(self.setVolumeFunc)

        # # 设置相关
        self.pushButton_11.clicked.connect(self.selectPath)
        self.pushButton_6.clicked.connect(self.confirmSetting)
        self.pushButton_7.clicked.connect(self.resetSetting)

        # 数据分析页面相关
        self.pushButton_8.clicked.connect(self.selectFile)
        self.comboBox.currentTextChanged.connect(self.selectDateset)
        self.comboBox_2.currentTextChanged.connect(self.selectTrial)

        # 摄像头相关
        self.label_49.clicked.connect(self.controlCamera)
        self.timerCamera.timeout.connect(self.refreshFrame)

    def switchPage(self):
        """
        tabWidget切换页码
        :return:
        """

        button = self.sender()

        # 切换页面
        if button == self.pushButton:
            self.pushButton.setStyleSheet("border:1px solid transparent; background-color: white;text-align: "
                                          "right;padding-right: 40px;")
            self.pushButton_4.setStyleSheet("border:1px solid transparent; background-color: transparent; text-align: "
                                            "right; padding-right: 40px;")
            self.pushButton_5.setStyleSheet("border:1px solid transparent; background-color: transparent; text-align: "
                                            "right; padding-right: 40px;")
            self.stackedWidget.setCurrentIndex(0)
        elif button == self.pushButton_4:
            self.pushButton_4.setStyleSheet("border:1px solid transparent; background-color: white;text-align: "
                                            "right;padding-right: 40px;")
            self.pushButton.setStyleSheet("border:1px solid transparent; background-color: transparent; text-align: "
                                          "right; padding-right: 40px;")
            self.pushButton_5.setStyleSheet("border:1px solid transparent; background-color: transparent; text-align: "
                                            "right; padding-right: 40px;")
            self.stackedWidget.setCurrentIndex(1)
        elif button == self.pushButton_5:
            self.pushButton_5.setStyleSheet("border:1px solid transparent; background-color: white;text-align: "
                                            "right;padding-right: 40px;")
            self.pushButton.setStyleSheet("border:1px solid transparent; background-color: transparent; text-align: "
                                          "right; padding-right: 40px;")
            self.pushButton_4.setStyleSheet("border:1px solid transparent; background-color: transparent; text-align: "
                                            "right; padding-right: 40px;")
            self.stackedWidget.setCurrentIndex(2)

    def selectVideo(self):
        """
        选择视频按钮的槽函数
        :return:
        """
        button = self.sender()

        if button == self.pushButton_2:
            selected_video = QFileDialog.getOpenFileUrl(filter="Video files (*.mp4 *.avi *.mkv)")[0]
            if not selected_video.isEmpty():
                self.player.setMedia(QMediaContent(selected_video))
                self.player.play()
                self.getSignal()
                self.setTimer()  # 设置定时器

        if button == self.pushButton_20:
            selected_video = QFileDialog.getOpenFileUrl(filter="Video files (*.mp4 *.avi *.mkv)")[0]
            if not selected_video.isEmpty():
                self.player_2.setMedia(QMediaContent(selected_video))
                self.player_2.play()

    def playPause(self):
        """
        播放/暂停视频
        :return:
        """

        button = self.sender()

        if button == self.pushButton_18:
            if self.player_2.state() == 1:
                self.pushButton_18.setIcon(QIcon('src/icon/play.png'))
                self.player_2.pause()
            else:
                self.pushButton_18.setIcon(QIcon('src/icon/pause.png'))
                self.player_2.play()

        else:
            if self.player.state() == 1:
                self.pushButton_3.setIcon(QIcon('src/icon/play.png'))
                self.player.pause()
            else:
                self.pushButton_3.setIcon(QIcon('src/icon/pause.png'))
                self.player.play()

    def setVolumeFunc(self):
        """
        设置音量
        :return:
        """
        horizontalSlider = self.sender()

        if horizontalSlider == self.horizontalSlider_2:
            self.player.setVolume(self.horizontalSlider_2.value())

        if horizontalSlider == self.horizontalSlider_7:
            self.player_2.setVolume(self.horizontalSlider_7.value())

    def getDuration(self, d):
        """
        视频总时长获取
        :param d: 获取到的视频总时长（ms）
        :return::return:
        """
        player = self.sender()

        if player == self.player:
            self.horizontalSlider.setRange(0, d)
            self.horizontalSlider.setEnabled(True)
            self.displayTime(d, player)

            total_hours = int(d / 3600000)
            total_minutes = int((d - total_hours * 3600000) / 60000)
            total_seconds = int((d - total_hours * 3600000 - total_minutes * 60000) / 1000)
            total_time_str = '{:02d}:{:02d}:{:02d}'.format(total_hours, total_minutes, total_seconds)
            self.label_11.setText(total_time_str)

        if player == self.player_2:
            self.horizontalSlider_3.setRange(0, d)
            self.horizontalSlider_3.setEnabled(True)
            self.displayTime(d, player)

            total_hours = int(d / 3600000)
            total_minutes = int((d - total_hours * 3600000) / 60000)
            total_seconds = int((d - total_hours * 3600000 - total_minutes * 60000) / 1000)
            total_time_str = '{:02d}:{:02d}:{:02d}'.format(total_hours, total_minutes, total_seconds)
            self.label_47.setText(total_time_str)

    def getPosition(self, p):
        """
        视频实时位置获取
        :param p: 视频实时位置
        :return:
        """
        player = self.sender()

        if player == self.player:
            self.horizontalSlider.setValue(p)
            self.displayTime(p, player)

        if player == self.player_2:
            self.horizontalSlider_3.setValue(p)
            self.displayTime(p, player)

    def displayTime(self, ms, player):
        """
        显示剩余时间
        :param player: 哪一个播放器
        :param ms: 剩余时间
        :return:
        """
        hours = int(ms / 3600000)
        minutes = int((ms - hours * 3600000) / 60000)
        seconds = int((ms - hours * 3600000 - minutes * 60000) / 1000)
        time_str = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

        if player == self.player:
            self.label_10.setText(time_str)

        if player == self.player_2:
            self.label_45.setText(time_str)

    def updatePosition(self, v):
        """
        用进度条更新视频位置
        :param v: 进度条拖动的位置
        :return:
        """
        horizontalSlider = self.sender()

        if horizontalSlider == self.horizontalSlider:
            self.player.setPosition(v)
            self.displayTime(self.horizontalSlider.maximum() - v, self.player)

        if horizontalSlider == self.horizontalSlider_3:
            self.player_2.setPosition(v)
            self.displayTime(self.horizontalSlider.maximum() - v, self.player_2)

    def fullScreen(self):
        """
        设置全屏
        :return:
        """
        button = self.sender()

        if button == self.pushButton_19:
            self.widget_2.setFullScreen(True)
        else:
            # 包括点击全屏和定时器全屏
            self.widget.setFullScreen(True)

    def closeFullScreen(self):
        if self.widget.isFullScreen():
            self.widget.setFullScreen(False)
            self.widget.setGeometry(20, 13, 1011, 391)

    def selectPath(self):
        """
        选择保存路径
        :return:
        """
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.DirectoryOnly)
        path = file_dialog.getExistingDirectory()
        self.lineEdit_3.setText(path)

    def confirmSetting(self):
        """
        设置确认，设置保存路径
        :return:
        """
        button = self.sender()
        self.settingDescription = self.lineEdit.text() if self.lineEdit.text() else self.settingDescription
        self.subjectName = self.lineEdit_2.text() if self.lineEdit_2.text() else self.subjectName

        if self.radioButton.isChecked():
            self.sex = '男'
        if self.radioButton_2.isChecked():
            self.sex = '女'

        if self.checkBox.isChecked():
            self.matFile = True
        if self.checkBox_2.isChecked():
            self.npyFile = True

        expTime = self.dateTimeEdit.text()
        if expTime != '':
            datetimeObj = QDateTime.fromString(expTime, 'yyyy/MM/dd HH:mm')
            self.expTime = datetimeObj.toString('yyyy_MM_dd_HH_mm')

        self.fatherPath = self.lineEdit_3.text()
        if self.matFile:
            self.matFileName = os.path.join(self.fatherPath,
                                            f"{self.settingDescription}-{self.subjectName}-{self.sex}-{self.expTime}")
        if self.npyFile:
            self.npyFileName = os.path.join(self.fatherPath,
                                            f"{self.settingDescription}-{self.subjectName}-{self.sex}-{self.expTime}")

        if self.matFileName:
            self.matFileName = os.path.normpath(self.matFileName)
        if self.npyFileName:
            self.npyFileName = os.path.normpath(self.npyFileName)

        if button == self.pushButton_6:
            self.pushButton_6.setIcon(QIcon('src/icon/confirm.png'))

    def resetSetting(self):
        """
        清除设置
        :return:
        """
        curDateTime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(curDateTime)
        self.spinBox.setValue(20)
        self.radioButton.setChecked(True)
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.pushButton_6.setIcon(QIcon())

    def selectFile(self):
        """
        选择需要分析的数据文件
        :return:
        """
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # 可以选择只读文件
        filePath, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'raw files(*.npy *.mat *.hdf5 *.dat)',
                                                  options=options)
        if filePath:
            self.filePath = filePath
            self.datasetType = self.comboBox.currentText()
            self.showAll()

    def showAll(self):
        """
        三个画布显示分析的结果
        :return:
        """
        rawEEG, ica = loadRawData(self.filePath, self.datasetType, self.trial)
        chTimeFig = rawEEG.plot(duration=4, n_channels=8, clipping=None, scalings=100, show=False)
        self.putFig(MyFigure(chTimeFig), self.graphicsView)
        plt.close()
        icaFig = ica.plot_components(nrows=2, ncols=2, show=False)
        self.putFig(MyFigure(icaFig), self.graphicsView_2)
        plt.close()
        psdFig = rawEEG.plot_psd(show=False, color='white')
        self.putFig(MyFigure(psdFig), self.graphicsView_3)
        plt.close()

    def selectDateset(self):
        """
        选择数据集的槽函数
        :return:
        """
        sender = self.sender()

        if sender == self.comboBox:
            self.selectFile()
            currentDateset = self.comboBox.currentText()  # 当前的选中的数据集类型
            if currentDateset != self.datasetType:  # 代表我什么都没选，那么当前显示的应该还是之前的数据集
                self.comboBox.blockSignals(True)  # 阻塞comboBox的currentTextChanged信号，不然会出两次弹窗
                self.comboBox.setCurrentText(self.datasetType)
                self.comboBox.blockSignals(False)  # 取消阻塞
        else:
            self.datasetType = self.comboBox.currentText()
        if self.datasetType == 'DEAP':
            self.comboBox_2.clear()
            for i in range(40):
                self.comboBox_2.addItem('trial-' + str(i + 1))
        elif self.datasetType == 'SEED':
            self.comboBox_2.clear()
            for i in range(15):
                self.comboBox_2.addItem('trial-' + str(i + 1))
        elif self.datasetType == 'DREAMER':
            self.comboBox_2.clear()
            for i in range(23):
                self.comboBox_2.addItem('trial-' + str(i + 1))
        else:
            self.comboBox_2.clear()
            pass  # TODO 这里需要改成自己的数据集

    def putFig(self, Fig, graphicsView):
        """
        在graphicsView中放置mne的图像
        :param Fig: 需要放置的图像
        :param graphicsView: 需要放置的区域
        :return:
        """
        Fig.resize(graphicsView.width(), graphicsView.height())
        self.scene = QGraphicsScene()  # 创建一个场景
        self.scene.addWidget(Fig)  # 将图形元素添加到场景中
        graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        graphicsView.setScene(self.scene)  # 将创建添加到图形视图显示窗口

    def selectTrial(self):
        """
        选择trial的槽函数
        :return:
        """
        currentText = self.comboBox_2.currentText()
        if currentText != '':
            currentTrial = int(currentText.split('-')[1])
            self.trial = currentTrial

        if self.datasetType is not None and self.filePath is not None:
            self.showAll()

    def eventFilter(self, watched, event):
        if watched == self.widget:
            handleVideoPlayerEvents(self.player, self.pushButton_3, self.widget, event)
        elif watched == self.widget_2:
            handleVideoPlayerEvents(self.player_2, self.pushButton_18, self.widget_2, event)

        return super().eventFilter(watched, event)

    def getSignal(self):
        """
        多线程实时获取脑电设备的数据
        :return:
        """
        # self.label_23.hide()
        # self.label_28.hide()

        # 　TODO 这里需要换成实际的通道
        eeg_ch = ['Fp1', 'AF3', 'F3', 'F7', 'FC5', 'FC1', 'C3', 'T7', 'CP5', 'CP1', 'P3', 'P7', 'PO3', 'O1', 'Oz', 'Pz',
                  'Fp2', 'AF4', 'Fz', 'F4', 'F8', 'FC6', 'FC2', 'Cz', 'C4', 'T8', 'CP6', 'CP2', 'P4', 'P8', 'PO4', 'O2']
        eeg_fs = 256
        self.info_eeg = mne.create_info(eeg_ch, eeg_fs, ch_types='eeg')

        # 实时展示数据
        self.my_thread = GetRealTimeData()
        self.my_thread.getSecondDataSignal.connect(self.getSecondData)
        self.my_thread.expFinished.connect(self.saveExpData)
        self.my_thread.start()

    def getSecondData(self, data):
        """
        得到每一秒的数据并绘制
        :param data: 每一秒的数据
        :return:
        """
        dataPerSecond = data[0]  # emit的数据从list中拿出来
        dataPerSecond = dataPerSecond.T  # data * ch -> ch * data

        dataPerSecond = mne.io.RawArray(dataPerSecond, self.info_eeg)
        chTimeFig = dataPerSecond.plot(duration=1, n_channels=6, clipping=None, scalings='auto', show=False)
        self.putFig(MyFigure(chTimeFig), self.graphicsView_4)
        plt.close()

        # 测试代码
        # dataPerSecond = data[0]
        # dataPerSecond = mne.io.RawArray(dataPerSecond, self.info_eeg)
        # chTimeFig = dataPerSecond.plot(duration=1, n_channels=6, clipping=None, scalings='auto', show=False)
        # self.putFig(MyFigure(chTimeFig), self.graphicsView_4)
        # plt.close()

    def saveExpData(self, data):
        """
        保存实验的数据，根据每一个trial保存数据
        :return:
        """
        matFileName = self.matFileName
        npyFileName = self.npyFileName

        if matFileName:
            matFileName = matFileName + '-片段{}'.format(self.clip)
        if npyFileName:
            npyFileName = npyFileName + '-片段{}'.format(self.clip)

        data = np.array(data)

        # if data.shape[0] > 100:  # 片段肯定大于100秒，只有这种才保存，其他的都不是片段数据
        #     if self.matFile:
        #         scipy.io.savemat(matFileName, {'data': data})
        #     if self.npyFile:
        #         np.save(npyFileName, data)
        #     self.clip = self.clip + 1

        if self.matFile:
            scipy.io.savemat(matFileName, {'data': data})
        if self.npyFile:
            np.save(npyFileName, data)
        self.clip = self.clip + 1

    def controlCamera(self):
        """
        打开/关闭摄像头
        :return:
        """
        if not self.timerCamera.isActive():
            flag = self.cam.open(0)
            if not flag:
                QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确", buttons=QMessageBox.Ok)
            else:
                self.timerCamera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.label_49.setPixmap(QPixmap('src/icon/camera-close.png'))
        else:
            self.timerCamera.stop()
            self.cam.release()
            self.label_4.setGeometry(100, 100, 121, 121)
            self.label_4.setPixmap(QPixmap('src/icon/camera.png'))
            self.label_49.setPixmap(QPixmap('src/icon/camera-open.png'))

    def refreshFrame(self):
        """
        摄像头逐帧展示图片
        :return:
        """
        _, image = self.cam.read()

        show = cv.resize(image, (340, 255))
        show = cv.cvtColor(show, cv.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)

        self.label_4.setGeometry(5, 50, 340, 255)
        self.label_4.setPixmap(QPixmap.fromImage(showImage))

    def selfAssessment(self):
        """
        自我评估对话框界面
        :return:
        """
        self.selfAssessmentDialog = SelfAssessment()
        self.selfAssessmentDialog.setModal(True)
        self.selfAssessmentDialog.label.setPixmap(QPixmap('src/image/valence.png'))
        self.selfAssessmentDialog.label_2.setPixmap(QPixmap('src/image/arousal.png'))
        self.selfAssessmentDialog.setWindowIcon(QIcon('src/icon/assessment.png'))
        self.selfAssessmentDialog.setWindowTitle('SelfAssessment')
        self.selfAssessmentDialog.setWindowFlags(Qt.Window | Qt.WindowTitleHint)  # 隐藏关闭按钮
        self.selfAssessmentDialog.setFixedSize(self.selfAssessmentDialog.size())
        self.selfAssessmentDialog.show()

        # 使用15秒评估完之后就关闭窗口，保存结果，恢复视频
        QTimer.singleShot(15000, self.selfAssessmentDialog.close)
        QTimer.singleShot(15000, self.playPause)

    def setTimer(self):
        """
        设置定时器，包括自动全屏，自动保存数据，弹出自我量表评估界面
        :return:
        """
        QTimer.singleShot(3000, self.fullScreen)  # 3s后自动全屏

        QTimer.singleShot(18000, self.my_thread.clearSamples)  # 18秒的时候开始记录第一组的数据，清空之前的数据
        QTimer.singleShot(60000, self.my_thread.saveSamples)  # 4分59秒的时候第一个视频采集完毕

        QTimer.singleShot(297000, self.selfAssessment)  # 5分2秒后第一个视频结束，保存数据，开始评估，评估时间为15秒，视频暂停
        QTimer.singleShot(297000, self.playPause)

        QTimer.singleShot(330000, self.my_thread.clearSamples)  # 5分30秒的时候开始记录第二组的数据，清空之前的数据
        QTimer.singleShot(583000, self.my_thread.saveSamples)  # 9分43的时候第二个视频采集完毕

        QTimer.singleShot(581000, self.selfAssessment)  # 5分2秒后第一个视频结束，保存数据，开始评估，评估时间为15秒，视频暂停
        QTimer.singleShot(581000, self.playPause)
