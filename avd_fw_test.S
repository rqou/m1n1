.section .text, "ax" @progbits

.cpu cortex-m3
.syntax unified
.thumb

.global _start
_start:
    .word 0x10010000        // Initial SP
    .word start+1           // Initial start

    .word nmi+1
    .word hardfault+1
    .word memmanage+1
    .word busfault+1
    .word usagefault+1
    .word 0
    .word 0
    .word 0
    .word 0
    .word svcall+1
    .word 0
    .word 0
    .word pendsv+1
    .word systick+1

    .word irq0+1
    .word irq1+1
    .word irq2+1
    .word irq3+1
    .word irq4+1
    .word irq5+1
    .word irq6+1
    .word irq7+1
    .word irq8+1
    .word irq9+1
    .word irq10+1
    .word irq11+1
    .word irq12+1
    .word irq13+1
    .word irq14+1
    .word irq15+1
    .word irq16+1
    .word irq17+1
    .word irq18+1
    .word irq19+1
    .word irq20+1
    .word irq21+1
    .word irq22+1
    .word irq23+1
    .word irq24+1
    .word irq25+1
    .word irq26+1
    .word irq27+1
    .word irq28+1
    .word irq29+1
    .word irq30+1
    .word irq31+1
    .word irq32+1
    .word irq33+1
    .word irq34+1
    .word irq35+1
    .word irq36+1
    .word irq37+1
    .word irq38+1
    .word irq39+1
    .word irq40+1
    .word irq41+1
    .word irq42+1
    .word irq43+1
    .word irq44+1
    .word irq45+1
    .word irq46+1
    .word irq47+1
    .word irq48+1
    .word irq49+1
    .word irq50+1
    .word irq51+1
    .word irq52+1
    .word irq53+1
    .word irq54+1
    .word irq55+1
    .word irq56+1
    .word irq57+1
    .word irq58+1
    .word irq59+1
    .word irq60+1
    .word irq61+1
    .word irq62+1
    .word irq63+1
    .word irq64+1
    .word irq65+1
    .word irq66+1
    .word irq67+1
    .word irq68+1
    .word irq69+1
    .word irq70+1
    .word irq71+1
    .word irq72+1
    .word irq73+1
    .word irq74+1
    .word irq75+1
    .word irq76+1
    .word irq77+1
    .word irq78+1
    .word irq79+1
    .word irq80+1
    .word irq81+1
    .word irq82+1
    .word irq83+1
    .word irq84+1
    .word irq85+1
    .word irq86+1
    .word irq87+1
    .word irq88+1
    .word irq89+1
    .word irq90+1
    .word irq91+1
    .word irq92+1
    .word irq93+1
    .word irq94+1
    .word irq95+1
    .word irq96+1
    .word irq97+1
    .word irq98+1
    .word irq99+1
    .word irq100+1
    .word irq101+1
    .word irq102+1
    .word irq103+1
    .word irq104+1
    .word irq105+1
    .word irq106+1
    .word irq107+1
    .word irq108+1
    .word irq109+1
    .word irq110+1
    .word irq111+1
    .word irq112+1
    .word irq113+1
    .word irq114+1
    .word irq115+1
    .word irq116+1
    .word irq117+1
    .word irq118+1
    .word irq119+1
    .word irq120+1
    .word irq121+1
    .word irq122+1
    .word irq123+1


// hax IPC:
//  +0x00 = status
//  +0x10 = flag
//  +0x14 = addr
//  +0x18 = WnR
//  +0x1c = val
//  +0xf0 = boot count
start:
    mov r0, #0x10000000
    movs r1, #0x55
    str r1, [r0]

    ldr r1, [r0, #0xf0]
    adds r1, #1
    str r1, [r0, #0xf0]

1:
    ldr r1, [r0, #0x10]
    cmp r1, #1
    bne 1b

    // addr
    ldr r1, [r0, #0x14]
    // WnR
    ldr r2, [r0, #0x18]
    cmp r2, #0
    bne 2f
    // read
    ldr r2, [r1]
    str r2, [r0, #0x1c]
    movs r2, #0
    str r2, [r0, #0x10]
    b 1b
2:
    // write
    ldr r2, [r0, #0x1c]
    str r2, [r1]
    movs r2, #0
    str r2, [r0, #0x10]
    b 1b

nmi:
    mov r0, #0x10000000
    movs r1, #0xAA
    str r1, [r0]
    b nmi

hardfault:
    mov r0, #0x10000000
    movs r1, #0xAB
    str r1, [r0]
    b hardfault

memmanage:
    mov r0, #0x10000000
    movs r1, #0xAC
    str r1, [r0]
    b memmanage

busfault:
    mov r0, #0x10000000
    movs r1, #0xAD
    str r1, [r0]
    b busfault

usagefault:
    mov r0, #0x10000000
    movs r1, #0xAE
    str r1, [r0]
    b usagefault

svcall:
    mov r0, #0x10000000
    movs r1, #0xAF
    str r1, [r0]
    b svcall

pendsv:
    mov r0, #0x10000000
    movs r1, #0xB0
    str r1, [r0]
    b pendsv

systick:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b systick

irq0:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq0

irq1:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq1

irq2:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq2

irq3:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq3

irq4:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq4

irq5:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq5

irq6:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq6

irq7:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq7

irq8:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq8

irq9:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq9

irq10:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq10

irq11:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq11

irq12:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq12

irq13:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq13

irq14:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq14

irq15:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq15

irq16:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq16

irq17:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq17

irq18:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq18

irq19:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq19

irq20:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq20

irq21:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq21

irq22:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq22

irq23:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq23

irq24:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq24

irq25:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq25

irq26:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq26

irq27:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq27

irq28:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq28

irq29:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq29

irq30:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq30

irq31:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq31

irq32:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq32

irq33:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq33

irq34:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq34

irq35:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq35

irq36:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq36

irq37:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq37

irq38:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq38

irq39:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq39

irq40:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq40

irq41:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq41

irq42:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq42

irq43:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq43

irq44:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq44

irq45:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq45

irq46:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq46

irq47:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq47

irq48:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq48

irq49:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq49

irq50:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq50

irq51:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq51

irq52:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq52

irq53:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq53

irq54:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq54

irq55:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq55

irq56:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq56

irq57:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq57

irq58:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq58

irq59:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq59

irq60:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq60

irq61:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq61

irq62:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq62

irq63:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq63

irq64:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq64

irq65:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq65

irq66:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq66

irq67:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq67

irq68:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq68

irq69:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq69

irq70:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq70

irq71:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq71

irq72:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq72

irq73:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq73

irq74:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq74

irq75:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq75

irq76:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq76

irq77:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq77

irq78:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq78

irq79:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq79

irq80:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq80

irq81:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq81

irq82:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq82

irq83:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq83

irq84:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq84

irq85:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq85

irq86:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq86

irq87:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq87

irq88:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq88

irq89:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq89

irq90:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq90

irq91:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq91

irq92:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq92

irq93:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq93

irq94:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq94

irq95:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq95

irq96:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq96

irq97:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq97

irq98:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq98

irq99:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq99

irq100:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq100

irq101:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq101

irq102:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq102

irq103:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq103

irq104:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq104

irq105:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq105

irq106:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq106

irq107:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq107

irq108:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq108

irq109:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq109

irq110:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq110

irq111:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq111

irq112:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq112

irq113:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq113

irq114:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq114

irq115:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq115

irq116:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq116

irq117:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq117

irq118:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq118

irq119:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq119

irq120:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq120

irq121:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq121

irq122:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq122

irq123:
    mov r0, #0x10000000
    movs r1, #0xB1
    str r1, [r0]
    b irq123
