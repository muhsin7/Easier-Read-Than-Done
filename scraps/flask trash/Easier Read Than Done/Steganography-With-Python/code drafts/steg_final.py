from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image

root = Tk()
root.geometry("700x300")
root.title("Steganography with Python!")


def callback(entry_name):
    global entry
    entry = entry_name.get()
    print(entry)

class newWindows:
    def encode_window(root):
        window = Toplevel(root)
        window.title("Encode")
        window.geometry("300x300")

        filename = Button(window, text="Select File", command =lambda: askopenfilename()).pack() #selectfile
        Label(window, text="What text would you like to hide in the image:").pack()      #askmessage
        text = Entry(window).pack()
        Button(window, text="Submit Text", command=lambda: callback(text)).pack()        #submit

        Label(window, text="What would you like to save your new image as?: ").pack()
        save_text = Entry(window).pack()
        Button(window, text="Submit file name", command=lambda: callback(save_text)).pack()

        file_name = filename
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

        text_bytes = list(map(bin, bytearray(entry.encode('utf-8'))))

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

        new_name = Entry(window).pack()
        new_filename = new_name
        im2.save(new_filename + '.jpg')


    def decode_window(root):
        window2 = Toplevel(root)
        window2.title("Decode")
        window2.geometry("300x300")
        filename = Button(window2, text="Select File", command =lambda: askopenfilename()).pack()
        image = Image.open(filename, "r")
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
        Label(window2, text="Decoded Text:").pack()
        Label(text=result).pack()

'''starting screen text'''
welcome = Label(root, text="Hide or reveal messages inside images")
welcome.pack()
crossroad1 = Label(root, text='Select "Encode" if you want to hide messages in images')
crossroad1.pack()
crossroad2 = Label(root, text='Select "Decode" if you want to reveal messages in images')
crossroad2.pack()

'''encode/decode buttons'''
encode = Button(root, text="Encode", command=lambda: newWindows.encode_window(root))
encode.pack()
decode = Button(root, text="Decode", command=lambda: newWindows.decode_window(root))
decode.pack()

root.mainloop()

