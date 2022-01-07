#https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=false

l=list(map(int,input().split()))
l.sort()
minimum=sum(l[:4])
maximum=sum(l[1:])
print(minimum,maximum)
