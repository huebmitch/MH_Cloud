'''
Created on Mar 25, 2016

@author: usreei
'''

import turtle

ninja = turtle.Turtle()

ninja.speed(0)

for i in range(180):
    ninja.forward(100)
    ninja.right(45)
    ninja.forward(30)
    ninja.left(70)
    ninja.forward(50)
    ninja.right(45)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()
