import turtle as t
import random
tom=t.Turtle()
tom.shape("turtle")
tom.pensize(10)
tom.speed("fastest")
num=int(input("Number of shapes you want:"))
#colours=['red','green','blue','yellow','purple','green yellow','deep pink','medium slate blue','cadet blue']
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

def shaping(num_sides):
    angle=360//num_sides
    for i in range(num_sides):
        tom.forward(100)
        tom.right(angle)


def shaping1(num_sides):
    angle=360//num_sides
    for i in range(num_sides):
        tom.forward(25)
        tom.penup()
        tom.forward(25)
        tom.pendown()
        tom.forward(25)
        tom.penup()
        tom.forward(25)
        tom.pendown()
        tom.left(angle)
for i in range(3,num+1):
    tom.color(random_color())
    shaping(i)
for i in range(3,num+1):
    tom.color(random_color())
    shaping1(i)
screen=t.Screen()
screen.exitonclick()