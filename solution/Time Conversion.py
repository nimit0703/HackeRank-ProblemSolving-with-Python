https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=false

s=input()
time=s[8:]
if time=='PM':
    a=12+int(s[:2])
    s1=str(a)+s[2:8]
    print(s1[:8])
else:
    print(s[:8])
