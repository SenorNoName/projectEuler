'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

num1 = 100
num2 = 100
productArr = []
palindromeArr = []


def palindromeCheck(int):
    int = str(int)
    rev = ''.join(reversed(int))
    if int == rev:
        return True
    return False

while num1 < 1000 and num2 < 1000:
    for i in range(900):
        num1 = 100
        for num in range(900):
            productArr.append(num1 * num2)
            num1 += 1
        num2 += 1

for i in productArr:
    if palindromeCheck(i) == True:
        palindromeArr.append(int(i))

print(max(palindromeArr))
