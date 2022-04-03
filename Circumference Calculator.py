def circle(radius):
    area = 3.1412*radius*radius
    circum = 2*3.1412*radius
    return area, circum


radius = [5.2,7.0,12.5,7.7,23.5]
n = len(radius)
print('\n    Circumference Calculator')
print('\nNo        Area       Circumference')
for i in range(n):
    area, circum = circle(radius[i])
    
    print('{:2}   {:11} {:14}' .format(i+1, round(area,4), round(circum,4)))