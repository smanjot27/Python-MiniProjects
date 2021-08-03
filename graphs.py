import matplotlib.pyplot as mat
import statistics as st
data=list(map(int,input().split()))
num=int(len(data)*0.1)
data.sort()
data=data[num:len(data)-num]
y=[]
for i in range(len(data)):
    y.append(5)
mat.plot(data,y)
mat.xlabel("Estimated Numbers")
mat.ylabel("Constant")
mat.plot([st.mean(data)],[5],'b^')
mat.plot([st.median(data)],[5],'ro')

mat.show()
