import binascii

""""converts text to binary"""
inp = str(input('text to hide: '))
var = ''
for ch in inp:
    binary = (str((bin(ord(ch))))[2:])
    var += binary
print(var)
chk_points = [7, 15, 23]
for i in chk_points:
    var = var[:i, +'*', var]
    print(var)

