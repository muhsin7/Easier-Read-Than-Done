inp = str(input('prompt: '))

inp2 = str(input('text to hide: '))
var = ''
for ch in inp:
    binary = (str((bin(ord(ch))))[2:])
    var += binary
j = "hello"
var_list = list(j)
print(var_list)



