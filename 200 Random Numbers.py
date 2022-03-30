from random import randint
n = 200
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
even = 0
divide5 = 0


print('\n                                 200 RANDOM NUMBERS\n')


for i in range(n):
    r = randint(1000, 9999)
    print(r, end = ' ')
    if r >= 1000 and r <= 2499:
        sum1 = sum1 + 1
    if r >= 2500 and r <= 4999:
        sum2 = sum2 + 1
    if r >= 5000 and r <= 7499:
        sum3 = sum3 + 1
    if r >= 7500 and r <= 9999:
        sum4 = sum4 + 1
    if r % 2 == 0:
        even = even + 1
    if r % 5 == 0:
        divide5 = divide5 + 1
        
        
print('\n\nTOTAL NUMBERS IN RANGE :\n')
print('1000 - 2499 =', sum1)
print('2500 - 4999 =', sum2)
print('5000 - 7499 =', sum3)
print('7500 - 9999 =', sum4)


print('\nTOTAL NUMBERS :')
print('\nEven Numbers   =', even)
print('Divisible by 5 =', divide5)