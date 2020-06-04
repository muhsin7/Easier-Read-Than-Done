
""""converts text to binary"""
inp = str(input('text to hide: '))
var = []
for ch in inp:
    binary = (str((bin(ord(ch))))[2:])
    var.append(binary)
print(var)

