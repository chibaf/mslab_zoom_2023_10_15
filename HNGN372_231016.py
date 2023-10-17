#!/usr/bin/env python3
# -*- coding: utf-8 -*-"
""" HNGN001 Created on Tue Jun 11 08:34:11 2019
(two days before 190613) (1month before 190711), work till 1000 codes"""

s000="""
# 一桁の数字（integer）を与えて、それをASCII になおして
# ORIONチラーの温度（10度きざみで）を設定する。

そのとき、BCCを計算する
ロジックというか、pythonコードを以下に作成する
{231016}

番地27, 温度20℃、マニュアルどおりのバイト列とBCCでの、コマンドがあるので
それを変更する形でプログラムする。
"""
print(s000)

# 番地27, 温度20℃、マニュアルどおりのバイト列とBCCでコマンドを送る。
command_SetT=b'\x04\x32\x37\x02\x53\x31\x20\x20\x20\x20\x32\x30\x2E\x30\x03\x7D'
# 
command_SetT_A=b'\x04\x32\x37\x02\x53\x31\x20\x20\x20\x20'
command_SetT_B=b'\x32\x30'         # 20℃
command_SetT_C=b'\x2E\x30\x03\x7D' # '.' 0 ETX BCC
command_SetT_CwoBCC=b'\x2E\x30\x03'    # '.' 0 ETX

command_SetT==(command_SetT_A+command_SetT_B+command_SetT_C)

s001=f"""
マニュアルのコマンドを、温度のところだけはずして分解し、組み立ててみた。
trueが返ってくるか確かめてみる
{command_SetT} ==
{command_SetT_A} + {command_SetT_B} + {command_SetT_C}
{command_SetT==(command_SetT_A+command_SetT_B+command_SetT_C)}

うまくいっている。この分解で良いようだ。
"""

print(s001)

# integer for x and y
x=3 
y=0
x_str=str(x)
y_str=str(y)
setT=x_str + y_str + ".0"


s00=f"""
\nいま、温度の一番上の10の桁の数値を {x} とし、
二番目の1の桁の数値を {y} とすると、
x と y の型は、{type(x)},  {type(y)} 。
設定温度は 10x {x} + {y} + 0.0 と設定。
すなわち、{setT} ℃ と設定する。

BCCを計算するにはEXORをつくるが、それには整数をつかう。
x も y も、このやり方では整数だから、
なにもしないで、このまま、EXOR （^演算子）を取れば良い
"""
print(s00)

# 2は、２進数で表すと、以下
ni= 0b10 

binary_string = bin(ni)


s01=f"""
（確認のために以下ずらずら書きます）

2は、２進数で表すと、以下
x= ni= 0b10 
関数として
bin というのを使えば良い
binary_string = bin(ni)
2進数表現: bin(ni) = {binary_string}

（確認おわり）
"""

print(s01)


work_BCC=x^y^0x2E^0x30^0x03
#        x y   .    0   ETX

s02=f"""
では、
ひとけため、y、についてどうするか？
x と同じで、関数の引数にしても整数にすれば
そのままでよい（なにもしなくて良い）。
x^y^0x2E^0x30^0x03
x y   .    0   ETX
{x} {y}   .    0   ETX
であって、
BCCとしては使わないけれど、ようは
x^y^0x2E^0x30^0x03 
    = 左記のBCC（整数） = {work_BCC}
    = 2進数表現        = {bin(work_BCC)}
    = 16進数表現 hex() = {hex(work_BCC)}
でいいのかな？
"""
print(s02)

BCC= 0x53^0x31^0x20^0x20^0x20^0x20^x^y^0x2E^0x30^0x03

s03=f"""
たぶん、これで良いと思う
すなわち、
BCCの計算はSTX（02h）のあとにつづく 
b'\x53\x31\x20\x20\x20\x20'
#    S  1   SP  SP   SP   SP 
の末尾に
以下をつければ良いのではないか。
x^y^0x2E^0x30^0x03 
だから、よっとこさっとこ、求める
BCCは

BCC=0x53^0x31^0x20^0x20^0x20^0x20^x^y^0x2E^0x30^0x03 
#      S  1    SP    SP   SP   SP x  y  .    0  ETX  

計算すると
BCC= {0x53^0x31^0x20^0x20^0x20^0x20^x^y^0x2E^0x30^0x03}

しつこいけれども、表示方法を変えてみると以下になる。

BCC = 整数での表現       = {BCC}
    = 2進数表現         = {bin(BCC)}
    = 16進数表現 hex()  = {hex(BCC)}
はい。
（ちなみに、(x,y)=(20,0)にするとマニュアルの例と同じになり
    BCCとして、7d、が算出されるので、このロジックは良さそう ）
"""

print(s03)

command_SetT_M=b'\x04\x32\x37\x02\x53\x31\x20\x20\x20\x20\x32\x30\x2E\x30\x03\x7D'
command_SetT =b'\x04\x32\x37\x02\x53\x31\x20\x20\x20\x20\x32\x30\x2E\x30\x03' + bytes([BCC])

# b'20' は文字 '2' と '0' の2つのASCII文字からなるバイト列です。
# bytes([x])+bytes([y])='\x02\x00' すなわち '\x02' と '\x00' は16進数表現で、それぞれ10進数の2と0に対応します。
# この2つは内容的に異なります。
# 文字列を使うもんだからちょっと厄介になる

ascii_byte_x = str(x).encode('ascii')
ascii_byte_y = str(y).encode('ascii')
command_SetT =command_SetT_A + ascii_byte_x + ascii_byte_y + command_SetT_CwoBCC + bytes([BCC])

hex_representation_M = ' '.join([f'{byte:02X}' for byte in command_SetT_M])

hex_representation_setT = ' '.join([f'{byte:02X}' for byte in command_SetT])

s04=f"""
このBCCを使って、マニュアルにある
command_SetT=b'\x04\x32\x37\x02\x53\x31\x20\x20\x20\x20\x32\x30\x2E\x30\x03\x7D'
をつくる。


マニュアルのコマンド{command_SetT_M}
目的のコマンドは{command_SetT}

マニュアルのは、{hex_representation_M} \n
ここx, yでは、{hex_representation_setT}

"""
print(s04)


""" This code is private property of MSLab inc. and it is strictly not permitted to copy any of algorisms in this code without written permission of MSLab inc., copy_right May 2023"""