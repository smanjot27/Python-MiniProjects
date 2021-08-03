def sortt(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
def search(a,x):
    l=0
    high=len(a)-1
    flag=0
    count=0
    while l<=high and flag==0:
        count+=1
        mid=(l+high)//2
        if x==a[mid]: 
            flag=1
            print(x,"found at position",mid,"with iterations",count)
        elif x<a[mid]:
            high=mid-1
        elif x>a[mid]:
            l=mid+1
    if flag==0:
        print("Element not found")

a=[]
for i in range(1001): a.append(i+1)
x=int(input("Enter element to be found: "))
a=sortt(a)
search(a,x)
