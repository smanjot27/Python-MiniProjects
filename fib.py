def fib(elem,li):
    j=2
    while(j<=elem):
        if j<len(li): 
            target=li[j]
        else:
            target=li[j-1]+li[j-2]
            li.append(target)
        j+=1
    return(target)
m,n=map(int,input().split())
li=[0,1]
s=0
for i in range(m,n+1):
    print(li)
    s+=fib(i,li)
    print("sum=",s)
s=list(str(s))
print(int(s[len(s)-1]))


