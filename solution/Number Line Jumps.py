#https://www.hackerrank.com/challenges/kangaroo/problem
x1,v1,x2,v2=map(int,input().split())
if v2>=v1:
    print("NO")
elif x1<x2 and v1>v2:
    while x1<x2:
        x1=x1+v1
        x2=x2+v2
        if x1==x2:
            print("YES")
            break

    if x1>x2:
        print("NO")
