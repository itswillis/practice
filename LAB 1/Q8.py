def get_smallest_prime_factor(number):
    if number <= 1:
        return -1
    
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    for i in range(2, 20):
        if is_prime(i) and number % i == 0:
            return i
    return -1

def create_dictionary(numbers):
    a_dict = {}
    for num in numbers: 
        smallest_prime = get_smallest_prime_factor(num)
        if smallest_prime != -1:
            if smallest_prime not in a_dict:
                a_dict[smallest_prime] = []
        a_dict[smallest_prime].append(num)
    return a_dict


numbers_dictionary = create_dictionary([76, 237, 20, 560, 924])
for key in sorted(numbers_dictionary.keys()):
    print(key, numbers_dictionary[key])
values = [76, 237, 20, 560, 924, 351, 561, 133, 102, 147, 415, 126, 121, 780, 17, 1273, 64, 12]
numbers_dictionary = create_dictionary(values)
for key in sorted(numbers_dictionary.keys()):
    print(key, numbers_dictionary[key])