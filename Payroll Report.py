name = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL']
hours = [23, 57, 54, 12, 98, 45, 34, 86, 46, 23, 68, 47]
n = len(name)
rate = 12.50
total = 0
sum = 0


print('\n              PAYROLL REPORT   \n')
print('\n No.   Employee       Hours        Salary(RM)\n')


for i in range(n):
    if hours[i] >= 0 and hours[i] <= 40:
        wage = hours[i] * rate
        sum = wage + sum
    elif hours[i] > 40 and hours[i] <= 60:
        wage = 40 * rate + (hours[i] - 40) * rate * 1.5
        sum = wage + sum
    elif hours[i] > 60:
        wage = 40 * rate + 20 * rate * 1.5 + (hours[i] - 60) * rate * 2.0
        sum = wage + sum
        
        
    print(' {:2d}       {:3s}       {:3f}      {:4f}' .format (i+1, name[i], hours[i], wage))


print('\nTotal Salary = RM', sum)