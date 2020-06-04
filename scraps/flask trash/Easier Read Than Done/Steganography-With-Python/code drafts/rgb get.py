from PIL import Image

file_name = input("Enter the name of the file you would like to open: ")
image = Image.open(file_name, "r")
rgb_image = image.convert('RGB')
pix = list(rgb_image.getdata())

bin_arr = []
for elem in pix:
    """get binary of image"""
    for i in elem:
        binary = bin(i)[2:].zfill(8)
        bin_arr.append(binary)

print(bin_arr)