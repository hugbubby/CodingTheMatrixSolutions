ciphertext = [21, 4, 21, 11, 25, 3, 11, 21, 4, 25, 26]
def intToChar(num):
    if num == 26:
        return ' '
    else:
        return chr(ord('A') + num)

def t1():
    for i in range(32):
        k = ''
        for j in [intToChar(x ^ i) for x in ciphertext]:
            k += j
        print(k) # EVE IS EVIL
