#https://www.hackerrank.com/challenges/bon-appetit/problem?h_r=profile
n,k,=map(int,input().split())
bill=list(map(int,input().split()))
charged=int(input())

bill.remove(bill[k])
annabill=int(sum(bill)/2)

if annabill < charged:
    print(charged-annabill)
else:
    print("Bon Appetit")
