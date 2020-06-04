"""coverts image to binary"""
from PIL import Image

text = input('Enter text to hide: ')
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


text_bytes = list(map(bin, bytearray(text.encode('utf-8'))))
for i in range(len(text_bytes)):
    text_bytes[i] = text_bytes[i][2:].zfill(8)

text_len = 0
for elem in text_bytes:
    text_len += len(elem)

img_len = 0
for elem in pix:
    for k in elem:
        img_len += len(k)

if text_len > img_len:
    print("Message too long")
else:
    ind = 0
    ind2 = 0
    for i in range(len(pix)):
        item = list(pix[i])
        for j in range(len(item)):
            try:
                if ind2 == len(text_bytes[ind]):
                    ind += 1
                    ind2 = 0
                item[j] = item[j][:len(item[j]) - 1] + text_bytes[ind][ind2]
                ind2 += 1
            except IndexError:
                pass
        pix[i] = tuple(item)

for i in range(len(pix)):
    temp = list(pix[i])
    for j in range(len(temp)):
        temp[j] = int(temp[j], 2)
    pix[i] = tuple(temp)

im2 = Image.new(image.mode, image.size)
im2.putdata(pix)
im2.save('out.jpg')