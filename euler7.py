'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primeCount = 0
prime = 1

while primeCount < 10001:
    prime += 1
    if isPrime(prime):
        primeCount += 1

print(prime)
