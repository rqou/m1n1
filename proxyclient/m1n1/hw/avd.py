# SPDX-License-Identifier: MIT
from ..utils import *


class AVDThing0_0000Regs(RegMap):
    pass


class AVDThing0_8000Regs(RegMap):
    pass


class AVDThing100Regs(RegMap):
    DEVICE_POWER_ON                     = 0x0, Register32


class AVDThing102Regs(RegMap):
    pass


class AVDPIODMARegs(RegMap):
    APIODMA_CFG                         = 0x00, Register32

    APIODMA_DMACFGMEMSRC                = 0x10, Register32
    APIODMA_DMACFGMEMDAT                = 0x14, Register32
    APIODMA_DMACFGMEMDST                = 0x18, Register32
    APIODMA_DMACFGPIORD                 = 0x1c, Register32
    APIODMA_DMACFGPIOWR                 = 0x20, Register32
    INIT_AVD_WRAP_THING                 = 0x24, Register32


class AVDCM3CtrlRegs(RegMap):
    INT_ENABLE_THING0                   = 0x10, Register32

    INT_ENABLE_THING1                   = 0x48, Register32

    MAILBOX0_STATUS                     = 0x50, Register32
    MAILBOX0_DATA                       = 0x54, Register32

    MAILBOX1_STATUS                     = 0x68, Register32
    MAILBOX1_DATA                       = 0x6c, Register32


class AVDConfigRegs(RegMap):
    HW_VERSION                          = 0x0000, Register32

    MCTLCONFIG_MODE                     = 0x0008, Register32


    HVPCONFIG_MODE0                     = 0x1000, Register32

    HV0CFG_THING0                       = 0x1008, Register32
    HV0CFG_THING1                       = 0x100c, Register32
    HV0CFG_THING2                       = 0x1010, Register32
    HV0CFG_THING3                       = 0x1014, Register32


    HVPCONFIG_MODE1                     = 0x1100, Register32

    HV1CFG_THING0                       = 0x1108, Register32
    HV1CFG_THING1                       = 0x110c, Register32
    HV1CFG_THING2                       = 0x1110, Register32
    HV1CFG_THING3                       = 0x1114, Register32


    HVPCONFIG_MODE2                     = 0x1200, Register32


    HVPCONFIG_MODE3                     = 0x1300, Register32


    AVPCONFIG_MODE0                     = 0x1400, Register32

    AVPCFG_THING0                       = 0x1408, Register32
    AVPCFG_THING1                       = 0x140c, Register32
    AVPCFG_THING2                       = 0x1410, Register32
    AVPCFG_THING3                       = 0x1414, Register32


    AVPCONFIG_MODE1                     = 0x1500, Register32


    AVPCONFIG_MODE2                     = 0x1600, Register32


    AVPCONFIG_MODE3                     = 0x1700, Register32


    LVPCONFIG_MODE                      = 0x1800, Register32


    QTCONFIG_MODE                       = 0x4000, Register32


    IPMCCONFIG_MODE                     = 0x4100, Register32


    LFCONFIG_MODE                       = 0x4200, Register32


    MVCONFIG_MODE                       = 0x4300, Register32


    TPCONFIG_MODE                       = 0x4400, Register32


    PCCONFIG_MODE                       = 0x4500, Register32


    SWRCONFIG_MODE                      = 0x4600, Register32


class AVDDMAThingyRegs(RegMap):
    DMAVPTOP_CLKGATINGEN                = 0x0000, Register32

    DMAVPTO_THING0                      = 0x0008, Register32
    DMAVPTO_THING1                      = 0x000c, Register32
    DMAVPTO_THING2                      = 0x0010, Register32
    DMAVPTO_THING3                      = 0x0014, Register32
    DMAVPTO_THING4                      = 0x0018, Register32
    DMAVPTO_THING5                      = 0x001c, Register32

    RDDMAHVPBITS_DMACONFIG0             = 0x0080, Register32
    RDDMAHVPBITS_DMABFRCONFIG0          = 0x0084, Register32

    RDDMAHVPBITS_DMACONFIG1             = 0x00c0, Register32
    RDDMAHVPBITS_DMABFRCONFIG1          = 0x00c4, Register32

    RDDMAHVPBITS_DMACONFIG2             = 0x0100, Register32
    RDDMAHVPBITS_DMABFRCONFIG2          = 0x0104, Register32

    RDDMAHVPBITS_DMACONFIG3             = 0x0140, Register32
    RDDMAHVPBITS_DMABFRCONFIG3          = 0x0144, Register32

    WRDMAHVPINSN_DMACONFIG0             = 0x0180, Register32
    WRDMAHVPINSN_DMABFRCONFIG0          = 0x0184, Register32

    WRDMAHVPINSN_DMACONFIG1             = 0x01c0, Register32
    WRDMAHVPINSN_DMABFRCONFIG1          = 0x01c4, Register32

    WRDMAHVPINSN_DMACONFIG2             = 0x0200, Register32
    WRDMAHVPINSN_DMABFRCONFIG2          = 0x0204, Register32

    WRDMAHVPINSN_DMACONFIG3             = 0x0240, Register32
    WRDMAHVPINSN_DMABFRCONFIG3          = 0x0244, Register32

    RDDMAAVPBITS_DMACONFIG0             = 0x0280, Register32
    RDDMAAVPBITS_DMABFRCONFIG0          = 0x0284, Register32

    RDDMAAVPBITS_DMACONFIG1             = 0x02c0, Register32
    RDDMAAVPBITS_DMABFRCONFIG1          = 0x02c4, Register32

    RDDMAAVPBITS_DMACONFIG2             = 0x0300, Register32
    RDDMAAVPBITS_DMABFRCONFIG2          = 0x0304, Register32

    RDDMAAVPBITS_DMACONFIG3             = 0x0340, Register32
    RDDMAAVPBITS_DMABFRCONFIG3          = 0x0344, Register32

    WRDMAAVPABOVEINFO_DMACONFIG0        = 0x0380, Register32
    WRDMAAVPABOVEINFO_DMABFRCONFIG0     = 0x0384, Register32

    WRDMAAVPABOVEINFO_DMACONFIG1        = 0x03c0, Register32
    WRDMAAVPABOVEINFO_DMABFRCONFIG1     = 0x03c4, Register32

    WRDMAAVPABOVEINFO_DMACONFIG2        = 0x0400, Register32
    WRDMAAVPABOVEINFO_DMABFRCONFIG2     = 0x0404, Register32

    WRDMAAVPABOVEINFO_DMACONFIG3        = 0x0440, Register32
    WRDMAAVPABOVEINFO_DMABFRCONFIG3     = 0x0444, Register32

    WRDMAAVPABOVEINFO_DMACONFIG4        = 0x0480, Register32
    WRDMAAVPABOVEINFO_DMABFRCONFIG4     = 0x0484, Register32

    WRDMAAVPABOVEINFO_DMACONFIG5        = 0x04c0, Register32
    WRDMAAVPABOVEINFO_DMABFRCONFIG5     = 0x04c4, Register32

    WRDMAAVPABOVEINFO_DMACONFIG6        = 0x0500, Register32
    WRDMAAVPABOVEINFO_DMABFRCONFIG6     = 0x0504, Register32

    WRDMAAVPABOVEINFO_DMACONFIG7        = 0x0540, Register32
    WRDMAAVPABOVEINFO_DMABFRCONFIG7     = 0x0544, Register32

    WRDMAAVPINSN_DMACONFIG0             = 0x0580, Register32
    WRDMAAVPINSN_DMABFRCONFIG0          = 0x0584, Register32

    WRDMAAVPINSN_DMACONFIG1             = 0x05c0, Register32
    WRDMAAVPINSN_DMABFRCONFIG1          = 0x05c4, Register32

    WRDMAAVPINSN_DMACONFIG2             = 0x0600, Register32
    WRDMAAVPINSN_DMABFRCONFIG2          = 0x0604, Register32

    WRDMAAVPINSN_DMACONFIG3             = 0x0640, Register32
    WRDMAAVPINSN_DMABFRCONFIG3          = 0x0644, Register32

    RDDMALVPBITS_DMACONFIG              = 0x0680, Register32
    RDDMALVPBITS_DMABFRCONFIG           = 0x0684, Register32

    WRDMALVPABOVEINFO_DMACONFIG         = 0x06c0, Register32
    WRDMALVPABOVEINFO_DMABFRCONFIG      = 0x06c4, Register32

    RDDMALVPABOVEINFO_DMACONFIG         = 0x0700, Register32
    RDDMALVPABOVEINFO_DMABFRCONFIG      = 0x0704, Register32

    WRDMALVPSEG_DMACONFIG               = 0x0740, Register32
    WRDMALVPSEG_DMABFRCONFIG            = 0x0744, Register32

    RDDMALVPSEG_DMACONFIG               = 0x0780, Register32
    RDDMALVPSEG_DMABFRCONFIG            = 0x0784, Register32

    WRDMALVPCOLO_DMACONFIG              = 0x07c0, Register32
    WRDMALVPCOLO_DMABFRCONFIG           = 0x07c4, Register32

    RDDMALVPCOLO_DMACONFIG              = 0x0800, Register32
    RDDMALVPCOLO_DMABFRCONFIG           = 0x0804, Register32

    WRDMALVPSTATE_DMACONFIG             = 0x0840, Register32
    WRDMALVPSTATE_DMABFRCONFIG          = 0x0844, Register32

    RDDMALVPSTATE_DMACONFIG             = 0x0880, Register32
    RDDMALVPSTATE_DMABFRCONFIG          = 0x0884, Register32

    WRDMALVPINSN_DMACONFIG              = 0x08c0, Register32
    WRDMALVPINSN_DMABFRCONFIG           = 0x08c4, Register32

    RDDMAPIPEINSN_DMACONFIG0            = 0x0900, Register32
    RDDMAPIPEINSN_DMABFRCONFIG0         = 0x0904, Register32

    RDDMAPIPEINSN_DMACONFIG1            = 0x0940, Register32
    RDDMAPIPEINSN_DMABFRCONFIG1         = 0x0944, Register32

    RDDMAPIPEINSN_DMACONFIG2            = 0x0980, Register32
    RDDMAPIPEINSN_DMABFRCONFIG2         = 0x0984, Register32

    RDDMAPIPEINSN_DMACONFIG3            = 0x09c0, Register32
    RDDMAPIPEINSN_DMABFRCONFIG3         = 0x09c4, Register32


    DMAINTRATOP_CLKGATINGEN             = 0x2000, Register32

    WRDMAIPABOVEPIX_DMACONFIG           = 0x2080, Register32
    WRDMAIPABOVEPIX_DMABFRCONFIG        = 0x2084, Register32

    RDDMAIPABOVEPIX_DMACONFIG           = 0x20c0, Register32
    RDDMAIPABOVEPIX_DMABFRCONFIG        = 0x20c4, Register32

    WRDMALFABOVEPIX_DMACONFIG           = 0x2100, Register32
    WRDMALFABOVEPIX_DMABFRCONFIG        = 0x2104, Register32

    RDDMALFABOVEPIX_DMACONFIG           = 0x2140, Register32
    RDDMALFABOVEPIX_DMABFRCONFIG        = 0x2144, Register32

    WRDMALFABOVEINFO_DMACONFIG          = 0x2180, Register32
    WRDMALFABOVEINFO_DMABFRCONFIG       = 0x2184, Register32

    RDDMALFABOVEINFO_DMACONFIG          = 0x21c0, Register32
    RDDMALFABOVEINFO_DMABFRCONFIG       = 0x21c4, Register32

    WRDMALFLEFTPIX_DMACONFIG            = 0x2200, Register32
    WRDMALFLEFTPIX_DMABFRCONFIG         = 0x2204, Register32

    RDDMALFLEFTPIX_DMACONFIG            = 0x2240, Register32
    RDDMALFLEFTPIX_DMABFRCONFIG         = 0x2244, Register32

    WRDMALFLEFTINFO_DMACONFIG           = 0x2280, Register32
    WRDMALFLEFTINFO_DMABFRCONFIG        = 0x2284, Register32

    RDDMALFLEFTINFO_DMACONFIG           = 0x22c0, Register32
    RDDMALFLEFTINFO_DMABFRCONFIG        = 0x22c4, Register32

    WRDMASWPIX_DMACONFIG                = 0x2300, Register32
    WRDMASWPIX_DMABFRCONFIG             = 0x2304, Register32

    WRDMASWLEFT_DMACONFIG               = 0x2340, Register32
    WRDMASWLEFT_DMABFRCONFIG            = 0x2344, Register32

    RDDMASWLEFT_DMACONFIG               = 0x2380, Register32
    RDDMASWLEFT_DMABFRCONFIG            = 0x2384, Register32

    WRDMAAZABOVEPIX_DMACONFIG           = 0x23c0, Register32
    WRDMAAZABOVEPIX_DMABFRCONFIG        = 0x23c4, Register32

    RDDMAAZABOVEPIX_DMACONFIG           = 0x2400, Register32
    RDDMAAZABOVEPIX_DMABFRCONFIG        = 0x2404, Register32

    WRDMAAZLEFTPIX_DMACONFIG            = 0x2440, Register32
    WRDMAAZLEFTPIX_DMABFRCONFIG         = 0x2444, Register32

    RDDMAAZLEFTPIX_DMACONFIG            = 0x2480, Register32
    RDDMAAZLEFTPIX_DMABFRCONFIG         = 0x2484, Register32

    WRDMAZIP_DMACONFIG0                 = 0x24c0, Register32

    WRDMAZIP_CMPBFRCONFIG0              = 0x24c8, Register32

    WRDMAZIP_HDRBFRCONFIG0              = 0x24cc, Register32

    WRDMAZIP_DMACONFIG1                 = 0x2500, Register32

    WRDMAZIP_CMPBFRCONFIG1              = 0x2508, Register32

    WRDMAZIP_HDRBFRCONFIG1              = 0x250c, Register32

    DMAINTERTOP_CLKGATINGEN             = 0x2800, Register32

    WRDMAMVABOVEINFO_DMACONFIG          = 0x2880, Register32
    WRDMAMVABOVEINFO_DMABFRCONFIG       = 0x2884, Register32

    RDDMAMVABOVEINFO_DMACONFIG          = 0x28c0, Register32
    RDDMAMVABOVEINFO_DMABFRCONFIG       = 0x28c4, Register32

    WRDMAMVCOLO_DMACONFIG               = 0x2900, Register32
    WRDMAMVCOLO_DMABFRCONFIG            = 0x2904, Register32

    RDDMAMVCOLO_DMACONFIG               = 0x2940, Register32
    RDDMAMVCOLO_DMABFRCONFIG            = 0x2944, Register32

    RDDMAZIP_DMACONFIG                  = 0x2980, Register32


class AVDWrapCtrlRegs(RegMap):
    DMA_IRQ_THING                       = 0x04, Register32

    IDLE_THING                          = 0x14, Register32
    AVDCTRL_CLOCKGATEENABLE             = 0x18, Register32
