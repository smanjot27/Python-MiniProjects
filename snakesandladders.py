def checkladders(p):
    if p==4: p=25
    elif p==8: p=29
    elif p==13: p=46
    elif p==33: p=49
    elif p==42: p=63
    elif p==50: p=69
    elif p==62: p=81
    elif p==67: p=86
    elif p==74: p=92
    return p
def checksnakes(p):
    if p==27: p=5
    elif p==40: p=3
    elif p==43: p=18
    elif p==54: p=31
    elif p==66: p=45
    elif p==76: p=58
    elif p==89: p=53
    elif p==95: p=84
    elif p==99: p=41
    return p
from PIL import Image
import random
img=Image.open("Snakes-and-Ladders-Life.png")
img.show()
player1=input("Enter Player 1 name:")
player2=input("Enter Player 2 name:")
points1=0
points2=0
turn=0
c=1
while c==1 and not (points1>=100 or points2>=100):
    if turn%2==0:
        print(player1,"'s turn")
        num=random.randint(1,6)
        print("Dice Number: ",num)
        points1+=num
        points1=checkladders(points1)
        points1=checksnakes(points1)
        if points1>100: 
            print("score a perfect number to win")
            points1-=num
        print("your score is",points1)
        c=int(input("Enter 1 to continue and 0 to quit:"))
        if c==0: break
    else:
        print(player2,"'s turn")
        num=random.randint(1,6)
        print("Dice number:",num) 
        points2+=num
        points2=checkladders(points2)
        points2=checksnakes(points2)
        if points2>100: 
            print("score a perfect number to win")
            points2-=num
        print("your score is ",points2)
        c=int(input("Enter 1 to continue and 0 to quit:"))
        if c==0: break
    turn+=1
if points1>=100: print(player1," Won")
elif points2>=100: print(player2,"Won")
else: print("Draw")
