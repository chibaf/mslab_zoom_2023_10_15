# 231015のメモです

"""
{231015}
（結論）

小数点以下は、たとえば 0 に固定しておく。
上の２桁だけ動かすようにする。たとえば

10.0 20.0 30.0 .... 90.0 

で、うごかしてみる。
"""

#（議論）

"""
0x32^0x30^0x2E^0x30  <== ASCII そのもの
 2    0    .   0   
"""

# 3.67 から　 3.7 にするには？
x = 3.67
rounded_x = round(x, 1)
print(rounded_x) # 3.7

rounded_x = 3
rounded_x_str = str(rounded_x)


# "3.7" を分解して"3"と "." と "7" にするには？
s = "3.7"
integer_part, decimal_point, decimal_part = s.partition('.')
print(integer_part, decimal_point, decimal_part) 





