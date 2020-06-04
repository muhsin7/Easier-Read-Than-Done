text = input("text to hide: ")
print(list(map(bin, bytearray(text.encode('utf-8')))))