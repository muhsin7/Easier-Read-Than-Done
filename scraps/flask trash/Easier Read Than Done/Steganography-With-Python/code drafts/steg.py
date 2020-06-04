
text = str(input('text to hide: '))


def msg2bin(text):
    var = ''
    for ch in text:
        binary = (str((bin(ord(ch))))[2:])
        var += binary
        return var


def replace_lsb():
    msgbin_text = []
    for n in msg2bin(text):
        msgbin_text.append(n)
    return msgbin_text


if len(text) > 0:
    print(replace_lsb())
