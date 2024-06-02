# import colorgram
#
# color_list = colorgram.extract("hirst.jpg", 2 ** 32)
# color_palette = []
#
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_palette.append(new_color)

import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

color_palette = [(226, 231, 236), (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53), (134, 42, 38), (47, 66, 61), (0, 122, 125)]

tim = Turtle()
tim.up()
tim.teleport(-365.00000000000006, -359.99999999999994)
tim.speed("fastest")

for y in range(10):
    x_position = tim.xcor()
    y_position = tim.ycor()
    for x in range(10):
        random_color = random.choice(color_palette)
        tim.dot(40, random_color)
        tim.forward(80)
    tim.teleport(x_position, y_position + 80)

screen = Screen()
screen.exitonclick()
