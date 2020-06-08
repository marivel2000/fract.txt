from itertools import combinations
n=int(input())
l1=list(map(int,input().split(" ")))
k=int(input())
l3=[]
c=0
mul=1
for i in range(len(l1)):
    for j in (combinations(l1,i)):
        l2=list(j)
        for m in l2:
            mul=mul*m
        if mul<k:
            print(l2)
            c+=1
        mul=1
print(c-1)
