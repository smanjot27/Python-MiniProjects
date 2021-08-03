n=int(input())
array=list(map(int,input().split()))
for i in range(n):
    if i>=len(array): break
    print("length of array",len(array))
    print("i=",i)
    print("element=",array[i])
    c=array.count(array[i])
    if c>1:
        print(array[i],"found",c,"times")
        flag=1
        for j in range(i+1,len(array)):
            print("j=",j)
            if array[j]==array[i]:
                print("another same element found",array[j])
                print("length of array:",len(array))
                for k in range(j,len(array)-1):
                    print("k=",k)
                    array[k]=array[k+1]
                flag+=1
                array.pop()
                print(array)
                if flag==c:
                    print("removed",array[i],c,"times")
                    break
for i in array:
    print(i,end=" ")
