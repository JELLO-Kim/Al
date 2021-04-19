import sys
# 내가 푼 코드
N = int(input()) # 곶감이 배치된 행 갯수
n = [list(map(int, input().split())) for _ in range(N)] # 곶감이 배치된 행열
M = int(input()) # 총 회전 수
m = [list(map(int, input().split())) for _ in range(M)] # 각 회전의 상세 내용 (index, 좌/우, 회전횟수)
res=0
for i in m:
    target=n[i[0]-1] # 회전이 진행될 곶감의 행 위치
    if i[1]==0: # 왼쪽으로 회전일 경우
        cnt=target+[0]*(int(i[2])) # 회전 수 만큼 target 행의 우측에 0을 추가한다
        for j in range(i[2]):
            cnt[(-i[2]+j)]=cnt[j] # 추가된 0의 자리에 회전됏을 경우의 곶감을 위치시킨다.
        cnt=cnt[i[2]:] # 회전 이후 형태만 추출한다.
    elif i[1]==1:  # 오른쪽으로 회전일 경우 (이하는 위의 로직과 같다)
        cnt=[0]*(int(i[2]))+target
        for j in range(i[2]):
            cnt[j] = cnt[(-i[2]+j)]
        cnt=cnt[:-i[2]]
    n[i[0]-1] = cnt # 기존 곶감 배열을 바뀐 형태로 갱신한다.
p=1 # 초기값이 1인 변수 p 선언
for row in n:
    if p==1: # p가 1일 경우 (제일 윗 행렬일 경우) 행의 전체 열을 더한다
        res=sum(row)
        p+=1
    elif p<=(N//2+1): # 중간 지점 행까지 좌우로 열을 하나씩 제외하면서 합을 구한다
        res+=sum(row[p-1:-p+1])
        p+=1
    else: # 과정이 전체 행의 중간지점을 넘었을 경우
        if p==N: # 마지막 행에 도달했을 경우 해당 행의 모든 열을 더해준다.
            res+=sum(row)
        res+=sum(row[N-p:-N+p]) # 좌우로 열을 하나씩 더하면서 합을 구한다.
        p+=1
print(res) # 최종 합을 출력한다.

#소스코드
import sys
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h, t, k=map(int, input().split()) # 회전에 대한 정보를 각각의 변수에 담는다.
    if(t==0): # 왼쪽으로 회전일 경우
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) # 왼쪽의 것을 pop으로 빼낸뒤 해당 값을 최우측에 append한다
    else: # 오른쪽으로 회전일 경우
        for _ in range(k): # 오른쪽으 것을 pop으로 빼낸뒤 해당 값을 최좌측에 append한다
            a[h-1].insert(0, a[h-1].pop())

res=0
s=0
e=n-1
for i in range(n): # 곶감 행의 갯수 만큼 반복문 진행
    for j in range(s, e+1): # 합을 구할 행의 조건 설정
        res+=a[i][j] # 해당 행의 합을 res에 더한다.
    if i<n//2: # 횟수가 전체 행의 절반보다 적을 경우 시작번호는 1씩 추가하고, 종료 번호는 1씩 감소시킨다.
        s+=1
        e-=1
    else: # 횟수가 전체 행의 절반이상일 경우 시작번호는 1씩 감소하고 종료 번호는 1씩 증가한다.
        s-=1
        e+=1
print(res) # 최종 합을 출력한다.