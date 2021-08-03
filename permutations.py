import random
def choose():
    words=['hello','something','pricelist','laptop','computer','kindergarden','lavender','workaholic','python','players']
    return(random.choice(words))
def jumbled(word):
    return("".join(random.sample(word,len(word))))    
def play():
    print("Welcome to the jumbled words game")
    pname1=input("Name of First player: ")
    pname2=input("Name of Recond player: ")
    coins1=0
    coins2=0
    turn=0
    while(1):
        if turn%2==0:
            print(pname1,"'s turn")
            picked=choose()
            print(jumbled(picked))
            word=input("Your Answer: ")
            if picked==word:
                coins1+=1
                print("Correct Answer! Your score is :",coins1)
            else:
                print("Better Luck Next Time!")
            c=int(input("Press 1 to continue and 0 to quit:"))
            if c==0:
               print("Thanks for playing")
               break
        else:
            print(pname2,"'s turn")
            picked=choose()
            print(jumbled(picked))
            word=input("Your Answer: ")
            if picked==word:
                coins2+=1
                print("Correct Answer! Your score is :",coins2)
            else:
                print("Better Luck Next Time!")
            c=int(input("Press 1 to continue and 0 to quit:"))
            if c==0: 
               print("Thanks for playing")
               break
        turn+=1
play()
