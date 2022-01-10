#https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=profile
s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
dm=list(map(int,input().split()))[:m]
dn=list(map(int,input().split()))[:n]
count_m=0
count_n=0
for i in dm:
    if i>=s-a and i<=t-a:
        count_m+=1        
for i in dn:
    if i>=-(b-s) and i<=-(b-t):
        count_n+=1
print(count_m)
print(count_n)
