from tkinter.filedialog import askopenfilename
from stegano import lsb

file = input("file: ")
hello = lsb.reveal(file)
print(hello)
