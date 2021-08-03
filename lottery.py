import matplotlib.pyplot as plt
import random
account=0
x=[]
y=[]
for i in range(365):
    x.append(i)
    rn=random.randint(1,10)
    bet=random.randint(1,10)
    if rn==bet: account=account+900-100
    else: account-=100
    y.append(account)
print("Net Balance:",account)
plt.plot(x,y)
plt.show()
