#import dependencies
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle X-Mas")

pen_heart = turtle.Turtle()
pen_heart.speed(12)
pen_heart.pensize(1)
pen_heart.color("red")

def draw_heart(pen_heart):
    pen_heart.penup()
    for size in range(50):
        pen_heart.goto(0, -100 -size *2.5)
        pen_heart.pendown()
        pen_heart.setheading(140)
        pen_heart.left(50)
        pen_heart.forward(50 + size * 5)
        pen_heart.circle(-25 -size * 2.5, 199)
        pen_heart.circle(-25 - size * 2.5, 199)
        pen_heart.forward(50 + size * 5.05)
        pen_heart.penup()
        
    draw_heart(pen_heart)

pen_heart.hideturtle()
turtle.done()