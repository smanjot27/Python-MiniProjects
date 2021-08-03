import random
def add(temp,ch,picked_movie):
    for i in range(len(picked_movie)):
        if ch==picked_movie[i]:
           temp[i]=ch 
    return temp
def display(temp):
    for i in temp:
        print(i,end=' ')
    print()
    return
def innsert(temp,movie):
        for i in range(len(movie)):
            if movie[i]==' ':
                temp.append(' ')
            else:
                temp.append('_')
        return temp
movies=['phillauri','zindagi na milegi dobara','aashiqui 2','yeh jawaani hai deewani','ranjhaana','prem ratan dhan payo','bhootnath','chennai express','kabir singh','chichhore']
p1name=input("Enter the name of Player 1: ")
p2name=input("Enter the name of player 2: ")
coins1=0
coins2=0
turn=1
while(1):
    if turn %2!=0: 
        guess=0
        print(p1name,"'s turn")
        picked_movie=random.choice(movies)
        movie=list(picked_movie)
        temp=[]
        gues=''
        temp=innsert(temp,movie)
        gues=''.join(temp)
        while gues!=picked_movie:
            display(temp)
            character=input("Guess the character: ")
            if character in picked_movie: 
                temp=add(temp,character,picked_movie)
                gues=''.join(temp)
            else: 
                print(character,'not present in movie name')
                m=int(input("Can't guess? press 1 to see the answer or any number to try guessing"))
                if m==1:
                    print(picked_movie,"is the movie name")
                    guess=2
                    break
            display(temp)           
            num=int(input("Press 1 to guess the movie name or 0 to continue unlocking: "))
            if num==1:
                name=input("Enter movie name: ")
                if name==picked_movie: 
                    coins1+=1
                    guess=1
                    print("Correct Answer.Your score is",coins1)
                    break
                else:
                    print("Wrong Answer! Try Unlocking letter by letter")
        if guess==0:
            coins1+=1
            print("Guessed correctly. Your score is",coins1)
        n=int(input("Enter 1 to continue and 0 to exit: "))
        if n==0:
            print("Thanks for playing\n",p1name,"'s score: ",coins1,"\n",p2name,"'s score:",coins2)
            break
    else:
        guess=0
        print(p2name,"'s turn")
        picked_movie=random.choice(movies)
        movie=list(picked_movie)
        temp=[]
        gues=''
        temp=innsert(temp,movie)
        gues=''.join(temp)
        while gues!=picked_movie:
            display(temp)
            character=input("Guess the character: ")
            if character in movie: 
                temp=add(temp,character,picked_movie)
                gues=''.join(temp)
            else: 
                print(character,'not present in movie name')
                m=int(input("Can't guess? press 1 to see the answer or any number to try guessing"))
                if m==1:
                    print(picked_movie,"is the movie name")
                    guess=2
                    break
            display(temp)
            num=int(input("Press 1 to guess the movie name or 0 to continue unlocking: "))
            if num==1:
                name=input("Enter movie name: ")
                if name==picked_movie: 
                    coins2+=1
                    guess=1
                    print("Correct Answer. Your score is",coins2)
                    break
                else:
                    print("Wrong Answer! Try Unlocking letter by letter")
        if guess==0:
            coins2+=1
            print("Guessed correctly. Your score is",coins2)
        n=int(input("Enter 1 to continue and 0 to exit: "))
        if n==0:
            print("Thanks for playing\n",p1name,"'s score: ",coins1,"\n",p2name,"'s score:",coins2)
            break
    turn+=1
