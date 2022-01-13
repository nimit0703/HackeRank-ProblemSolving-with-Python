#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=profile
n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    for j in a[i+1:]:
        
        if (a[i]+j)%k==0:
            count+=1
            
print(count)
