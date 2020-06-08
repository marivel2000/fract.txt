from itertools import combinations
s=input()
n=len(s)
l1=list(s)
def find(l2,k):
    m=""
    for r in l2:
        m+=r
    l3=[]
    a=k[:]
    a=a.replace(m,"",1)
    if m in a:
        l3.append(m)
        l3.append(len(m))
    return l3
k=[]
for i in range(n):
    for j in (combinations(l1,i)):
        l2=list(j)
        k.append(find(l2,s))
z=[]
for i in k:
    if len(i)>1:
        z.append(i)
for u in (z[len(z)-1]):
    print(u)
    break
