#https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=next-challenge&h_v=zen&isFullScreen=false
n = int(input())
l = list(map(int,input().split()))
print(l.count(max(l)))
