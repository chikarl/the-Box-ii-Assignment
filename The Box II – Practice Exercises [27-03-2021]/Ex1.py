print('Please enter ur height in feet and inches for example 5feet and 9inches')
feet = float(input('Feet: '))
inches = float(input('Inches: '))
def cm(x,y):
    cm = (30.48*feet)+(2.54*inches)
    return cm

print(f"Your height is {cm(feet, inches)} in cm")