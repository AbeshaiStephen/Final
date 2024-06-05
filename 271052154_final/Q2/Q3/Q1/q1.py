def dec_to_binary(decimal):
    if decimal == 0:
        return 0
    else:
        return decimal % 2 + 10 * (dec_to_binary(decimal // 2))

def binary_to_dec(binary):
    if binary == 0:
        return 0
    else:
        return binary % 10 + 2 * binary_to_dec(binary // 10)

print(dec_to_binary(7))

print(binary_to_dec(111))