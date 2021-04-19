import sys
# 내가 푼 코드
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
k = N//2
j = -k
res = 0
p=0 # 진행 횟수를 0으로 초기화 한다
for i in M:
    res+=sum(i[k:j])
    if p < N//2: #총 진행 횟수가 전체 행의 갯수 절반보다 적을 경우 좌우 열을 하나씩 늘려가면서 합을 구한다.
        if k > 0:
            k-=1
            j=-k
            if k==0:
                j=N
        p+=1
    else: # 그 반대의 경우 좌우 열을 하나씩 줄여가면서 합을 구한다
        k+=1
        j=-k
        p+=1
print(res)

# 소스코드
import sys
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2 # 좌우 열을 지정하는 값을 모두 전체 열의 절반 값으로 초기화 한다.
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
