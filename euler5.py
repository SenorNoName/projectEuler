'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

num = 0
bool = True

def divide():
    for n in range(1, 20):
        if num % n == 0:
            continue
        else:
            print(f'{num} failed')
            break
    bool = False

while bool == True:
    divide()
    num += 1

print(num)
