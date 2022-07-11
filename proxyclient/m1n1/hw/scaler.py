# SPDX-License-Identifier: MIT
from ..utils import *
from enum import IntEnum


### NOTE: This is "MSR10j" (M1 Max), and there definitely *ARE* differences from M1

class R_IRQS(Register32):
    DONE = 0
    DBGSTS_ERROR = 1
    # presumably one is read and one is write?
    RW_ERROR_A = 3
    RW_ERROR_B = 4
    DECOMPRESSION_ERROR = 9
    CONTEXT_SWITCH = 10
    _BIT11 = 11
    AXI_ERROR = 12
    _BIT13 = 13

class ScalerMainRegs(RegMap):
    # on startup 1 will be written followed by 0
    # but it's not clear if that actually does anything
    HW_VERSION                      = 0x00000, Register32
    # bit0 = normal, bit1 = apiodma related
    # if things are reset here, reading all other regs will *HANG*
    RESET                           = 0x00004, Register32
    # can set 0x1f00
    RESET_APIODMA_RELATED           = 0x00008, Register32
    IS_RUNNING                      = 0x0000c, Register32
    # writable, can set to 0xfff
    REG_0x10                        = 0x00010, Register32
    REGISTER_FIFO_AVAILABILITY      = 0x00014, Register32
    # XNU sets 0x121b, we can at most set 0x3e1b
    IRQ_ENABLE                      = 0x00018, R_IRQS
    MSR_GLBL_IRQSTS                 = 0x0001c, R_IRQS
    FRAME_COUNT                     = 0x00020, Register32

    # 1, or 3 if readonly??
    START                           = 0x00080, Register32

    # 0x3f3d?
    MSR_CTRL_DBGSTS                 = 0x0009c, Register32

    PROFILING_RELATED               = 0x000a4, Register32

    TRANSFORM_ID                    = 0x00110, Register32

    RDMA_THING0                     = 0x00180, Register32
    RDMA_THING1                     = 0x00184, Register32
    RDMA_THING2                     = 0x00188, Register32
    RDMA_THING3                     = 0x0018c, Register32
    RDMA_THING4                     = 0x00190, Register32

    # there's probably another source plane existing?
    SRC_PLANE0_LO                   = 0x00198, Register32
    SRC_PLANE0_HI                   = 0x0019c, Register32
    SRC_PLANE1_LO                   = 0x001a0, Register32
    SRC_PLANE1_HI                   = 0x001a4, Register32
    SRC_PLANE2_LO                   = 0x001a8, Register32
    SRC_PLANE2_HI                   = 0x001ac, Register32

    SRC_PLANE0_COMPRESSEDTHING_LO   = 0x001b8, Register32
    SRC_PLANE0_COMPRESSEDTHING_HI   = 0x001bc, Register32
    SRC_PLANE1_COMPRESSEDTHING_LO   = 0x001c0, Register32
    SRC_PLANE1_COMPRESSEDTHING_HI   = 0x001c4, Register32
    SRC_PLANE2_COMPRESSEDTHING_LO   = 0x001c8, Register32
    SRC_PLANE2_COMPRESSEDTHING_HI   = 0x001cc, Register32

    SRC_PLANE0_STRIDE               = 0x001d8, Register32
    SRC_PLANE1_STRIDE               = 0x001dc, Register32
    SRC_PLANE2_STRIDE               = 0x001e0, Register32

    SRC_PLANE0_OFFSET               = 0x001e8, Register32
    SRC_PLANE1_OFFSET               = 0x001ec, Register32
    SRC_PLANE2_OFFSET               = 0x001f0, Register32

    SRC_SWIZZLE                     = 0x001f8, Register32
    SRC_SIZE_THING0                 = 0x001fc, Register32
    SRC_SIZE_THING1                 = 0x00200, Register32
    CACHE_HINTS_THING0              = irange(0x00204, 4, 4), Register32
    CACHE_HINTS_THING1              = irange(0x00214, 4, 4), Register32
    TUNABLES_THING0                 = irange(0x00224, 4, 4), Register32
    SRC_SIZE_THING2                 = 0x00234, Register32
    SRC_SIZE_THING3                 = 0x00238, Register32
    SRC_SIZE_THING4                 = 0x0023c, Register32

    SRC_SIZE_THING5                 = 0x00244, Register32
    SRC_SIZE_THING6                 = 0x00248, Register32
    SRC_SIZE_THING7                 = 0x0024c, Register32

    WDMA_THING0                     = 0x00280, Register32
    WDMA_THING1                     = 0x00284, Register32
    WDMA_THING2                     = 0x00288, Register32
    WDMA_THING3                     = 0x0028c, Register32
    DST_PLANE0_LO                   = 0x00290, Register32
    DST_PLANE0_HI                   = 0x00294, Register32
    DST_PLANE1_LO                   = 0x00298, Register32
    DST_PLANE1_HI                   = 0x0029c, Register32
    DST_PLANE2_LO                   = 0x002a0, Register32
    DST_PLANE2_HI                   = 0x002a4, Register32
    DST_PLANE0_COMPRESSEDTHING_LO   = 0x002a8, Register32
    DST_PLANE0_COMPRESSEDTHING_HI   = 0x002ac, Register32
    DST_PLANE1_COMPRESSEDTHING_LO   = 0x002b0, Register32
    DST_PLANE1_COMPRESSEDTHING_HI   = 0x002b4, Register32
    DST_PLANE2_COMPRESSEDTHING_LO   = 0x002b8, Register32
    DST_PLANE2_COMPRESSEDTHING_HI   = 0x002bc, Register32
    DST_PLANE0_STRIDE               = 0x002c0, Register32
    DST_PLANE1_STRIDE               = 0x002c4, Register32
    DST_PLANE2_STRIDE               = 0x002c8, Register32
    DST_PLANE0_OFFSET               = 0x002cc, Register32
    DST_PLANE1_OFFSET               = 0x002d0, Register32
    DST_PLANE2_OFFSET               = 0x002d4, Register32
    DST_SWIZZLE                     = 0x002d8, Register32
    DST_SIZE_THING0                 = 0x002dc, Register32
    DST_SIZE_THING1                 = 0x002e0, Register32
    # uhh is there a macos bug with these? last val always overwritten
    CACHE_HINTS_THING2              = irange(0x002e4, 3, 4), Register32
    CACHE_HINTS_THING3              = irange(0x002f0, 3, 4), Register32
    TUNABLES_THING1                 = irange(0x002fc, 3, 4), Register32
    DST_SIZE_THING2                 = 0x00308, Register32
    DST_SIZE_THING3                 = 0x0030c, Register32
    DST_SIZE_THING4                 = 0x00310, Register32
    DST_SIZE_THING5                 = 0x00314, Register32
    DST_SIZE_THING6                 = 0x00318, Register32
    DST_SIZE_THING7                 = 0x0031c, Register32
