#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from m1n1.setup import *
from m1n1.hw.dart8110 import DART8110
from m1n1.utils import *
import struct
import subprocess


p.pmgr_adt_clocks_enable(f'/arm-io/avd0')
p.pmgr_adt_clocks_enable(f'/arm-io/dart-avd0')
avd_base, _ = u.adt[f'/arm-io/avd0'].get_reg(0)

thing0_base     = avd_base + 0x000_0000
thing1_base     = avd_base + 0x000_8000

thing2_base     = avd_base + 0x100_0000
dart_base       = avd_base + 0x101_0000
thing3_base     = avd_base + 0x102_0000

thing4_base     = avd_base + 0x107_0000
cm3_code_base   = avd_base + 0x108_0000
cm3_data_base   = avd_base + 0x109_0000
cm3_ctrl_base   = avd_base + 0x10a_0000

thing5_base     = avd_base + 0x110_0000
thing6_base     = avd_base + 0x110_c000

thing7_base     = avd_base + 0x140_0000

def dump(base, sz):
    data = b''
    for i in range(0, sz, 4):
        addr = base + i
        print(f"{addr:X}")
        val = p.read32(addr)
        data += struct.pack("<I", val)

    return data

def load(base, data):
    for i in range(0, len(data), 4):
        addr = base + i
        print(f"{addr:X}")
        val = struct.unpack("<I", data[i:i+4])[0]
        p.write32(addr, val)

    return data


ret = subprocess.call([
    'arm-none-eabi-gcc',
    '-ggdb',
    '-nostdlib',
    '-Wl,-Ttext,0',
    '-o', 'avd_fw_test.elf',
    'avd_fw_test.S'])
assert ret == 0
ret = subprocess.call([
    'arm-none-eabi-objcopy',
    '-O', 'binary',
    'avd_fw_test.elf',
    'avd_fw_test.bin'])
assert ret == 0


with open('avd_fw_test.bin', 'rb') as f:
    test_fw = f.read()

assert len(test_fw) <= 0x10000
test_fw += b'\x00' * (0x10000 - len(test_fw))


# # ??? tunables
# p.write32(0x286000000 + 0x0, 0x11)
# p.write32(0x286000000 + 0x10, 0xd0000)
# p.write32(0x286000000 + 0x14, 0x1)
# p.write32(0x286000000 + 0x18, 0x1)
# p.write32(0x286000000 + 0x1c, 0x3)
# p.write32(0x286000000 + 0x20, 0x3)
# p.write32(0x286000000 + 0x24, 0x3)
# p.write32(0x286000000 + 0x28, 0x3)
# p.write32(0x286000000 + 0x2c, 0x3)
# p.write32(0x286000000 + 0x400, 0x40a10001)
# p.write32(0x286000000 + 0x600, 0x1ffffff)
# p.write32(0x286000000 + 0x410, 0x1100)
# p.write32(0x286000000 + 0x420, 0x1100)
# p.write32(0x286000000 + 0x430, 0x1100)
# p.write32(0x286000000 + 0x8000, 0x9)
# p.write32(0x286000000 + 0x820, 0x80)
# p.write32(0x286000000 + 0x8008, 0x7)
# p.write32(0x286000000 + 0x8014, 0x1)
# p.write32(0x286000000 + 0x8018, 0x1)
# p.write32(0x286000000 + 0x7a8, 0x1)
# p.write32(0x286000000 + 0x8208, 0x4)
# p.write32(0x286000000 + 0x8280, 0x20)
# p.write32(0x286000000 + 0x8288, 0x3)
# p.write32(0x286000000 + 0x828c, 0xc)
# p.write32(0x286000000 + 0x8290, 0x18)
# p.write32(0x286000000 + 0x8294, 0x30)
# p.write32(0x286000000 + 0x8298, 0x78)
# p.write32(0x286000000 + 0x829c, 0xf0)
# p.write32(0x286000000 + 0x82b8, 0x1)
# p.write32(0x286000000 + 0x82bc, 0x1)
# p.write32(0x286000000 + 0x82c0, 0x1)
# p.write32(0x286000000 + 0x7a8, 0x1)
# p.write32(0x286000000 + 0x820c, 0x5)
# p.write32(0x286000000 + 0x8284, 0x20)
# p.write32(0x286000000 + 0x82a0, 0x3)
# p.write32(0x286000000 + 0x82a4, 0xc)
# p.write32(0x286000000 + 0x82a8, 0x18)
# p.write32(0x286000000 + 0x82ac, 0x30)
# p.write32(0x286000000 + 0x82b0, 0x78)
# p.write32(0x286000000 + 0x82b4, 0xf0)
# p.write32(0x286000000 + 0x82b8, 0x3)
# p.write32(0x286000000 + 0x82bc, 0x2)
# p.write32(0x286000000 + 0x82c0, 0x3)
# p.write32(0x286000000 + 0x8210, 0x0)
# p.write32(0x286000000 + 0x8408, 0xd)
# p.write32(0x286000000 + 0x8418, 0x3)
# p.write32(0x286000000 + 0x841c, 0x0)
# p.write32(0x286000000 + 0x8420, 0xff)
# p.write32(0x286000000 + 0x8424, 0x0)
# p.write32(0x286000000 + 0x8428, 0xfff)
# p.write32(0x286000000 + 0x82b8, 0x7)
# p.write32(0x286000000 + 0x82bc, 0x4)
# p.write32(0x286000000 + 0x82c0, 0x7)

# skipping DART here

# # ??? more tunables?
# p.write32(0x286000000 + 0x8014, 0x1)
# p.write32(0x286000000 + 0x82bc, 0x1)
# p.write32(0x286000000 + 0x82bc, 0x2)
# p.write32(0x286000000 + 0x82bc, 0x4)
# p.write32(0x286000000 + 0x0, 0x11)
# p.write32(0x286000000 + 0x10, 0xd0000)
# p.write32(0x286000000 + 0x14, 0x1)
# p.write32(0x286000000 + 0x18, 0x1)
# p.write32(0x286000000 + 0x1c, 0x3)
# p.write32(0x286000000 + 0x20, 0x3)
# p.write32(0x286000000 + 0x24, 0x3)
# p.write32(0x286000000 + 0x28, 0x3)
# p.write32(0x286000000 + 0x2c, 0x3)
# p.write32(0x286000000 + 0x400, 0x40a10001)
# p.write32(0x286000000 + 0x600, 0x1ffffff)
# p.write32(0x286000000 + 0x410, 0x1100)
# p.write32(0x286000000 + 0x420, 0x1100)
# p.write32(0x286000000 + 0x430, 0x1100)
# p.write32(0x286000000 + 0x8000, 0x9)
# p.write32(0x286000000 + 0x820, 0x80)
# p.write32(0x286000000 + 0x8008, 0x7)
# p.write32(0x286000000 + 0x8014, 0x1)
# p.write32(0x286000000 + 0x8018, 0x1)
# p.write32(0x286000000 + 0x7a8, 0x1)
# p.write32(0x286000000 + 0x8208, 0x4)
# p.write32(0x286000000 + 0x8280, 0x20)
# p.write32(0x286000000 + 0x8288, 0x3)
# p.write32(0x286000000 + 0x828c, 0xc)
# p.write32(0x286000000 + 0x8290, 0x18)
# p.write32(0x286000000 + 0x8294, 0x30)
# p.write32(0x286000000 + 0x8298, 0x78)
# p.write32(0x286000000 + 0x829c, 0xf0)
# p.write32(0x286000000 + 0x82b8, 0x1)
# p.write32(0x286000000 + 0x82bc, 0x1)
# p.write32(0x286000000 + 0x82c0, 0x1)
# p.write32(0x286000000 + 0x7a8, 0x1)
# p.write32(0x286000000 + 0x820c, 0x5)
# p.write32(0x286000000 + 0x8284, 0x20)
# p.write32(0x286000000 + 0x82a0, 0x3)
# p.write32(0x286000000 + 0x82a4, 0xc)
# p.write32(0x286000000 + 0x82a8, 0x18)
# p.write32(0x286000000 + 0x82ac, 0x30)
# p.write32(0x286000000 + 0x82b0, 0x78)
# p.write32(0x286000000 + 0x82b4, 0xf0)
# p.write32(0x286000000 + 0x82b8, 0x3)
# p.write32(0x286000000 + 0x82bc, 0x2)
# p.write32(0x286000000 + 0x82c0, 0x3)
# p.write32(0x286000000 + 0x8210, 0x0)
# p.write32(0x286000000 + 0x8408, 0xd)
# p.write32(0x286000000 + 0x8418, 0x3)
# p.write32(0x286000000 + 0x841c, 0x0)
# p.write32(0x286000000 + 0x8420, 0xff)
# p.write32(0x286000000 + 0x8424, 0x0)
# p.write32(0x286000000 + 0x8428, 0xfff)
# p.write32(0x286000000 + 0x82b8, 0x7)
# p.write32(0x286000000 + 0x82bc, 0x4)
# p.write32(0x286000000 + 0x82c0, 0x7)

# power on
p.write32(thing2_base + 0x0, 0x1fff)

# # XXX DART stuff?
# dart = DART8110.from_adt(u, f'/arm-io/dart-avd0')
# dart.initialize()
# dart.regs.TCR[15].val = 0x2
# dart.regs.TTBR[15].val = 0x200000
# dart.invalidate_streams()

load(cm3_code_base, test_fw)

p.write32(cm3_ctrl_base + 0x08, 0xe)
p.write32(cm3_ctrl_base + 0x10, 0)
p.write32(cm3_ctrl_base + 0x48, 0)

# # tunables
# p.write32(0x286000000 + 0x1100008, 0x80000000)
# p.write32(0x286000000 + 0x1101000, 0x80000000)
# p.write32(0x286000000 + 0x1101100, 0x80000000)
# p.write32(0x286000000 + 0x1101200, 0x80000000)
# p.write32(0x286000000 + 0x1101300, 0x80000000)
# p.write32(0x286000000 + 0x1101400, 0x80000000)
# p.write32(0x286000000 + 0x1101500, 0x80000000)
# p.write32(0x286000000 + 0x1101600, 0x80000000)
# p.write32(0x286000000 + 0x1101700, 0x80000000)
# p.write32(0x286000000 + 0x1101800, 0x80000000)
# p.write32(0x286000000 + 0x1104000, 0x80000000)
# p.write32(0x286000000 + 0x1104100, 0x80000000)
# p.write32(0x286000000 + 0x1104200, 0x80000000)
# p.write32(0x286000000 + 0x1104300, 0x80000000)
# p.write32(0x286000000 + 0x1104400, 0x80000000)
# p.write32(0x286000000 + 0x1104500, 0x80000000)
# p.write32(0x286000000 + 0x1104600, 0x80000000)
# p.write32(0x286000000 + 0x110c000, 0x1)
# p.write32(0x286000000 + 0x110c080, 0x800107ff)
# p.write32(0x286000000 + 0x110c084, 0x28)
# p.write32(0x286000000 + 0x110c0c0, 0x800107ff)
# p.write32(0x286000000 + 0x110c0c4, 0x280028)
# p.write32(0x286000000 + 0x110c100, 0x800107ff)
# p.write32(0x286000000 + 0x110c104, 0x500028)
# p.write32(0x286000000 + 0x110c140, 0x800107ff)
# p.write32(0x286000000 + 0x110c144, 0x780028)
# p.write32(0x286000000 + 0x110c180, 0x800107ff)
# p.write32(0x286000000 + 0x110c184, 0x520028)
# p.write32(0x286000000 + 0x110c1c0, 0x800107ff)
# p.write32(0x286000000 + 0x110c1c4, 0x7a0028)
# p.write32(0x286000000 + 0x110c200, 0x800107ff)
# p.write32(0x286000000 + 0x110c204, 0xa20028)
# p.write32(0x286000000 + 0x110c240, 0x800107ff)
# p.write32(0x286000000 + 0x110c244, 0xca0028)
# p.write32(0x286000000 + 0x110c280, 0x800107ff)
# p.write32(0x286000000 + 0x110c284, 0xa00020)
# p.write32(0x286000000 + 0x110c2c0, 0x800107ff)
# p.write32(0x286000000 + 0x110c2c4, 0xc00020)
# p.write32(0x286000000 + 0x110c300, 0x800107ff)
# p.write32(0x286000000 + 0x110c304, 0xe00020)
# p.write32(0x286000000 + 0x110c340, 0x800107ff)
# p.write32(0x286000000 + 0x110c344, 0x1000020)
# p.write32(0x286000000 + 0x110c380, 0x800107ff)
# p.write32(0x286000000 + 0x110c384, 0xa)
# p.write32(0x286000000 + 0x110c3c0, 0x800107ff)
# p.write32(0x286000000 + 0x110c3c4, 0xa000a)
# p.write32(0x286000000 + 0x110c400, 0x800107ff)
# p.write32(0x286000000 + 0x110c404, 0x14000a)
# p.write32(0x286000000 + 0x110c440, 0x800107ff)
# p.write32(0x286000000 + 0x110c444, 0x1e000a)
# p.write32(0x286000000 + 0x110c480, 0x800107ff)
# p.write32(0x286000000 + 0x110c484, 0x120000c)
# p.write32(0x286000000 + 0x110c4c0, 0x800107ff)
# p.write32(0x286000000 + 0x110c4c4, 0x12c000c)
# p.write32(0x286000000 + 0x110c500, 0x800107ff)
# p.write32(0x286000000 + 0x110c504, 0x138000c)
# p.write32(0x286000000 + 0x110c540, 0x800107ff)
# p.write32(0x286000000 + 0x110c544, 0x144000c)
# p.write32(0x286000000 + 0x110c580, 0x800107ff)
# p.write32(0x286000000 + 0x110c584, 0xf20020)
# p.write32(0x286000000 + 0x110c5c0, 0x800107ff)
# p.write32(0x286000000 + 0x110c5c4, 0x1120020)
# p.write32(0x286000000 + 0x110c600, 0x800107ff)
# p.write32(0x286000000 + 0x110c604, 0x1320020)
# p.write32(0x286000000 + 0x110c640, 0x800107ff)
# p.write32(0x286000000 + 0x110c644, 0x1520020)
# p.write32(0x286000000 + 0x110c680, 0x800107ff)
# p.write32(0x286000000 + 0x110c684, 0x1500018)
# p.write32(0x286000000 + 0x110c6c0, 0x800107ff)
# p.write32(0x286000000 + 0x110c6c4, 0x28000a)
# p.write32(0x286000000 + 0x110c700, 0x800107ff)
# p.write32(0x286000000 + 0x110c704, 0x168000e)
# p.write32(0x286000000 + 0x110c740, 0x800107ff)
# p.write32(0x286000000 + 0x110c744, 0x32000a)
# p.write32(0x286000000 + 0x110c780, 0x800107ff)
# p.write32(0x286000000 + 0x110c784, 0x176000a)
# p.write32(0x286000000 + 0x110c7c0, 0x800107ff)
# p.write32(0x286000000 + 0x110c7c4, 0x3c000c)
# p.write32(0x286000000 + 0x110c800, 0x800107ff)
# p.write32(0x286000000 + 0x110c804, 0x1800012)
# p.write32(0x286000000 + 0x110c840, 0x800107ff)
# p.write32(0x286000000 + 0x110c844, 0x48000a)
# p.write32(0x286000000 + 0x110c880, 0x800107ff)
# p.write32(0x286000000 + 0x110c884, 0x192000a)
# p.write32(0x286000000 + 0x110c8c0, 0x800107ff)
# p.write32(0x286000000 + 0x110c8c4, 0x1720018)
# p.write32(0x286000000 + 0x110c900, 0x800113ff)
# p.write32(0x286000000 + 0x110c904, 0x19c011c)
# p.write32(0x286000000 + 0x110c940, 0x800113ff)
# p.write32(0x286000000 + 0x110c944, 0x2b8011c)
# p.write32(0x286000000 + 0x110c980, 0x800113ff)
# p.write32(0x286000000 + 0x110c984, 0x3d4011c)
# p.write32(0x286000000 + 0x110c9c0, 0x800113ff)
# p.write32(0x286000000 + 0x110c9c4, 0x4f0011c)
# p.write32(0x286000000 + 0x110e000, 0x1)
# p.write32(0x286000000 + 0x110e080, 0x800207ff)
# p.write32(0x286000000 + 0x110e084, 0x1c)
# p.write32(0x286000000 + 0x110e0c0, 0x800207ff)
# p.write32(0x286000000 + 0x110e0c4, 0x2e)
# p.write32(0x286000000 + 0x110e100, 0x800207ff)
# p.write32(0x286000000 + 0x110e104, 0x1c0054)
# p.write32(0x286000000 + 0x110e140, 0x800207ff)
# p.write32(0x286000000 + 0x110e144, 0x2e009e)
# p.write32(0x286000000 + 0x110e180, 0x800207ff)
# p.write32(0x286000000 + 0x110e184, 0x700016)
# p.write32(0x286000000 + 0x110e1c0, 0x800207ff)
# p.write32(0x286000000 + 0x110e1c4, 0xcc0022)
# p.write32(0x286000000 + 0x110e200, 0x800207ff)
# p.write32(0x286000000 + 0x110e204, 0x860020)
# p.write32(0x286000000 + 0x110e240, 0x800207ff)
# p.write32(0x286000000 + 0x110e244, 0xee0020)
# p.write32(0x286000000 + 0x110e280, 0x800207ff)
# p.write32(0x286000000 + 0x110e284, 0xa6000c)
# p.write32(0x286000000 + 0x110e2c0, 0x800207ff)
# p.write32(0x286000000 + 0x110e2c4, 0x10e000c)
# p.write32(0x286000000 + 0x110e300, 0x80023fff)
# p.write32(0x286000000 + 0x110e304, 0xbc00d0)
# p.write32(0x286000000 + 0x110e340, 0x800207ff)
# p.write32(0x286000000 + 0x110e344, 0xb2000a)
# p.write32(0x286000000 + 0x110e380, 0x800207ff)
# p.write32(0x286000000 + 0x110e384, 0x11a000a)
# p.write32(0x286000000 + 0x110e3c0, 0x800207ff)
# p.write32(0x286000000 + 0x110e3c4, 0x18c0012)
# p.write32(0x286000000 + 0x110e400, 0x800207ff)
# p.write32(0x286000000 + 0x110e404, 0x1240020)
# p.write32(0x286000000 + 0x110e440, 0x800207ff)
# p.write32(0x286000000 + 0x110e444, 0x19e0068)
# p.write32(0x286000000 + 0x110e480, 0x800207ff)
# p.write32(0x286000000 + 0x110e484, 0x1440060)
# p.write32(0x286000000 + 0x110e4c0, 0x80034071)
# p.write32(0x286000000 + 0x110e4c8, 0x21e009e)
# p.write32(0x286000000 + 0x110e4cc, 0x206000c)
# p.write32(0x286000000 + 0x110e500, 0x80056071)
# p.write32(0x286000000 + 0x110e508, 0x2bc009e)
# p.write32(0x286000000 + 0x110e50c, 0x212000c)
# p.write32(0x286000000 + 0x110e800, 0x1)
# p.write32(0x286000000 + 0x110e880, 0x800207ff)
# p.write32(0x286000000 + 0x110e884, 0x16)
# p.write32(0x286000000 + 0x110e8c0, 0x800207ff)
# p.write32(0x286000000 + 0x110e8c4, 0x22)
# p.write32(0x286000000 + 0x110e900, 0x800207ff)
# p.write32(0x286000000 + 0x110e904, 0x160022)
# p.write32(0x286000000 + 0x110e940, 0x800207ff)
# p.write32(0x286000000 + 0x110e944, 0x22003a)
# p.write32(0x286000000 + 0x110e980, 0x80770003)
# p.write32(0x286000000 + 0x1400018, 0x1)
# p.write32(0x286000000 + 0x1070000, 0x0)
# p.write32(0x286000000 + 0x1070010, 0xfff3)
# p.write32(0x286000000 + 0x1070014, 0xfff3)
# p.write32(0x286000000 + 0x1070018, 0xfff3)
# p.write32(0x286000000 + 0x107001c, 0xfff0)
# p.write32(0x286000000 + 0x1070020, 0xfff0)

p.write32(cm3_ctrl_base + 0x10, 0x0)
p.write32(cm3_ctrl_base + 0x48, 0x0)
p.write32(cm3_ctrl_base + 0x50, 0x1)
p.write32(cm3_ctrl_base + 0x68, 0x1)
p.write32(cm3_ctrl_base + 0x5c, 0x1)
p.write32(cm3_ctrl_base + 0x74, 0x1)
p.write32(cm3_ctrl_base + 0x10, 0x2)
p.write32(cm3_ctrl_base + 0x48, 0x8)

p.write(cm3_ctrl_base + 0x08, 1)


# NOTE: the following loop runs the following number of times per second
# start:
#    mov r0, #0x10000000
#    movs r1, #0
#1:
#    str r1, [r0]
#    adds r1, #1
#    b 1b
# 64397529
# 64383456
# 64390321
# 64386696
# 64387557
# 64384937
# 64395642
# 64390264
# 64387706
# 64391074
# 64382244
# 64392814
# 64363923
# 64393883
# 64366853
# 64385064
# 64385699
# 64392906
# 64374883
# 64389206
# 64370786
# 64391695
# 64373101
