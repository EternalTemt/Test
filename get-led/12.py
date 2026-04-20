def dec2bin(value):
    return list(int(i) for i in bin(value)[2:].zfill(8))
print(dec2bin(1201))