'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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
primeSum = 0

while prime < 2000000:
    if isPrime(prime):
        primeSum += prime
    prime += 1

print(primeSum)
