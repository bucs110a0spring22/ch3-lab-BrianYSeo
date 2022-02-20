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
for i in range(3):
  leonardo.forward(25)
  leonardo.right(120)
leonardo.clear()

leonardo.down()
for i in range(4):
  leonardo.forward(25)
  leonardo.right(90)
leonardo.clear()

leonardo.down()
for i in range(6):
  leonardo.forward(25)
  leonardo.right(60)
leonardo.clear()

leonardo.down()
for i in range(9):
  leonardo.forward(25)
  leonardo.right(40)
leonardo.clear()

leonardo.down()
for i in range(12):
  leonardo.forward(25)
  leonardo.right(30)
leonardo.clear()

window.exitonclick()
