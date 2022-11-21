# ex5
# import 사용 예제2
# for 문 사용 예제

import turtle

myT = turtle.Turtle()
myT.shape("classic")

for i in range(0, 100) :
    myT.forward(200)
    myT.right(90)

turtle.done()