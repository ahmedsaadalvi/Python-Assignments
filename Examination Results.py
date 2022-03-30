name = ['AAA','BBB','CCC','DDD', 'EEE', 'FFF', 'GGG', 'HHH', 'III']
mark = [88, 45, 60, 63, 92, 64, 71, 54, 73]
n = len(name)
sum = 0


print('\n         EXAMINATION RESULTS\n')
print('         PYTHON PROGRAMMING\n')
print('No.    Student Name    Mark    Grade')


for i in range(n):
    sum = sum + mark[i]
    if mark[i] >= 0 and mark[i] <= 49:
        grade = 'F'
    elif mark[i] >= 50 and mark[i] <= 64:
        grade = 'C'
    elif mark[i] >= 65 and mark[i] <= 79:
        grade = 'B'
    elif mark[i] >= 80 and mark[i] <= 100:
        grade = 'A'
    else:
        grade = 'Invalid Mark'
        
        
    print('{:2d}          {:8s}    {:2d}       {:7s}' .format (i+1, name[i], mark[i], grade))


average = sum/n
minimum = min(mark)
maximum = max(mark)


print('\nAverage Mark =', round(average, 0))
print('Minimum Mark =', minimum)
print('Maximum Mark=', maximum)