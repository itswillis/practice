def dec_convert_to_radix(num, radix):
    a = num // radix
    b = num % radix
    if (a > 0):
        result = b + 10 * dec_convert_to_radix(a, radix)
    else:
        result = b
    return result

print(dec_convert_to_radix(37, 4))