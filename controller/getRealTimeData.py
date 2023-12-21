import pygds as g
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal


class GetRealTimeData(QThread):
    """
    获取实时脑电数据的子线程
    """
    getSecondDataSignal = pyqtSignal(list)
    expFinished = pyqtSignal(list)

    def __init__(self, ):
        super().__init__()

        self.d = g.GDS()
        self.reference = 32

        self.filename = 'demo_save.npy'

        # 这里进行读取数据前的设置过程
        f_s_2 = sorted(self.d.GetSupportedSamplingRates()[0].items())[0]  # 256Hz
        self.d.SamplingRate, self.d.NumberOfScans = f_s_2

        # 配置默认参数
        self.configure()

        # 通过设置对应的滤波器获取选定采样率所有适合的带通滤波器和陷波滤波器index来实现滤波
        N = [x for x in self.d.GetNotchFilters()[0] if x['SamplingRate'] == self.d.SamplingRate]
        BP = [x for x in self.d.GetBandpassFilters()[0] if x['SamplingRate'] == self.d.SamplingRate]

        # 在自己想要的电极通道数上设置滤波器参数和参考电极参数
        for i, ch in enumerate(self.d.Channels):
            ch.Acquire = True  # 设置为可采数据
            ch.ReferenceChannel = self.reference  # 设置参考电极
            if N:
                ch.NotchFilterIndex = N[0]['NotchFilterIndex']  # 50Hz陷波滤波器
            if BP:
                ch.BandpassFilterIndex = BP[14]['BandpassFilterIndex']  # [0.5-60]带通滤波
            # if i == reference - 1:
            #     break

        # 将设置好的参数应用到设备上
        self.d.SetConfiguration()

        # 实现获取电极的阻抗值
        self.inform_impedance()

    def configure(self):
        """
        实现对选中的电极通道进行设置初始化（采样率、带通滤波器参数、陷波滤波器参数和参考电极）
        :return:
        """
        self.d.InternalSignalGenerator.Enabled = False      # 不使用内置信号发生器
        self.d.InternalSignalGenerator.Frequency = 10
        self.d.NumberOfScans_calc()
        self.d.Counter = 0
        self.d.Trigger = 0
        for ch in self.d.Channels:
            ch.Acquire = 0    # 初始化为不获得数据
            ch.BandpassFilterIndex = -1
            ch.NotchFilterIndex = -1
            ch.BipolarChannel = 0  # 0 => to GND
        self.d.HoldEnabled = 0

    def inform_impedance(self):
        """
        实时获取选择通道的阻抗值
        :return:
        """
        imps = self.d.GetImpedance([1] * len(self.d.Channels))
        for i, ch in enumerate(self.d.Channels):
            if i < self.reference:
                print("channel_{}'s impedance is {}".format(i + 1, imps[0][i]))

    def run(self):
        samples = []
        while len(samples) < 240:
            container = list()
            data = self.d.GetData(self.d.SamplingRate)  # 一个data获取的就是1s的数据
            samples.append(data)
            container.append(data)
            self.getSecondDataSignal.emit(container)

        self.expFinished.emit(samples)
        del data

        self.d.Close()
        del self.d

        # 测试数据
        # samples = []
        # while len(samples) < 30:
        #     container = []
        #     self.msleep(1000)
        #     data = np.random.rand(32, 256)
        #     samples.append(data)
        #     container.append(data)
        #     self.getSecondDataSignal.emit(container)
        #
        # self.expFinished.emit(samples)










