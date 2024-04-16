def binary_search(names_list, target_name):
    left = 0
    right = len(names_list) - 1

    while left <= right:
        mid_index = (left + right) // 2
        print(f'left: {left}, mid: {mid_index}, right: {right}')

        if names_list[mid_index] == target_name:
            return True
        elif names_list[mid_index] < target_name:
            left = mid_index + 1
        else:
            right = mid_index - 1

    return False


my_list = ['Alexandra', 'Auckland', 'Christchurch', 'Dunedin', 'Gisborne', 'Hamilton', 'Invercargill', 'Masterton', 'Queenstown', 'Rotorua', 'Taupo', 'Tauranga', 'Wellington']
print(binary_search(my_list, "Auckland"))