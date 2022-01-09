#https://www.hackerrank.com/challenges/grading/problem?isFullScreen=false

n=int(input())
def round(a):
    if int(a[1]) in [3,4]:
       print(a[0]+'5')
    else:
        print(str(int(a[0])+1)+'0')
for i in range(n):
    a=input()
    if int(a)<38 or int(a[1]) in [1,2,0,5,6,7]:
        print(a)
    else:
        round(a)
