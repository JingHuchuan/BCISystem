import numpy as np
import matplotlib.pyplot as plt
#
import pygds as g
import pygds

from pygds import Scope
import time

# f = 10
# scope = Scope(1 / f, modal=True)
# t = np.linspace(0, 100, 100) / f
# scope(np.array([np.sin(t + i / 2) for i in range(10)]))
# time.sleep(1)
# plt.show()
# scope(np.array([np.sin(t + i / 3) for i in range(10)]))
# time.sleep(1)
# plt.show()
# scope(np.array([np.sin(t + i / 4) for i in range(10)]))
# time.sleep(1)
# plt.show()
# scope(np.array([np.sin(t + i / 5) for i in range(10)]))
#
# plt.show()
# data = np.ones((1000, 32))
# scope.__call__()
# scope.__call__(data)
# del scope

# cd = pygds.ConnectedDevices()
# hiamp = cd.find(pygds.DEVICE_TYPE_GHIAMP)
# hiamp is None or len(hiamp.split('.')) > 0
# print(hiamp)

# d = g.GDS()

# scanCount = 500
# channelsPerDevice, bufferSizeInSamples = d.GetDataInfo(scanCount)
# print(sum(channelsPerDevice))
# print(sum(channelsPerDevice) * scanCount == bufferSizeInSamples)
# d.Close()
# del d

# n = d.N_ch_calc()
# print(d.N_ch)
# print(d.N_electrodes)
# print(d.N_ch == n)

# d = g.GDS()
# minf_s = sorted(d.GetSupportedSamplingRates()[0].items())[0]
# d.SamplingRate, d.NumberOfScans = minf_s
# for ch in d.Channels:
#     ch.Acquire = True
# d.SetConfiguration()
# scope = g.Scope(1 / d.SamplingRate)
# d.GetData(d.SamplingRate, scope)

# import pygds
#
# d = pygds.GDS()
# samples = []
# more = lambda s: samples.append(s.copy()) or len(samples) < 2
# data = d.GetData(d.SamplingRate, more)
# print(len(samples))

# import pygds
#
# d = pygds.GDS()
# print(d.SamplingRate)
#
# # GetSupportedSamplingRates得到的是支持的采样率和扫描次数
# d.GetSupportedSamplingRates()[0]
#
# # GetBandpassFilters内置了很多滤波器，之后就选择和采样率的频率一致的即可
# d.GetBandpassFilters()[0]
#
# print(len(d.Channels))
#
# f_s_2 = sorted(d.GetSupportedSamplingRates()[0].items())[1]  # 512 or 500
# d.SamplingRate, d.NumberOfScans = f_s_2
# # 这句话的含义是获取和采样率一致的带通滤波器
# BP = [x for x in d.GetBandpassFilters()[0] if x['SamplingRate'] == d.SamplingRate]
# # 给每一个通道设置带通滤波器，默认d.Channels是256个通道
# for ch in d.Channels:
#     ch.Acquire = True
#     if BP:
#         ch.BandpassFilterIndex = BP[0]['BandpassFilterIndex']
# d.SetConfiguration()
# print(d.SamplingRate)
# print(d.GetData(d.SamplingRate).shape[0] == d.SamplingRate)
# d.Close()
# del d

from pygds import *
import pygds
import pygds as g


def configure_demo(d, testsignal=False, acquire=1):
    '''
    Makes a configuration for the demos.

    The device configuration fields are members of the device object d.
    If d.ConfigCount>1, i.e. more devices are connected, use d.Configs[i] instead.

    Config names are unified: See ``name_maps``.

    This does not configure a filter.
    Note that g.HIamp version < 1.0.9 will have wrong first value without filters.

    '''
    if d.DeviceType == DEVICE_TYPE_GNAUTILUS:
        sensitivities = d.GetSupportedSensitivities()[0]
        d.SamplingRate = 250
        if testsignal:
            d.InputSignal = GNAUTILUS_INPUT_SIGNAL_TEST_SIGNAL
        else:
            d.InputSignal = GNAUTILUS_INPUT_SIGNAL_ELECTRODE
    else:
        d.SamplingRate = 256
        d.InternalSignalGenerator.Enabled = testsignal
        d.InternalSignalGenerator.Frequency = 10
    d.NumberOfScans_calc()
    d.Counter = 0
    d.Trigger = 0
    for i, ch in enumerate(d.Channels):
        ch.Acquire = acquire
        ch.BandpassFilterIndex = -1
        ch.NotchFilterIndex = -1
        ch.BipolarChannel = 0  # 0 => to GND
        if d.DeviceType == DEVICE_TYPE_GNAUTILUS:
            ch.BipolarChannel = -1  # -1 => to GND
            ch.Sensitivity = sensitivities[5]
            ch.UsedForNoiseReduction = 0
            ch.UsedForCAR = 0
    # not unified
    if d.DeviceType == DEVICE_TYPE_GUSBAMP:
        d.ShortCutEnabled = 0
        d.CommonGround = [1] * 4
        d.CommonReference = [1] * 4
        d.InternalSignalGenerator.WaveShape = GUSBAMP_WAVESHAPE_SINE
        d.InternalSignalGenerator.Amplitude = 200
        d.InternalSignalGenerator.Offset = 0
    elif d.DeviceType == DEVICE_TYPE_GHIAMP:
        d.HoldEnabled = 0
    elif d.DeviceType == DEVICE_TYPE_GNAUTILUS:
        d.NoiseReduction = 0
        d.CAR = 0
        d.ValidationIndicator = 1
        d.AccelerationData = 1
        d.LinkQualityInformation = 1
        d.BatteryLevel = 1


def demo_counter():
    '''
    This demo

    - configures to internal test signal
    - records 1 second
    - displays the counter
    - displays channel 2

    Have a device

    - connected to the PC and
    - switched on

    '''
    d = GDS()
    # configure
    configure_demo(d, testsignal=d.DeviceType != DEVICE_TYPE_GUSBAMP)
    d.Counter = 1
    # set configuration
    d.SetConfiguration()
    # get data
    data = d.GetData(d.SamplingRate)
    # plot counter
    scope = Scope(1 / d.SamplingRate, modal=True, ylabel='n',
                  xlabel='t/s', title='Counter')
    icounter = d.IndexAfter('Counter') - 1
    scope(data[:, icounter:icounter + 1])
    plt.show()
    # plot second channel
    scope = Scope(1 / d.SamplingRate, modal=True, ylabel=u'U/μV',
                  xlabel='t/s', title='Channel 2')
    scope(data[:, 1:2])
    # or
    # plt.plot(data[1:,1])
    # plt.title('Channel 2')
    plt.show()
    # close
    d.Close()
    del d
    return data


def demo_save():
    '''
    This demo

    - records the internal test signal
    - saves the acquired data after recording

    Have a device

    - connected to the PC and
    - switched on

    '''
    filename = 'demo_save.npy'
    assert not os.path.exists(
        filename), "the file %s must not exist yet" % filename
    # device object
    d = GDS()
    # configure
    configure_demo(d, testsignal=True)
    # set configuration
    d.SetConfiguration()
    # get data
    data = d.GetData(d.SamplingRate)
    # save
    np.save(filename, data)
    del data
    # load
    dfromfile = np.load(filename)
    os.remove(filename)
    # show loaded
    scope = Scope(1 / d.SamplingRate, modal=True,
                  xlabel="t/s", title='Channel 1')
    scope(dfromfile[:, 0:1])
    # close
    d.Close()
    del d


def demo_di():
    '''
    This demo

    - records the DI channel
    - displays it with the live scope

    Have a device

    - connected to the PC and
    - switched on

    '''
    d = GDS()
    # configure
    configure_demo(d, testsignal=False, acquire=1)
    d.Trigger = 1
    d.Channels[0].Acquire = 1  # at least one channel needs to be there
    d.SetConfiguration()
    # initialize scope object
    scope = Scope(1 / d.SamplingRate, subplots={0: 0, 1: 1}, xlabel=(
        '', 't/s'), ylabel=(u'V/μV', 'DI'), title=('Ch1', 'DI'), modal=False)
    # get data to scope
    data = d.GetData(d.SamplingRate, more=scope)
    di1 = d.IndexAfter('DI') - 1
    di2 = d.IndexAfter('Trigger') - 1
    assert di1 == di2
    print('DI channel is ', di1)
    # close
    d.Close()
    del d


def demo():
    d = g.GDS()

    minf_s = sorted(d.GetSupportedSamplingRates()[0].items())[0]
    d.SamplingRate, d.NumberOfScans = minf_s
    for ch in d.Channels:
        ch.Acquire = True
    d.SetConfiguration()
    scope = g.Scope(1 / d.SamplingRate)
    d.GetData(d.SamplingRate, scope)


def demo_scope():
    '''
    This demo

    - records a test signal
    - displays it in the live scope

    Have a device

    - connected to the PC and
    - switched on

    '''
    d = GDS()
    # configure
    configure_demo(d, testsignal=False, acquire=1)    # d.Channels[0].Acquire = 1  # at least one channel needs to be there
    # d.Channels[1].Acquire = 1  # at least one channel needs to be there
    # d.Channels[2].Acquire = 1  # at least one channel needs to be there
    d.SetConfiguration()
    # initialize scope
    scope = Scope(1 / d.SamplingRate, xlabel='t/s', ylabel=u'V/μV',
                  title="Internal Signal Channels: %s")
    # get data to scope
    data = d.GetData(d.SamplingRate, scope)
    np.save('demo.npy', data)
    # close
    d.Close()
    del d


demo_scope()
# demo()
# demo_di()
# demo_save()
# d = g.GDS()

# configure_demo(d)
# data = demo_counter()
# print()
