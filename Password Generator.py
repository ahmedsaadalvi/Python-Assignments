import random

s1 = 'abcdefghijkl'
s2 = 'ABCDEFGHIJKL'
s3 = '0987654'
s4 = '@$#?%&*)'
s = s1 + s2 + s3 + s4

print ('\nPasswords =\n')

for i in range(7):
    password = ''
    for j in range(7):
        password = password + random.choice(s)
    print ('Password', i+1, ': ', password)