import turtle as squirtle

#When using turtle, no need for "penup" after
#"write" command (does it itself)

squirtle.forward(200)
squirtle.right(180)
squirtle.forward(400)
squirtle.right(180)
squirtle.forward(200)

squirtle.right(90)
squirtle.forward(200)
squirtle.right(180)
squirtle.forward(400)

squirtle.penup()
squirtle.goto(50,0)
squirtle.pendown()
squirtle.circle(50)

squirtle.penup()
squirtle.goto(0,200)
squirtle.write("North")

squirtle.goto(215,0)
squirtle.write("East")

squirtle.goto(0,-215)
squirtle.write("South")

squirtle.goto(-215,0)
squirtle.write("West")

squirtle.hideturtle()
input('press any key to exit')