import random
li=[0]*3
i=random.randint(0,2)
li[i]="Chocolate"
for j in range(0,3):
    if j!=i: 
        li[j]="nothing"
choice=int(input("Enter your choice 0 to 2:" ))
d=random.randint(0,2)
while d==i or d==choice:
    d=random.randint(0,2)
print("position",d,"has",li[d])
ch=input("Would you like to swap?y/n: ")
if ch=='y':
    if choice==i:
        print("you lost")
    else:
        print("you won a chocolate")
else:
    if choice==i:
        print("you won a chocolate")
    else:
        print("you lost")


