def display(array):
    for i in range(3):
        for j in range(3):
            print(array[i][j],end=' ')
        print()
    print()
def place(row,col,array,symbol):
    if array[row][col]=='_':
        array[row][col]=symbol
    else:
        print('Choose a valid position')
def check(array,symbol):
    val=False
    for i in range(3):
        if array[i][0]==array[i][1]==array[i][2]==symbol:
            val=True
        if array [0][i]==array[1][i]==array[2][i]==symbol:
            val=True
    if (array[0][0]==array[1][1]==array[2][2]==symbol) or (array[2][0]==array[1][1]==array[0][2]==symbol):
            val=True
    return val
ttt=[['_' for i in range(3)] for j in range(3)]
player1=input("Player 1, Enter your name: ")
player2=input("Player 2, Enter your name: ")
print("Symbol for ",player1,": O")
print("Symbol for",player2,": X")
turn=0
flag=0
while turn<10:
    if turn%2==0:
        print(player1,"'s turn")
        row,col=input("Enter the row and column in which you want to place your symbol:").split()
        place(int(row),int(col),ttt,'O')
        display(ttt)
        if check(ttt,'O')==True:
            print(player1,"Won")
            flag=1
            break
    else: 
        print(player2,"'s turn")
        row,col=input("Enter the row and column in which you want to place your symbol:").split()
        place(int(row),int(col),ttt,'X')
        display(ttt)
        if check(ttt,'X')==True:
            print(player2,"Won")
            flag=1
            break
    turn+=1
if flag==0: print("Draw")        
