n=int(input())
array=list(map(int,input().split()))
for i in range(n):
    if i>=len(array): break
    c=array.count(array[i])
    if c>1:
        flag=1
        j=i+1
        while(j<len(array)):
                if array[j]==array[i]:
                    for k in range(j,len(array)-1):
                        array[k]=array[k+1]
                    flag+=1
                    array.pop() 
                    if flag==c: break
                else:  j+=1
for i in array:
    print(i,end=" ")
