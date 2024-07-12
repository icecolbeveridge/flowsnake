import turtle

import random

turtle.up()
turtle.setpos(100,401)
turtle.down()
turtle.speed(0)
DIST = 15
ITERATIONS = 4


def iterate(prev: str) -> str:
    next = prev.replace("A", "a-b--b+a++aa+b-")
    next = next.replace("B", "+a-bb--b-a++a+b")
    return next.upper()

def draw(x: str) -> None:
    while x:
        y, x = x[0], x[1:]
        if y == "A" or y == "B": 
            turtle.forward(DIST)
        if y == "+":
            turtle.left(60)
        if y == "-":
            turtle.right(60)
    
x = "A"
for _ in range(ITERATIONS):
    x = iterate(x)

draw(x)
input()