# PALMOS, John Richard (BSCS 1B)
# Midterm Output - Mandala Art 05/12/2022
import turtle

turtle.title("XQZT Quarters by Chadmeister")
setSs = turtle.Screen()
setSs.setup(width = 1280, height = 720)
setSs.bgcolor('black')
turtle.hideturtle()
turtle.speed(0)

turtle.penup()
turtle.goto(0,-285)
turtle.pendown()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(285)
turtle.end_fill()
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

if __name__ == "__main__":

    turtle.width(2.5)
    for k in range(0,int(360/30)):
      turtle.color('black')
      for i in range(0,int(360/60)):
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(81,60,10)
        turtle.circle(81,60,10)
        turtle.left(180)
        turtle.end_fill()
      turtle.left(30)

    for k in range(0,int(360/30)):
      turtle.color('white')
      for i in range(0,int(360/45)):
        turtle.fillcolor('black')
        turtle.begin_fill()
        for j in range(0,int(360/40)):
          turtle.circle(30,15,3)
        turtle.left(180)
        turtle.end_fill()
      turtle.left(30)

    turtle.width(2)
    for k in range(0,int(360/30)):
      for i in range(0,8):
        for j in range(0,9):
          turtle.circle(30,15,3)
        turtle.left(180)
      turtle.left(30)     
    
    for k in range(0,int(360/30)):
      for i in range(0,6):
        turtle.circle(81,60,10)
        turtle.left(180)
      turtle.left(30)
	
turtle.Screen().exitonclick()
