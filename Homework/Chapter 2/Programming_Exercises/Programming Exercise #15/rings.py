import turtle as rings

rings.pensize(3)

#First ring
rings.circle(40)
rings.penup()

#Second ring
rings.forward(100)
rings.pendown()
rings.circle(40)
rings.penup()

#Thrid ring
rings.setheading(180)
rings.forward(200)
rings.pendown()
rings.setheading(0)
rings.circle(40)
rings.penup()

#Fourth ring
rings.forward(50)
rings.setheading(270)
rings.forward(40)
rings.setheading(0)
rings.pendown()
rings.circle(40)
rings.penup()

#Fifth ring
rings.forward(100)
rings.pendown()
rings.circle(40)

rings.hideturtle()
