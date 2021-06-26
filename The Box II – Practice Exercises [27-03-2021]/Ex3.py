import math
ch = int(input('1: to convert form cm to feet and inches \n2: to convert form feet and inches to cm \n'))

def feet_inches(x):
    if x >= 30.48:
        feet = math.floor(x/30.48)
        inches = (x - (feet*30.48))/2.54
        print(f'You are {feet} feet and {inches} inches tall')
    else:
        inches = x/2.54
        print(f'You are  0 feet and {inches} inches tall')

def cm(x,y):
    cm = (30.48*x)+(2.54*y)
    print(f"Your height is {cm} in cm")


if ch ==1:
    cm = float(input('Please enter ur height in cm: '))
    feet_inches(cm)

elif ch ==2:
    print('\nPlease enter ur height in feet and inches for example 5feet and 9inches\n')
    feet = float(input('Feet: '))
    inches = float(input('Inches: '))
    cm(feet, inches)
else:
    print('Sorry Wrong input')