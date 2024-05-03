def create_dictionary(usernames_list):
    username_dict = {}
    for username in usernames_list:
        letter = username[0]
        if letter in username_dict:
            username_dict[letter].append(username)
        else:
            username_dict[letter] = [username]

    return username_dict

data = create_dictionary(['mgra734', 'dng004', 'bcar035', 'myu134', 'dkim104'])
for key in sorted(data ):
    print(key, sorted(data[key]))