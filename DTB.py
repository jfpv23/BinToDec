def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        return "0"
    elif decimal < 0:
        decimal = abs(decimal)
        binary += "-"
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary