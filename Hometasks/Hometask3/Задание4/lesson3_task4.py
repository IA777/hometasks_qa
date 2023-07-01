# from turtle import *

# my_turtle = Turtle()
# my_turtle.speed(-10)
# my_turtle.screen.setup(800, 800)

# # Нарисовать квадрат
# def draw_rect(t):
#     for x in range(0, 4):
#         t.right(90)
#         t.forward(100)

# # Рисует квадраты в цикле
# for x in range(0, 360):
#     draw_rect(my_turtle)
#     my_turtle.right(1)

# # Необходимо, чтобы окно не закрывалось само, а только по клику
# my_turtle.screen.exitonclick()
# my_turtle.screen.mainloop()


# from turtle import *
# t = Turtle()
# t.screen.setup(800, 800)
# t.fd(200)
# t.screen.exitonclick()
# t.screen.mainloop()

# from turtle import *
# t = Turtle()
# t.screen.setup(800, 800)
# for i in range(20):
#     t.fd(8)
#     t.up()
#     t.fd(8)
#     t.down()
# t.screen.exitonclick()
# t.screen.mainloop(

from turtle import *

my_cat = Turtle()
my_cat.screen.setup(800, 800)

my_cat.circle(100, 360)
my_cat.goto(100, 574)


my_cat.screen.exitonclick()
my_cat.screen.mainloop()
