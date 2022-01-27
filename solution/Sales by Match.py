#https://www.hackerrank.com/challenges/sock-merchant/problem?h_r=profile
n=int(input())
arr=list(map(int,input().split()))
a=list(set(arr))
count=0
for i in a:
    p=arr.count(i)
    count += int(p/2)
print(count)
