import math

# Main area calculator that obtains shape of interest and calls other functions.
def areaCalculator():
    # Available shape options.
    shapes = ["circle", "rectangle", "square", "triangle"]
    userShape = ""
    doesNotHaveValidShape = True

    # Introduction message.
    print("I can calculate the area of a shape for you.")

    # while and try/except to obtain a valid shape choice.
    while doesNotHaveValidShape:
        userShape = input("\nWhat shape do you want to calculate the area for? ").lower()

        if userShape in shapes:
            doesNotHaveValidShape = False
        else:
            print(f"\nOops. {userShape} is not a shape the calculator can find the area for.")
            print("Consider finding the area of a circle, rectangle, square, or triangle.")
    
    # Control flow to collect valid measurements using while loops and try/except. Measurements are then
    # Measurements are then plugged into the appropiate area formula.
    if userShape == "circle":
        radius = 0.0
        doesNotHaveValidRadius = True

        while doesNotHaveValidRadius:
            try:
                radius = float(input("\nWhat is the radius of the circle? "))

                doesNotHaveValidRadius = False
            except: 
                print("\nOops. Please enter a valid numeric measurement (integer or float).")

        print(f"\nThe area of the circle is {circle(radius)}")

    elif userShape == "rectangle" or userShape == "square":
        length = 0.0
        width = 0.0
        doesNotHaveValidLengthAndWidth = True

        while doesNotHaveValidLengthAndWidth:
            try:
                length = float(input("\nWhat is the length of the rectanle or square? "))
                width = float(input("What is the width of the rectangle or square? "))

                doesNotHaveValidLengthAndWidth = False
            except:
                print("\nOops. Please enter a valid numeric measurement (integer or float).")

        print(f"\nThe area of the square/rectangle is {square(length, width)}")

    else:
        base = 0.0
        height = 0.0
        doesNotHaveValidBaseAndHeight = True

        while doesNotHaveValidBaseAndHeight:
            try:
                base = float(input("\nWhat is the base of the triangle? "))
                height = float(input("What is the height of the triangle? "))

                doesNotHaveValidBaseAndHeight = False
            except:
                print("\nOops. Please enter a valid numeric measurement (integer or float).")

        print(f"\nThe area of the triangle is {triangle(base, height)}")

# Area formulas separated into functions.
def circle(radius):
    return math.pi * pow(radius, 2)

def square(length, width):
    return length * width

def triangle(base, height):
    return (base * height) / 2

areaCalculator()



# print(circle(5)) # 78.53982
# print(circle(13.5)) # 572.55526
# print(circle(98.9994)) # 30790.37638
# print(circle(0.5403)) # 0.91711

# print(square(12, 12)) # 144
# print(square(34, 55)) # 1870
# print(square(0.345, 78)) # 26.91

# print(triangle(6, 18)) # 54
# print(triangle(3.45, 6.93)) # 11.95425
# print(triangle(0.045, 4)) # 0.09