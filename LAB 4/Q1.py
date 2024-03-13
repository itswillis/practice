def is_licence_eligible(number):

    # try to convert into int 
    try:
        number = int(number)
    except ValueError:
        return (False, 'ERROR: The value is invalid!') 
    except TypeError:
        return (False, 'ERROR: The type is incorrect!') 
    else: 
        if number >= 32 and number <= 35: 
            return (True, number)
        else:
            return (False, number)


data = is_licence_eligible('32')
print(data)
print(type(data))

print(is_licence_eligible(-1))
print(is_licence_eligible('28'))
print(is_licence_eligible([18, 12]))
print(is_licence_eligible('two'))