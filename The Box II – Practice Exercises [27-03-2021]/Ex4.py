height = float(input('Please enter ur heigth in cm: '))
bmi = 21.7
def idw(h):
    h = 175/100
    idw = bmi*(h**2)
    print(f"Your ideal weight is {idw}")

idw(height)