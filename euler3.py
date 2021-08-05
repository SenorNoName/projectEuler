'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

num = 600851475143
counter = 2

while counter <= math.sqrt(num):
    if num % counter == 0:
        num /= counter
        counter -= 1
    if num >= 2:
        print(num)
    counter += 1
