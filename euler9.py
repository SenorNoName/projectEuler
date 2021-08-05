'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math

'''
a^2 = c^2 - b^2
a = math.sqrt(c^2 - b^2)
math.sqrt(c^2 - b^2) + b + c = 1000
'''

for b in range(1000):
    for c in range(1000):
        if c**2 - b**2 > 0 and math.sqrt(c**2 - b**2) + b + c == 1000 and b != 0 and c != 0:
            print(f'a:{math.sqrt(c**2 - b**2)}, b:{b}, c:{c}')
            print(f'Product: {math.sqrt(c**2 - b**2) * b * c}')
