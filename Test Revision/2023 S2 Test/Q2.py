'''def get_words(usernames_list):
    results_list = []
    for username in usernames_list:
        username_str = ''
        for letters in username:
            if letters.isalpha():
                username_str += letters
        
        results_list.append(username_str)
    return results_list'''

def extract_letters(username):
    ''' Extracts and returns only alphabetical characters from the username. '''
    return ''.join(char for char in username if char.isalpha())

def get_words(username_list):
    ''' Uses extract_letters to each username in the list and returns the list. '''
    return ([extract_letters(username) for username in username_list])

print(get_words(['mgra734', 'dng004', 'bcar035']))
print(get_words(['myu134', 'dkim104']))