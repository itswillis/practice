class Primes:

    def __init__(self, number_of_primes=5):
        self.number_of_primes = number_of_primes

    def __iter__(self):
        return PrimesIterator(self.number_of_primes)

class PrimesIterator:

    '''
    A class to create an iterable sequence of prime numbers:
        - number_of_primes is the total number of prime numbers to generate

    The __iter__() method returns a PrimesIterator object to generate prime numbers. 

    Authour: William Tang
    '''

    def __init__(self, number_of_primes =5):
        self.number_of_primes = number_of_primes
        self.count = 1
        self.current = 2
    
    def __next__(self):
        if self.count > self.number_of_primes:
            raise StopIteration
        else:
            while True: # loop to find the next prime number
                is_prime = True # assume current number is a prime
                i = 2 # start checking from the smallest prime number
                while i <= int(self.current / 2):
                    if self.current % i == 0: 
                        is_prime = False
                        self.current += 1
                        i = 2 # reset i to check the number from beginning 
                    else:
                        i += 1
                if is_prime: # if not found, the current number is a prime
                    prime = self.current
                    self.current += 1
                    self.count += 1
                    return prime
                
sequence = Primes(10)
for prime in sequence:
    print(prime, end=" ")
print()
