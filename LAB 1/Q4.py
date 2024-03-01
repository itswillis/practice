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

print(get_smallest_prime_factor(55))
print(get_smallest_prime_factor(42))
print(get_smallest_prime_factor(1273))
print(get_smallest_prime_factor(46))
print(get_smallest_prime_factor(667))