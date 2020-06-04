from PIL import Image
import textwrap

file_name = input("Enter the name of the file you would like to open: ")
image = Image.open(file_name, "r")
rgb_image = image.convert('RGB')
pix = list(rgb_image.getdata())

lsb_arr = []
for elem in pix:
    """get binary of image"""
    for i in elem:
        binary = bin(i)[2:]
        lsb = binary[len(binary)-1]
        lsb_arr.append(lsb)

lsb_string = ''.join(lsb_arr)

lsb_wrap = textwrap.wrap(lsb_string, 3)

print(lsb_wrap)
