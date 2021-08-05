'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

ones = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
teens = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
tens = 60 + 60 + 50 + 50 + 50 + 70 + 60 + 60 + ones*8
hundreds = 63 + ones*109 + teens*9 + tens*9 + 8910
thousand = 11

print(ones + teens + tens + hundreds + thousand)
