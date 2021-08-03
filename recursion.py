def fact(n):
    if n==1:
        return n 
    else:
        return n*fact(n-1)
def fibo(n):
    if n==0: return n
    elif n==1 or n==2:
        return 1
    else:    
        return(fibo(n-1)+fibo(n-2))
def bs(array,low,high,ele):
    if low<=high:
        mid=(low+high)//2
        if ele==array[mid]: return mid
        elif ele<array[mid]:return bs(array,0,mid-1,ele)
        else: return bs(array,mid+1,high,ele)
    else:
        return -1
print("----Factorial of a number----")
num=int(input('enter any positive number: '))
print("Factorial of",num,'is:',fact(num))
print()
print("----Fibonacci Series----")
terms=int(input("enter the  term of fibonacci series to display:"))
print('Term : ',fibo(terms))
print()
print("----Binary Search----")
array=[]
for i in range(100): array.append(i+1)
ele=int(input("Enter the element you want to find:"))
pos=bs(array,0,len(array)-1,ele)
if pos==-1:
    print('element not found')
else:
    print('element found at position',pos)
