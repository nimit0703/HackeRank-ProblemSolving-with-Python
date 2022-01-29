#https://www.hackerrank.com/challenges/counting-valleys/problem?h_r=profile&h_r=next-challenge&h_v=zen
n=int(input())
p=input()
l=0
c=0
for i in p:
    if i=="U":
        l+=1
    elif i=="D":
        l-=1
    if l==0 and i=="U":
        c+=1    
print(c)
