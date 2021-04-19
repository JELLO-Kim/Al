import sys
# 내가 푼 코드
n=int(input())
res=0
t=[]
# 주어진 행열의 가장자리에 0을 추가하는 과정
for k in range(n+2):
    if k==0:
        t.append([0]*(n+2))
    elif k==(n+1):
        t.append([0]*(n+2))
    else:
        t.append([0]+list(map(int, input().split()))+[0])
# 봉우리 갯수 파악하는 과정 (가장자리는 다 0이므로 시작 범위는 1번째 index 부터이다)
for i in range(1, n+1):
    for j in range(1, n+1):
        if (t[i-1][j]<t[i][j]) and (t[i+1][j]<t[i][j]) and  (t[i][j-1]<t[i][j]) and  (t[i][j+1]<t[i][j]): # 해당지점이 상하좌우보다 값이 클 경우에만 봉우리로 판단한다.
            res+=1
print(res)

# 소스 코드 (4방향 탐색법 알아두기!!)
import sys
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
# 주어진 행렬의 가장자리에 0을 추가한다
a.insert(0, [0]*n)
a.append([0]*n)
for x in a: 
    x.insert(0, 0)
    x.append(0)

cnt=0
dx=[-1, 0, 1, 0] #4방향 탐색법의 좌우 지점
dy=[0, 1, 0, -1] #4방향 탐색법의 상하 지점
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)