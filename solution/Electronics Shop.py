#https://www.hackerrank.com/challenges/electronics-shop/problem?h_r=profile&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
b,n,m=map(int,input().split())
kb=list(map(int,input().split()))[:n]
dr=list(map(int,input().split()))[:m]
a=list()
for i in kb:
    for j in dr:
        s=i+j
        if s<=b:
            a.append(s)
if len(a)==0:
    print("-1")
else:
    print(max(a))
