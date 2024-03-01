def is_palindrome(word):
    # convert these strings into list
    a_list = []
    reversed_list = []
    for letters in word: 
        a_list.append(letters)
    
    for i in reversed(a_list):
        reversed_list.append(i)
    
    if a_list == reversed_list:
        return True
    else:
        return False

print(is_palindrome('radar'))
print(is_palindrome('python'))
print(is_palindrome('madam'))
print(is_palindrome('computer'))