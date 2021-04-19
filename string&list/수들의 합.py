import sys
# 내가 푼 코드 : 채점소요시간이 오래걸린다. (지정 조건 없이 중첩 for loops를 돌렸기 때문이라 생각한다.)
N, M = input().split()
A=list(map(int, input().split()))
cnt=0
res=0
for i in range(int(N)):
    cnt=A[i]
    for j in A[i+1:]:
        cnt+=j
        if cnt>int(M): # 조건에 맞는것 없이 구하고자 하는 값보다 합이 커질경우 바로 반복문을 중단한다.
            break
        if cnt==int(M): # 조건에 맞는 경우를 발견했을 경우 res값을 하나 더해주고 cnt값은 i값으로 초기화 해준다. 그리고 반복문 중단한다.
            res+=1
            cnt=i
            break
print(res)

# 소스코드
N, M = map(int, input().split())
A=list(map(int, input().split()))
lt=0 # 시작지점의 순번 (합을 구하는 구간의 최 좌측)
rt=1 # 오른쪽 지점의 순번 (합을 구하는 구간의 최 우측)
cnt=A[0]
res=0
while True: # break 상황이 오기 전까지 계속 반복된다.
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