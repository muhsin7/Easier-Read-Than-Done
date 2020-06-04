"""coverts image to binary"""

from PIL import Image

text = input('Enter text to hide: ')
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

text_bytes = list(map(bin, bytearray(text.encode('utf-8'))))

for i in range(len(text_bytes)):
    text_bytes[i] = text_bytes[i][2:].zfill(8)



total_len = 0
for elem in text_bytes:
    total_len += len(elem)

ind = 0
ind2 = 0
if total_len > len(bin_arr):
    print("Message too long")
else:
    for i in range(len(bin_arr)):
        elem = bin_arr[i]
        try:
            if ind2 == len(text_bytes[ind]):
                ind += 1
                ind2 = 0
            new_elem = elem[:len(elem) - 1] + text_bytes[ind][ind2]
            encrypted_bin_arr.append(new_elem)
            ind2 += 1
        except IndexError:
            encrypted_bin_arr.append(elem)

enc_tuples_list = []
k = 0
s = 3
count = int(len(encrypted_bin_arr) / 3)
for i in range(count):
    elem = encrypted_bin_arr[k:s]
    for i in range(len(elem)):
        elem[i] = int(elem[i], 2)
        if elem[i] > 255 or elem[i] < 0:
            print(elem[i])
    enc_tuples_list.append(tuple(elem))
    k = s
    s += 3

im2 = Image.new(image.mode, image.size)
im2.putdata(enc_tuples_list)

new_filename = input("what would you like to save your new image as?: ")
im2.save(new_filename+".png")

print("Done! Your new image can be found in the source folder of the cover image")
