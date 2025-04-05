def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476
    original_length = len(message)
    message = bytearray(message)
    message.append(0x80)
    while (len(message) % 64) != 56:
        message.append(0)
    message += (original_length * 8).to_bytes(8, 'little')
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]
        A, B, C, D = a, b, c, d 
        for j in range(64):
            if j < 16:
                F = (B & C) | (~B & D)
                g = j
            elif j < 32:
                F = (D & B) | (~D & C)
                g = (5 * j + 1) % 16
            elif j < 48:
                F = B ^ C ^ D
                g = (3 * j + 5) % 16
            else:
                F = C ^ (B | ~D)
                g = (7 * j) % 16
            temp = D
            D = C
            C = B
            B = B + left_rotate((A + F + words[g] + 0x5A827999) & 0xFFFFFFFF, 3)
            A = temp
        a = (a + A) & 0xFFFFFFFF
        b = (b + B) & 0xFFFFFFFF
        c = (c + C) & 0xFFFFFFFF
        d = (d + D) & 0xFFFFFFFF
    return "{:08x}{:08x}{:08x}{:08x}".format(a, b, c, d)

input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))
print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
