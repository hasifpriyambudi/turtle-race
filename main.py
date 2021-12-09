import turtle
import random

screen = turtle.Screen()
x = 500
y = 400
screen.setup(x, y)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
allTurtle = []
y2 = -100

for i in range(len(colors)):
    newTurtle = turtle.Turtle(shape="turtle")
    newTurtle.color(colors[i])
    newTurtle.penup()
    newTurtle.goto(-150, y2)
    y2 += 40
    allTurtle.append(newTurtle)

betCondition = True
while betCondition:
    bet = screen.textinput("Make your bet", "Which turtle will win the race? enter a color: ").lower()
    if bet in colors:
        betCondition = False

condition = True
while condition:
    turtle = random.choice(allTurtle)
    if turtle.xcor() >= (x/2)-20:
        condition = False
        winning = turtle.pencolor()
        if winning == bet:
            print(f"You' ve won! The {winning} turtle is the winner!")
        else:
            print(f"You've lost! The {winning} turtle is the winner!")

    move = random.randint(0, 10)
    turtle.forward(move)

screen.exitonclick()
