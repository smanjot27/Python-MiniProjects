import string
dic={}
for i in range(len(string.ascii_letters)):
    dic[string.ascii_letters[i]]=string.ascii_letters[i-5]
data=''
fil=open('streetfoodop.txt','w')
with open('streetfood.txt') as f:
    while True:
        c=f.read(1)
        if not c:
            print('End Of File')
            break
        if c in dic: 
            data=dic[c]
        else: data=c
        fil.write(data)
fil.close()

