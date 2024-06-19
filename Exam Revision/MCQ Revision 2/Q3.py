def radix_convert_to_dec(num, radix):
    a = num // 10
    b = num % 10
    if (a > 0):
        result = b + radix * radix_convert_to_dec(a, radix)
    else:
        result = b
    return result

print(radix_convert_to_dec(111, 2))