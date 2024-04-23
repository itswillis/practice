def get_ascii_value(username):
    first = username[0]
    last = username[-1]

    first_1 = ord(first)
    last_1 = ord(last)

    return (first_1 + last_1)

    


print(get_ascii_value('Akim161'))
print(get_ascii_value('Akim161'))
print(get_ascii_value('mgra734'))
print(get_ascii_value('dng004'))
print(get_ascii_value('bcar035'))

