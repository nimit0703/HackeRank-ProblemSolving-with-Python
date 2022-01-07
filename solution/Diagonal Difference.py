# https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=profile

n=int(input())
a=list()
b=list()
for i in range(n):
    row=list(map(int,input().split()))[:n]
    a.append(row[i])
    b.append(row[n-i-1])   
print(abs(sum(a)-sum(b)))
