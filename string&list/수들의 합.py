import sys
# 내가 푼 코드 => 시간초과
N, M = input().split()
A=list(map(int, input().split()))
cnt=0
res=0
for i in range(int(N)):
    cnt=A[i]
    for j in A[i+1:]:
        cnt+=j
        if cnt>int(M):
            break
        if cnt==int(M):
            res+=1
            cnt=i
            break
print(res)

# 소스코드
N, M = map(int, input().split())
A=list(map(int, input().split()))
lt=0
rt=1
cnt=A[0]
res=0
while True:
    if cnt<M:
        if rt<N:
            cnt+=A[rt]
            rt+=1
        else:
            break
    elif cnt==M:
        res+=1
        cnt-=A[lt]
        lt+=1
    else:
        cnt-=A[lt]
        lt+=1
print(res)