def binary_to_decimal(binary):
    if binary[0] == "-":
        sign = -1
        binary = binary[1:]
    else:
        sign = 1
    decimal = 0
    power = 0
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1
    return sign * decimal