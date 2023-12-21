import mne
import pickle
import numpy as np
import pandas as pd
from scipy.io import loadmat
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtCore import Qt, QEvent, pyqtSignal
from mne.channels import make_standard_montage
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg


def loadRawData(filepath, datasetType, trial):
    """
    根据文件的类型和数据集的类型，加载数据
    :param trial:   哪一个刺激视频
    :param filepath: 文件路径
    :param datasetType:  数据集类型
    :return:
    """
    rawEEG, ica = None, None

    if datasetType == 'DEAP':
        rawData = open(filepath, 'rb')
        rawData = pickle.load(rawData, encoding='latin1')
        rawData = rawData['data']
        rawData = rawData[:, :32, :]  # 只取前32个脑电通道
        eegCh = np.load('./file/DEAP_CH.npy').tolist()
        eegFs = 128
        infoEEG = mne.create_info(ch_names=eegCh, sfreq=eegFs, ch_types='eeg')
        rawData = rawData[trial - 1, :, :]
        rawEEG = mne.io.RawArray(rawData, infoEEG)
        montage = make_standard_montage('biosemi32')
        rawEEG.set_montage(montage)
        ica = mne.preprocessing.ICA(n_components=4, random_state=0)
        ica.fit(rawEEG.copy().filter(4, 45))
    elif datasetType == 'SEED':
        rawData = loadmat(filepath)
        rawData = rawData['djc_eeg' + str(trial)]
        eegCh = np.load('./file/SEED_CH.npy').tolist()
        eegFs = 200
        infoEEG = mne.create_info(ch_names=eegCh, sfreq=eegFs, ch_types='eeg')
        rawEEG = mne.io.RawArray(rawData, infoEEG)
        montage = seedMontage()
        rawEEG.set_montage(montage)
        ica = mne.preprocessing.ICA(n_components=4, random_state=0)
        ica.fit(rawEEG.copy())
    elif datasetType == 'DREAMER':
        data_dict = loadmat(filepath)['DREAMER'][0][0][0][0]
        # subject_index受试者, trial_index刺激视频
        subject_index = 0
        rawData = data_dict[subject_index][0][0][2][0][0][1][trial - 1][0]
        rawData = rawData.T
        eegCh = np.load('./file/DREAMER_CH.npy').tolist()
        eegFs = 128
        infoEEG = mne.create_info(ch_names=eegCh, sfreq=eegFs, ch_types='eeg')
        rawEEG = mne.io.RawArray(rawData, infoEEG)
        montage = make_standard_montage('biosemi32')
        rawEEG.set_montage(montage)
        ica = mne.preprocessing.ICA(n_components=4, random_state=0)
        ica.fit(rawEEG.copy())
    elif datasetType == 'SELF':
        pass

    return rawEEG, ica


class MyFigure(FigureCanvasQTAgg):
    """
    重写一个MNE电极位置图像绘制类
    """

    def __init__(self, posFig):
        self.fig = posFig
        super(MyFigure, self).__init__(self.fig)


def seedMontage():
    """
    SEED数据集的电极的位置是要自己调整的，这里进行调整
    :return:
    """
    seedPos = pd.read_excel('./file/seedPos.xlsx', index_col=0)
    channels1020 = np.array(seedPos.index)
    value1020 = np.array(seedPos)

    list_dic = dict(zip(channels1020, value1020))
    montageSeedPos = mne.channels.make_dig_montage(ch_pos=list_dic,
                                                   nasion=[5.27205792e-18, 8.60992398e-02, -4.01487349e-02],
                                                   lpa=[-0.08609924, -0., -0.04014873],
                                                   rpa=[0.08609924, 0., -0.04014873])

    return montageSeedPos


def handleVideoPlayerEvents(player, button, widget, event):
    """
    视频播放事件处理
    :param player: 需要选择的播放器
    :param button: 需要改变的按钮
    :param widget: 需要改变的窗体
    :param event:  监听到的事件
    :return:
    """

    # 鼠标左键按下时，暂停或继续播放
    if event.type() == QEvent.MouseButtonPress:
        if event.button() == Qt.LeftButton:
            if player.state() == QMediaPlayer.PlayingState:
                player.pause()
                button.setIcon(QIcon('src/icon/play.png'))
            else:
                player.play()
                button.setIcon(QIcon('src/icon/pause.png'))

    # 全屏状态时，按ESC键退出全屏
    if event.type() == QEvent.KeyPress:
        if event.key() == Qt.Key_Escape:
            if widget.isFullScreen():
                widget.setFullScreen(False)
                widget.setGeometry(20, 13, 1011, 391)

    # 双击事件，打开或关闭全屏
    if event.type() == QEvent.MouseButtonDblClick:
        if event.button() == Qt.LeftButton:
            if not widget.isFullScreen():
                widget.setFullScreen(True)
            else:
                widget.setFullScreen(False)
                widget.setGeometry(20, 13, 1011, 391)


class ClickableLabel(QLabel):
    """
    自定义一个可以有点击事件的Label类
    """
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)
