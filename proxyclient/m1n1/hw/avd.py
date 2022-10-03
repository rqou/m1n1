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


class R_PIODMA_CFG(Register32):
    PAUSE       = 0
    # dunno, but this is set on reset
    _BIT1       = 1


class R_PIODMA_IRQ(Register32):
    DONE                    = 0
    COMMAND_PARSE_ERROR     = 1
    SEQUENCE_FIFO_OVERFLOW  = 2
    AXI_BUS_ERROR           = 3
    # haven't been able to trigger this one yet
    ADDRESS_BOUNDS_ERROR    = 4
    _BIT5                   = 5
    # this gets set when finishing a normal command
    _BIT6                   = 6
    _BIT7                   = 7
    # this gets set if i use 0x19 instead of 0x11
    _BIT8                   = 8
    _BIT9                   = 9


class R_PIODMA_STATUS(Register32):
    FREE_COMMAND_COUNT      = 5, 0
    COMMANDS_COMPLETED      = 21, 16
    # indicates something, happens when i link a 0 size at the end
    _BIT22                  = 22
    BUSY                    = 31


class R_PIODMA_COMMAND(Register32):
    # bit0 = go?
    # 7 = cancel
    # 0x11 = normal
    # 0x13 = pio read error (so, the other way around?)
    # 0x19 = different
    CMD                     = 7, 0
    COUNT                   = 30, 8


class R_PIODMA_ERROR_STATUS(Register32):
    # this doesn't seem to make sense or be understood
    PARSE_COUNTS            = 15, 0
    ERR_MEM_RD              = 28
    ERR_MEM_WR              = 29
    ERR_PIO_RD              = 30
    ERR_PIO_WR              = 31


class PIODMA_PACKET_WRITE(Register32):
    INCREMENT               = 0
    MUST_BE_ZERO            = 1
    ADDR                    = 17, 2
    COUNT_MINUS_ONE         = 29, 18
    # not sure how to use regs >= 4???
    BASE_ADDR_REG           = 31, 30


class PIODMA_PACKET_LINK(Register32):
    MUST_BE_ONE             = 1, 0
    _UNK0                   = 3, 2
    COUNT                   = 25, 4
    _UNK1                   = 27, 26
    IOVA_HI                 = 31, 28


class AVDPIODMARegs(RegMap):
    CFG                                 = 0x00, R_PIODMA_CFG
    IRQ_STATUS                          = 0x04, R_PIODMA_IRQ
    IRQ_ENABLE                          = 0x08, R_PIODMA_IRQ
    STATUS                              = 0x0c, R_PIODMA_STATUS
    # Tunables of some kind
    DMACFGMEMSRC                        = 0x10, Register32
    DMACFGMEMDAT                        = 0x14, Register32
    DMACFGMEMDST                        = 0x18, Register32
    DMACFGPIORD                         = 0x1c, Register32
    DMACFGPIOWR                         = 0x20, Register32
    # at least four of them work, not sure about the other four
    # addr >> 4
    BASE_ADDR_LO                        = irange(0x24, 8, 4), Register32

    # 0x44
    # 0xffffffff
    # 0x48
    # 0x3ff

    SRC_ADDR_LO                         = 0x4c, Register32
    SRC_ADDR_HI                         = 0x50, Register32
    # 0xffffff7e
    COMMAND                             = 0x54, R_PIODMA_COMMAND

    # regs here not writable, all 0 on start

    # XXX are these only valid on faults?
    MEM_RD_ADDR_LO                      = 0x90, Register32
    MEM_RD_ADDR_HI                      = 0x94, Register32
    MEM_WR_ADDR_LO                      = 0x98, Register32
    MEM_WR_ADDR_HI                      = 0x9c, Register32
    PIO_RD_ADDR_LO                      = 0x90, Register32
    PIO_RD_ADDR_HI                      = 0x94, Register32
    PIO_WR_ADDR_LO                      = 0x98, Register32
    PIO_WR_ADDR_HI                      = 0x9c, Register32
    # [0xb0] = mem counts
    #     [31:16] = memWCnt
    #     [15:0] = memRCnt

    HW_VERSION                          = 0xb4, Register32

    # another block of not writable, all 0 on start

    ERROR_STATUS                        = 0xc4, R_PIODMA_ERROR_STATUS

    # 0xd0
    # 0xc0000002
    # 0xd4
    # 0xffffffff
    # 0xd8
    # 0xffffff
    # 0xdc
    # 0xffffffff
    # 0xe0
    # 0xff
    # 0xe4
    # 0xffff

    # TO BE CONFIRMED, FROM SCALER RE
    # XXX it doesn't seem to work
    BASE_ADDR_HI                        = irange(0xf0, 8, 4), Register32


class R_CM3_IRQ_0(Register32):
    MBOX0_EMPTY     = 0
    MBOX0_NOT_EMPTY = 1
    MBOX1_EMPTY     = 2
    MBOX1_NOT_EMPTY = 3
    MBOX2_EMPTY     = 4
    MBOX2_NOT_EMPTY = 5
    MBOX3_EMPTY     = 6
    MBOX3_NOT_EMPTY = 7
    COUNTER0        = 8
    COUNTER1        = 9
    MBOX01_OVERFLOW = 10
    MBOX23_OVERFLOW = 11
    FLAGS0          = 12
    FLAGS1          = 13


class R_CM3_IRQ_1(Register32):
    PIODMA          = 8


class R_AP_IRQ(Register32):
    # AIC line 1011
    MBOX0_EMPTY     = 0
    MBOX0_NOT_EMPTY = 1
    # AIC line 1012
    MBOX1_EMPTY     = 2
    MBOX1_NOT_EMPTY = 3
    # AIC line 1013
    MBOX2_EMPTY     = 4
    MBOX2_NOT_EMPTY = 5
    # AIC line 1014
    MBOX3_EMPTY     = 6
    MBOX3_NOT_EMPTY = 7
    # AIC line 1015
    FLAGS0          = 8
    # AIC line 1016
    FLAGS1          = 9


class R_MBOX_STATUS(Register32):
    # This one bit can be read/written
    ENABLE      = 0
    WPTR        = 10, 8
    RPTR        = 14, 12
    FULL        = 16
    EMPTY       = 17
    # Not sure how to clear these bits?
    OVERFLOW    = 18
    UNDERFLOW   = 19


class R_COUNTER_CONFIG(Register32):
    ENABLE = 0
    # 0 = wrap from 0xffffffff
    # 1 = wrap from value written to count
    RELOAD = 7


class AVDCM3CtrlRegs(RegMap):
    # seems to be read-only
    REG_0x0                             = 0x00, Register32
    # seems to be read-only
    REG_0x4                             = 0x04, Register32
    # bit3 = ???
    # bit2 = ??? hold cpu in reset
    # bit1 = ??? also holds cpu in reset, but differently????
    # bit0 = run???? obviously not, the CPU runs even if i clear it
    # init value is 0x2 and writing 0 is enough to make it boot
    # not sure what the write of 0x1 does
    RUN_CONTROL                         = 0x08, Register32
    # seems to be read-only
    REG_0xc                             = 0x0c, Register32
    CM3_IRQ_ENABLE_0                    = 0x10, R_CM3_IRQ_0
    CM3_IRQ_ENABLE_1                    = 0x14, R_CM3_IRQ_1
    # R/W, 32 bits, may also be CM3 IRQ enables?
    REG_0x18                            = 0x18, Register32
    REG_0x1c                            = 0x1c, Register32
    REG_0x20                            = 0x20, Register32
    REG_0x24                            = 0x24, Register32
    REG_0x28                            = 0x28, Register32
    # Write 1 to clear
    CM3_IRQ_STATUS_CLR_0                = 0x2c, R_CM3_IRQ_0
    CM3_IRQ_STATUS_CLR_1                = 0x30, R_CM3_IRQ_1
    # There may be more IRQ status regs here

    AP_IRQ_ENABLE                       = 0x48, R_AP_IRQ
    # Write 1 to clear
    AP_IRQ_STATUS_CLR                   = 0x4c, R_AP_IRQ
    MAILBOX0_STATUS                     = 0x50, R_MBOX_STATUS
    MAILBOX0_SUBMIT                     = 0x54, Register32
    MAILBOX0_RETRIEVE                   = 0x58, Register32
    MAILBOX1_STATUS                     = 0x5c, R_MBOX_STATUS
    MAILBOX1_SUBMIT                     = 0x60, Register32
    MAILBOX1_RETRIEVE                   = 0x64, Register32
    MAILBOX2_STATUS                     = 0x68, R_MBOX_STATUS
    MAILBOX2_SUBMIT                     = 0x6c, Register32
    MAILBOX2_RETRIEVE                   = 0x70, Register32
    MAILBOX3_STATUS                     = 0x74, R_MBOX_STATUS
    MAILBOX3_SUBMIT                     = 0x78, Register32
    MAILBOX3_RETRIEVE                   = 0x7c, Register32
    # IRQ8 on M3
    COUNTER0_CONFIG                     = 0x80, R_COUNTER_CONFIG
    COUNTER0_VAL                        = 0x84, Register32
    # IRQ9 on M3
    COUNTER1_CONFIG                     = 0x88, R_COUNTER_CONFIG
    COUNTER1_VAL                        = 0x8c, Register32
    # Used to communicate boot completion between fw<->host
    # FLAGS0 = IRQ12
    # FLAGS1 = IRQ13
    FLAGS0_SET                          = 0x90, Register32
    FLAGS1_SET                          = 0x94, Register32
    FLAGS0_CLR                          = 0x98, Register32
    FLAGS1_CLR                          = 0x9c, Register32


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
    # probably two bits???
    # probably corresponds to irq14/15
    DMA_IRQ_ENABLE                      = 0x00, Register32
    DMA_IRQ_STATUS_CLR                  = 0x04, Register32

    IDLE_THING                          = 0x14, Register32
    AVDCTRL_CLOCKGATEENABLE             = 0x18, Register32
