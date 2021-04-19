import sys
# 내가 푼 코드
N = int(input())
n = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
m = [list(map(int, input().split())) for _ in range(M)]
res=0
for i in m:
    target=n[i[0]-1]
    if i[1]==0:
        cnt=target+[0]*(int(i[2]))
        for j in range(i[2]):
            cnt[(-i[2]+j)]=cnt[j]
        cnt=cnt[i[2]:]
    elif i[1]==1: 
        cnt=[0]*(int(i[2]))+target
        for j in range(i[2]):
            cnt[j] = cnt[(-i[2]+j)]
        cnt=cnt[:-i[2]]
    n[i[0]-1] = cnt
p=1
for row in n:
    if p==1:
        res=sum(row)
        p+=1
    elif p<=(N//2+1):
        res+=sum(row[p-1:-p+1])
        p+=1
    else:
        if p==N:
            res+=sum(row)
        res+=sum(row[N-p:-N+p])
        p+=1
print(res)

#소스코드
import sys
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h, t, k=map(int, input().split())
    if(t==0):
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

res=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)