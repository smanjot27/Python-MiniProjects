import random
def evolve(x):
    index=random.randint(0,len(x))
    p=random.randint(1,100)
    if p==1:
        if x[index]==0:
            x[index]=1
        else:
            x[index]=0
    return(x)

with open("data.txt",'r+') as myfile:
    x=myfile.read()
    x=list(x)
    print(x)
    for i in range(len(x)):
        evolve(x)
    print(x)
