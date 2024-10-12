import turtle as bot

bot.penup()
bot.goto(250,-250)
bot.speed(1000)

for i in range(1, 101):
    bot.pendown()
    bot.setheading(90)
    bot.forward(i * 5)
    bot.setheading(180)
    bot.forward(i * 5)
    bot.setheading(270)
    bot.forward(i * 5)
    bot.setheading(0)
    bot.forward(i * 5)
    
bot.hideturtle()