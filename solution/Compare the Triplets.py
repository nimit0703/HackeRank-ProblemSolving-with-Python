# https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=profile
a=list(map(int,input().split()))[:3]
b=list(map(int,input().split()))[:3]
result=[0,0]
for i in range(3):
    if a[i]> b[i]:
        result[0]+=1
    elif a[i]<b[i]:
        result[1]+=1
print(*result)
