Title: RaspberryPI 2 Model BのGPIOピン配置
Date: 2016-01-21 19:00
Category: RaspberryPI
Tags: RaspberryPI, Rasbian, GPIO
Author: TakesxiSximada
Summary: RaspberryPI 2 Model BのGPIOピン配置

RaspberryPI 2 Model Bを触る機会があったのでGPIOピン配置をメモしておきます。

| Pin | Name                | - | Name                | Pin |
|:---:|:--------------------|:-:|:-------------------:|:---:|
| 01  | 3.3V                | - | 5V                  | 02  |
| 03  | GPIO2/SDA1 I2C      | - | 5V                  | 04  |
| 05  | GPIO3/SCL1 I2C      | - | Gnd                 | 06  |
| 07  | GPIO4/GPCLK0 1 Wire | - | GPIO14/UART0_TXD    | 08  |
| 09  | Gnd                 | - | GPIO15/UART0_RXD    | 10  |
| 11  | GPIO17              | - | GPIO18/PWM_CLK      | 12  |
| 13  | GPIO27/PCM_DOUT     | - | Gnd                 | 14  |
| 15  | GPIO22              | - | GPIO23              | 16  |
| 17  | 3.3V                | - | GPIO24              | 18  |
| 19  | GPIO10/SPI0_MOSI    | - | Gnd                 | 20  |
| 21  | GPIO9/SPI0_MISO     | - | GPIO25              | 22  |
| 23  | GPIO11/SPI0_SCLK    | - | GPIO8/SPI0_CEO      | 24  |
| 25  | Gnd                 | - | GPIO7/SPI0_CE1      | 26  |
| 27  | GPIO0/ID SD         | - | GPIO1/ID SC         | 28  |
| 29  | GPIO5               | - | Gnd                 | 30  |
| 31  | GPIO6               | - | GPIO12              | 32  |
| 33  | GPIO13              | - | Gnd                 | 34  |
| 35  | GPIO19              | - | GPIO16              | 36  |
| 37  | GPIO26              | - | GPIO20              | 38  |
| 40  | Gnd                 | - | GPIO21              | 41  |