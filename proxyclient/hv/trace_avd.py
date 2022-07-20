from m1n1.trace import Tracer
from m1n1.trace.dart8110 import DART8110Tracer
from m1n1.hw.avd import *
from m1n1.utils import *
import struct


class AVDTracer(Tracer):
    DEFAULT_MODE = TraceMode.SYNC

    def __init__(self, hv, devpath, dart_tracer, verbose=False):
        super().__init__(hv, verbose=verbose, ident=type(self).__name__ + "@" + devpath)
        self.dev = hv.adt[devpath]
        self.dart_tracer = dart_tracer

    def start(self):
        avd_base, _ = self.dev.get_reg(0)
        self.trace_regmap(avd_base + 0x000_0000, 0x4000, AVDThing0_0000Regs, name="Thing_0x000_0000", prefix="Thing_0x000_0000")
        self.trace_regmap(avd_base + 0x000_8000, 0x4000, AVDThing0_8000Regs, name="Thing_0x000_8000", prefix="Thing_0x000_8000")
        self.trace_regmap(avd_base + 0x100_0000, 0x4000, AVDThing100Regs, name="Thing_0x100_0000", prefix="Thing_0x100_0000")
        self.trace_regmap(avd_base + 0x102_0000, 0x4000, AVDThing102Regs, name="Thing_0x102_0000", prefix="Thing_0x102_0000")
        self.trace_regmap(avd_base + 0x107_0000, 0x4000, AVDPIODMARegs, name="PIODMA", prefix="PIODMA")
        # self.trace(avd_base + 0x108_0000, 0x10000, mode=self.DEFAULT_MODE, prefix="CM3CODE")
        # self.trace(avd_base + 0x109_0000, 0x10000, mode=self.DEFAULT_MODE, prefix="CM3DATA")
        self.trace_regmap(avd_base + 0x10a_0000, 0x4000, AVDCM3CtrlRegs, name="CM3Ctrl", prefix="CM3Ctrl")
        self.trace_regmap(avd_base + 0x110_0000, 0x8000, AVDConfigRegs, name="CTRL", prefix="CTRL")
        self.trace_regmap(avd_base + 0x110_c000, 0x4000, AVDDMAThingyRegs, name="DMA_THINGY", prefix="DMA_THINGY")
        self.trace_regmap(avd_base + 0x140_0000, 0x4000, AVDWrapCtrlRegs, name="WRAP_CTRL", prefix="WRAP_CTRL")
        self.dart_tracer.start()

AVDTracer = AVDTracer._reloadcls()

p.pmgr_adt_clocks_enable('/arm-io/dart-avd0')
p.pmgr_adt_clocks_enable('/arm-io/avd0')

dart_tracer = DART8110Tracer(hv, "/arm-io/dart-avd0", verbose=3)
print(dart_tracer)
tracer = AVDTracer(hv, '/arm-io/avd0', dart_tracer, verbose=3)
tracer.start()
print(tracer)