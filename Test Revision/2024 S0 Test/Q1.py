def get_ascii_value(username):
    calculation = ord(username[0]) + ord(username[-1])

    return calculation

print(get_ascii_value('Akim161'))
print(get_ascii_value('mgra734'))
print(get_ascii_value('dng004'))
print(get_ascii_value('bcar035'))