from turtle import *

w = Screen()
w.setup(600, 800)
w.bgcolor('black')
w.title('Сердечко')

t = Turtle()
t.color('red', 'pink')
t.width(5)
t.left(140)
t.begin_fill()
t.forward(220)
t.circle(-110, 200)
t.seth(60)
t.circle(-110, 200)
t.forward(220)
t.end_fill()  # кінцева заливка
t.hideturtle()  # прибрати черепаху
exitonclick()  # затримка екрана
