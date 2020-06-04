"""decrypts message"""

from PIL import Image

file_name = input("Enter the name of the file you would like to open: ")
image = Image.open(file_name, "r")
rgb_image = image.convert('RGB')
pix = list(rgb_image.getdata())

bin_arr = []
encrypted_bin_arr = []
for elem in pix:
    """get binary of image"""
    for i in elem:
        binary = bin(i)[2:].zfill(8)
        bin_arr.append(binary)

LSB_arr = []
for i in range(len(bin_arr)):
    elem = bin_arr[i]
    LSB = elem[len(elem) - 1]
    LSB_arr.append(LSB)

l = LSB_arr
result = "".join(chr(int("".join(map(str, l[i:i+8])), 2)) for i in range(0, len(l), 8))
print(result)
