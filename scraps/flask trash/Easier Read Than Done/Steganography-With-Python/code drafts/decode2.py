"""decrypts message"""

from PIL import Image

file_name = input("Enter the name of the file you would like to open: ")
image = Image.open(file_name, "r")
rgb_image = image.convert('RGB')
pix = list(rgb_image.getdata())

for k in range(len(pix)):
    """get binary of image"""
    elem = pix[k]
    new_tuple = []
    for i in range(len(elem)):
        new_tuple.append(bin(elem[i])[2:].zfill(8))
    pix[k] = tuple(new_tuple)

LSB_arr = []
for i in range(len(pix)):
    for k in range(len(pix[i])):
        LSB = pix[i][k][len(pix[i][k]) - 1]
        LSB_arr.append(LSB)

l = LSB_arr
result = "".join(chr(int("".join(map(str,l[i:i+8])),2)) for i in range(0,len(l),8))
print(result)