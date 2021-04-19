import sys
# 내가 푼 코드
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
k = N//2
j = -k
res = 0
p=0
for i in M:
    res+=sum(i[k:j])
    if p < N//2:
        if k > 0:
            k-=1
            j=-k
            if k==0:
                j=N
        p+=1
    else:
        k+=1
        j=-k
        p+=1
print(res)

# 소스코드
import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)
