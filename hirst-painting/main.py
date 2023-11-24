import turtle
import random

turtle.colormode(255)
pen = turtle.Turtle()
pen.speed("fastest")
pen.penup()
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

pen.setheading(255)
pen.forward(250)
pen.setheading(0)


def pendot():
    for _ in range(10):
        for _ in range(10):
            pen.dot(20, random.choice(color_list))
            pen.forward(50)

        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)


pendot()

screen = turtle.Screen()
screen.exitonclick()
