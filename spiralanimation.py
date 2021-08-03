import turtle
import random
pen=turtle.Turtle()
turtle.bgcolor('Black')
pen.penup()
pen.setpos(-600,600)
num=int(input("Enter width distance"))
dotd=num**2
colors=['red','white','yellow','green','blue','cyan','pink','orange']
row=0
col=num-1
r=0
c=num
while r<=num//2 and c>=num//2:
    pen.color(random.choice(colors))
    for i in range(r,c):
        pen.dot()
        pen.forward(dotd)
    pen.right(90)
    row+=1
    for i in range(row,c):
        pen.dot()
        pen.forward(dotd)
    pen.right(90)
    for i in range(col-1,r-1,-1):
        pen.dot()
        pen.forward(dotd)
    pen.right(90)     
    col-=1
    for i in range(col,row-1,-1):
        pen.dot()
        pen.forward(dotd)
    pen.right(90)
    r+=1
    c-=1
