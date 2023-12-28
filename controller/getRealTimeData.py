import time
import pygds as g
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal


# class GetRealTimeData(QThread):
#     """
#     获取实时脑电数据的子线程
#     """
#     getSecondDataSignal = pyqtSignal(list)
#     expFinished = pyqtSignal(list)
#
#     def __init__(self, d):
#         super().__init__()
#         self.samples = []
#         self.d = d
#
#     def emitPerSecond(self):
#         """
#         发送每一秒的数据，用于实时绘制
#         :return:
#         """
#         self.getSecondDataSignal.emit(self.samples)
#
#     def saveSamples(self):
#         """
#         一个片段结束，发送samples，准备采集数据
#         :return:
#         """
#         self.expFinished.emit(self.samples)
#
#     def clearSamples(self):
#         self.samples = []
#
#     def run(self):
#         self.d.GetData(self.d.SamplingRate, lambda s: self.samples.append(s.copy()) or len(self.samples) < 1000)
#         self.d.Close()
#         del self.d


class GetRealTimeData(QThread):
    """
    获取实时脑电数据的子线程
    """
    getSecondDataSignal = pyqtSignal(list)
    expFinished = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.samples = []

    def emitPerSecond(self):
        """
        发送每一秒的数据，用于实时绘制
        :return:
        """
        self.getSecondDataSignal.emit(self.samples)

    def saveSamples(self):
        """
        一个片段结束，发送samples，准备采集数据
        :return:
        """
        self.expFinished.emit(self.samples)

    def clearSamples(self):
        self.samples = []

    def run(self):
        while True:
            data = np.random.rand(256, 8)
            self.samples.append(data)
            time.sleep(1)
