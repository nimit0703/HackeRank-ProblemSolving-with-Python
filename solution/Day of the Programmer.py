#https://www.hackerrank.com/challenges/day-of-the-programmer/problem?h_r=profile
n=int(input())


if(n>=1700 and n<=1917):
    if n%4==0:
        print("12.09."+str(n))
    else:
        print("13.09."+str(n))
        
elif (n>=1919 and n<=2700):
    if n%400==0 or (n%4==0 and n%100!=0):
        print("12.09."+str(n))
    else:
        print("13.09."+str(n))
elif n>1917 and n<1919:
    print("26.09."+str(n))
