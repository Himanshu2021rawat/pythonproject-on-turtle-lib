import turtle

s = turtle.Turtle()
s.getscreen().bgcolor("#994444")

s.penup()
s.goto(-200,100)
s.pendown()

# def star():
# for i in range(5):
#         s.forward(100)
#         s.left(216)
# star()

def star(turtle, size):
    if size <=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
star(s,360)

turtle.end_fill()


turtle.done()