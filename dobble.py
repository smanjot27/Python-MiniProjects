import random
import string
while(1):
    symbols=list(string.ascii_letters)
    symbol=random.choice(symbols)
    symbols.remove(symbol)
    list1=[0]*5
    list2=[0]*5
    pos1=random.randint(0,4)
    pos2=random.randint(0,4)
    if pos1==pos2:
        list1[pos2]=symbol
        list2[pos1]=symbol
    else:
        list1[pos1]=random.choice(symbols)
        symbols.remove(list1[pos1])
        list1[pos2]=symbol
        list2[pos1]=symbol
        list2[pos2]=random.choice(symbols)
        symbols.remove(list2[pos2])
    i=0
    while i<5:
        if i!=pos1 and i!=pos2:
            list1[i]=random.choice(symbols)
            symbols.remove(list1[i])
            list2[i]=random.choice(symbols)
            symbols.remove(list2[i])
        i+=1
    print(list1)
    print(list2)
    c=input("spot the similarity: ")
    if c==symbol:
        print("correct Answer")
    else:
        print("try again :(")
    con=int(input("Press 1 to continue and 0 to quit: "))
    if con==0: break
