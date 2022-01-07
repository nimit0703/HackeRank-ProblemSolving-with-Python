# https://www.hackerrank.com/challenges/plus-minus/problem?h_r=profile

n=int(input())
l=list(map(int,input().split()))[:n]
cp=cn=cz=0
for i in l:
    if i>0:
        cp+=1
    elif i<0:
        cn+=1
    else :
        cz+=1
print("{:.6f}".format(cp/n))
print("{:.6f}".format(cn/n))
print("{:.6f}".format(cz/n))
