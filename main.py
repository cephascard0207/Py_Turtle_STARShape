#Py_Turtle_Square
#Created by Cephas Cardozo

#imports
import turtle

#global_variables
star = turtle.Turtle()

#color_coordinates
star.color("blue", "white")

#turtle_speed
star.speed(78)

#turtle_pensize
star.pensize(0.5)

#begin_command_execution
#begin & end_fill can be used to fill color inside the shape
star.begin_fill()

for i in range(90):
  star.forward(100)

  #change the value of degrees below to get different star shapes
  star.left(190)


star.end_fill()

#end_execution
turtle.done()