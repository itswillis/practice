def foo(number):
    word = str(number % 4)
    if number % 4 == 0:
        return word
    else:
        return foo(number // 4) + word
    
print(foo(13))