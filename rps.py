def rps(ch1,ch2,bit1,bit2):
    p1=int(ch1[bit1])%3
    p2=int(ch2[bit2])%3
    if player1[p1]==player2[p2]: print("draw")
    elif player1[p1]=='rock' and player2[p2]=='paper': print("player1 won")
    elif player1[p1]=='paper' and player2[p2]=='scissors': print("player2 won")
    elif player1[p1]=='scissors' and player2[p2]=='rock': print("player2 won")
    elif player[p1]=='rock' and player2[p2]=='scissors': print("player1 won")
    elif player1[p1]=='paper' and player2[p2]=='rock': print("player2 won")
    elif player1[p1]=='scissors' and player2[p2]=='paper': print("player1 won")



player1={0:'rock',1:'paper',2:'scisssors'}
player2={0:'scissors',1:'rock',2:'paper'}
while True:
    choice1=input("Player1, Enter any number: ")
    choice2=input("Player2, Enter any number: ")
    bit1=int(input("Player1, Enter your secret bit position: "))
    bit2=int(input("Player2, Enter your secret bit position: "))
    rps(choice1,choice2,bit1,bit2)
    ch=input("Do you want to continue?y/n: ")
    if ch=='n': break

