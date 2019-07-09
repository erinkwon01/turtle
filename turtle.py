import turtle

turtle.speed(3)
from turtle import *
color('blue', 'green')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
