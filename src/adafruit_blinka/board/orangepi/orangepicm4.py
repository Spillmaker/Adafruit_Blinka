# SPDX-FileCopyrightText: 2024 Krister Berntsen - @Spillmaker
#
# SPDX-License-Identifier: MIT
"""Pin definitions for the Orange Pi Compute Module 4."""

from adafruit_blinka.microcontroller.rockchip.rk3566 import pin

# D-pin number is ordered by physical pin sequence
# Reference: Orange Pi provided Ubuntu image has a built-in GPIO utility.
# The following is the output of using ``gpio readall`` on the Orange Pi CM4.

#  +------+-----+----------+--------+---+  PI CM4  +---+--------+----------+-----+------+
#  | GPIO | wPi |   Name   |  Mode  | V | Physical | V |  Mode  | Name     | wPi | GPIO |
#  +------+-----+----------+--------+---+----++----+---+--------+----------+-----+------+
#  |      |     |     3.3V |        |   |  1 || 2  |   |        | 5V       |     |      |
#  |  140 |   0 |    SDA.2 |     IN | 1 |  3 || 4  |   |        | 5V       |     |      |
#  |  141 |   1 |    SCL.2 |     IN | 1 |  5 || 6  |   |        | GND      |     |      |
#  |  147 |   2 |    PWM15 |     IN | 0 |  7 || 8  | 1 | ALT1   | RXD.2    | 3   | 25   |
#  |      |     |      GND |        |   |  9 || 10 | 1 | ALT1   | TXD.2    | 4   | 24   |
#  |  118 |   5 | GPIO3_C6 |     IN | 0 | 11 || 12 | 0 | IN     | GPIO3_C7 | 6   | 119  |
#  |  128 |   7 | GPIO4_A0 |     IN | 0 | 13 || 14 |   |        | GND      |     |      |
#  |  130 |   8 |    TXD.7 |     IN | 0 | 15 || 16 | 0 | IN     | RXD.7    | 9   | 131  |
#  |      |     |     3.3V |        |   | 17 || 18 | 0 | IN     | GPIO4_A1 | 10  | 129  |
#  |  138 |  11 | SPI3_TXD |   ALT4 | 1 | 19 || 20 |   |        | GND      |     |      |
#  |  136 |  12 | SPI3_RXD |   ALT4 | 1 | 21 || 22 | 0 | IN     | TXD.9    | 13  | 132  |
#  |  139 |  14 | SPI3_CLK |   ALT4 | 0 | 23 || 24 | 1 | ALT4   | SPI3_CS1 | 15  | 134  |
#  |      |     |      GND |        |   | 25 || 26 | 0 | IN     | GPIO3_D6 | 16  | 126  |
#  |   32 |  17 |    SDA.3 |   ALT1 | 1 | 27 || 28 | 1 | ALT1   | SCL.3    | 18  | 33   |
#  |  133 |  19 |    RXD.9 |     IN | 0 | 29 || 30 |   |        | GND      |     |      |
#  |  124 |  20 | GPIO3_D4 |     IN | 0 | 31 || 32 | 0 | IN     | PWM11    | 21  | 144  |
#  |  127 |  22 | GPIO3_D7 |     IN | 0 | 33 || 34 |   |        | GND      |     |      |
#  |  120 |  23 | GPIO3_D0 |     IN | 0 | 35 || 36 | 0 | IN     | GPIO3_D5 | 24  | 125  |
#  |  123 |  25 | GPIO3_D3 |     IN | 0 | 37 || 38 | 0 | IN     | GPIO3_D2 | 26  | 122  |
#  |      |     |      GND |        |   | 39 || 40 | 0 | IN     | GPIO3_D1 | 27  | 121  |
#  +------+-----+----------+--------+---+----++----+---+--------+----------+-----+------+
#  | GPIO | wPi |   Name   |  Mode  | V | Physical | V |  Mode  | Name     | wPi | GPIO |
#  +------+-----+----------+--------+---+  PI CM4  +---+--------+----------+-----+------+

# D1 = VCC3V3_SYS
# D2 = VCC5V0_SYS
D3 = pin.GPIO4_B4 # SDA.2
# D4 = VCC5V0_SYS
D5 = pin.GPIO4_B5 # SCL.2
# D6 = GND
D7 = pin.GPIO4_C3 # PWM15
D8 = pin.GPIO0_D1 # RXD.2
# D9 = GND
D10 = pin.GPIO0_D0 # TXD.2
D11 = pin.GPIO3_C6
D12 = pin.GPIO3_C7
D13 = pin.GPIO4_A0
# D14 = GND
D15 = pin.GPIO4_A2 # TXD.7
D16 = pin.GPIO4_A3 # RXD.7
# D17 = Vcc3V3_SYS
D18 = pin.GPIO4_A1
D19 = pin.GPIO4_B2 # SPI3_TXD
# D20 = GND
D21 = pin.GPIO4_B0 # SPI3_RXD
D22 = pin.GPIO4_A4 # TXD.9
D23 = pin.GPIO4_B3 # SPI3_CLK
D24 = pin.GPIO4_A6 # SPI3_CS1
# D25 = GND
D26 = pin.GPIO3_D6
D27 = pin.GPIO1_A0 # SDA.3
D28 = pin.GPIO1_A1 # SCL.3
D29 = pin.GPIO4_A5 # RXD.9
# D30 = GND
D31 = pin.GPIO3_D4
D32 = pin.GPIO4_C0 # PWM11
D33 = pin.GPIO3_D7
# D34 = GND
D35 = pin.GPIO3_D0
D36 = pin.GPIO3_D5
D37 = pin.GPIO3_D3
D38 = pin.GPIO3_D2
# D39 = GND
D40 = pin.GPIO3_D1

# Aliases (Based of the names from the Orange Pi GPIO utility)
SDA_2 = D3
SCL_2 = D5
PWM15 = D7
RXD_2 = D8
TXD_2 = D10
TXD_7 = D15
RXD_7 = D16
SPI3_TXD = D19
SPI3_RXD = D21
TXD_9 = D22
SPI3_CLK = D23
SPI3_CS1 = D24
SDA_3 = D27
SCL_3 = D28
RXD_9 = D29
PWM11 = D32

# SPI configuration
SCLK = SPI3_CLK
MOSI = SPI3_TXD
MISO = SPI3_RXD
CS = SPI3_CS1