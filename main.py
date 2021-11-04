import turtle 
import random

t = turtle.Turtle()
t.getscreen().bgcolor('black')
t.pensize(4)
t.speed(10)
#concentric circle

colors  = ["orange","yellow","dark orange"]
for i in range(30):
    color = random.choice(colors)
    t.color(color)
    t.circle(10*i)
    t.up()
    t.sety((10*i)*(-1))
    t.down()

t.up()
t.goto(0,0)
t.down()
    
t.goto(0,0)
t.pensize(6)
t.color("magenta")
t.speed(9)
t.left(0)

#spiral petal

t.penup()
size=20
def petal():
  t.pendown()
  for x in range(40):
    t.forward(size)
    t.left(x)
  t.penup() 

left_d = -15

for pet in range(8):
  petal()
  t.goto(0,0)
  t.left(-15)

t.pendown()
t.goto(0,0)

#circular petal 

t.color("cyan")

for x in range(15):
  t.circle(80)
  t.forward(3)
  t.right(25)

t.goto(0,0)

#rhombus petal

t.color("red")

for i in range(10):
  for i in range(2):
    t.forward(50)
    t.right(60)
    t.forward(50)
    t.right(120)
  t.right(36)  
  
  
