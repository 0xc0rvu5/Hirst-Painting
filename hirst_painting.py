import turtle as t
import random


#initialize global variables
COLOR_LIST = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), 
              (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), 
              (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), 
              (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), 
              (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]
JAMMY = t.Turtle()
NUMBER_OF_DOTS = 10
X = -250
Y = -200


#customization of JAMMY and positioning JAMMY at start locaiton
JAMMY.shape('turtle')
t.colormode(255)
JAMMY.penup()
JAMMY.goto(X, Y)


def move_horizontal():
    '''Directions in which JAMMY the turtle will move. Also changing the color of each dot every x distance.'''
    for i in range(0, NUMBER_OF_DOTS):
        JAMMY.dot(20, random.choice(COLOR_LIST))
        JAMMY.penup()
        JAMMY.forward(50)


#initialize program to paint dots with turtle 10x10
try:
    move_horizontal()
    while Y % 50 == 0 and Y < 201:
        Y += 50
        JAMMY.goto(X, Y)
        move_horizontal()
    screen = t.Screen()
    screen.exitonclick()
    
except KeyboardInterrupt:
    print('\nSee you later.')