def swap_space_with_target(string, target_letter):
    placeholder = '~'
    # take the old target letter out and replace with placeholder
    string = string.replace(target_letter, placeholder)

    # replace the empty with the target letter
    string = string.replace(' ', target_letter)

    # replace the placeholder with empty string to return to previous state
    string = string.replace(placeholder, ' ')

    return string

print(swap_space_with_target("abcde fgh", 'b'))
print(swap_space_with_target("abcde fgh", 'g'))
print(swap_space_with_target("abcde fgh", 'h'))
print(swap_space_with_target("abcde fgh", 'a'))