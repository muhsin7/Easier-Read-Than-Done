binary = 0o0000100010


def bin2hex(binary):
    print(''.join((hex(int(binary[i:i+8], 2))[2:] for i in range(0, len(binary), 4))))

