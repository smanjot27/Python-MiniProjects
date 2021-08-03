text1=input("Enter first string: ")
text2=input("Enter second string: ")
count1=0
count2=0
for i in text1: count1+=ord(i)
for j in text2: count2+=ord(j)
if count1==count2: print("Strings are Anagrams")
else: print("Strings are not anagrams")
