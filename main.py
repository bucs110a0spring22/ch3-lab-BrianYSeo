import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo.forward(random.randrange(1,100))
leonardo.forward(random.randrange(1,100))
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

for i in range(10):
  leonardo.forward(random.randrange(1,10))
  michelangelo.forward(random.randrange(1,10))
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
# Part B - complete part B here
leonardo.down()
sides=[3, 4, 6, 9, 12]
for item in sides:
  for i in range(item):
   leonardo.forward(25)
   leonardo.right(360/item)
  leonardo.clear()

window.exitonclick()
