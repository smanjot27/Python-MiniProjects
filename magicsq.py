def magic(n):
    sq=[]
    sq=[[0 for i in range(n)] for j in range(n)]
    printt(sq,n)
    sq[n//2][n-1]=1
    i=2
    row=n//2
    col=n-1
    while(i<=n**2):
         row-=1
         col+=1
         if row==-1 and col==n:
             row=0
             col=n-2
         elif row==-1: row=n-1
         elif col==n: col=0
         if sq[row][col]!=0:
            row+=1
            col-=2
         sq[row][col]=i
         i+=1
    printt(sq,n)
def printt(sq,n):
    for i in range(n):
        for j in range(n):
            print(sq[i][j],end=" ")
        print()
    print()


magic(int(input()))

