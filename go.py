# This program calculates the area of a rectangle or a circle

import math

# Define a function to calculate the area of a rectangle
def rectangle_area(length, width):
    area = length * width
    return area

# Define a function to calculate the area of a circle
def circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

# Prompt the user to choose which shape they want to calculate the area for
shape = input("Which shape do you want to calculate the area for? Enter 'rectangle' or 'circle': ")

# Call the appropriate function based on the user's input
if shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print("The area of the rectangle is", area)
elif shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print("The area of the circle is", area)
else:
    print("Invalid input. Please enter 'rectangle' or 'circle'.")
