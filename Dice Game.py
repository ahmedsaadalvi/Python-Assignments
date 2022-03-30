from random import randint
r = randint(1, 6)
n = 3


for i in range(n):
    guess = int(input('Guess The Number On Dice(Between 1 and 6):'))
    if guess == r:
        print('The Number is ', r)
        print('Good Guess - Congratulations!')
        break
    else:
        print('Bad Guess - Try Again!')
        n = n - 1
        if n == 0:
            print('Sorry Your Chances Are Over!')
            break
        print('You Have %d More Chances' % (n))
print('\nWell Played')