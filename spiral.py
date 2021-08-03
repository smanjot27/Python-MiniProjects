num=int(input("Enter any number"))
count=1
a=[[0 for i in range(num)]for j in range(num)]
for i in range(num):
    for j in range(num):
        a[i][j]=count
        count+=1

row=0
col=num-1
r=0
c=num
while r<=num//2 and c>=num//2:
    for i in range(r,c):
        print(a[row][i],end=' ' )
    row+=1
    for i in range(row,c):
        print(a[i][col],end=' ')
    for i in range(col-1,r-1,-1):
        print(a[col][i],end=' ')
    col-=1
    for i in range(col,row-1,-1):
        print(a[i][row-1],end=' ')
    r+=1
    c-=1
