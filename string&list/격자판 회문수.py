import sys
# 내가 푼 코드
N = [list(map(int, input().split())) for _ in range(7)]
res=0
k=5
# 행의 회문수 판별
for a in N: # 들어온 리스트 속의 리스트 값을 반복문을 진행한다.
    for i in range(3): # 반복문을 진행하는 개별의 list에서 연속된 5개의 수가 회문수인지 확인한다
        if a[i:i+5]==list(reversed(a[i:i+5])): # 회문수가 맞다면 res의 값에 1을 추가한다.
            res+=1

# 열의 회문수 판별
cnt=[] # cnt라는 빈 list를 선언한다
for i in range(7): # 0번째 열부터 6번째 열까지 확인해야 한다.
    k=0
    while k<3: # 0, 1, 2 일때만 반복되도록 설정 (0+5=5, ..., 2+5=7)
        for j in range(5): # 하나의 열에 4개의 연속된 행의 수를 확인해야 한다.
            cnt.append(N[j+k][i])
        if cnt==list(reversed(cnt)): # 회문수가 맞다면 res에 1을 더해준다.
            res+=1
        cnt=[] # 하나의 검사가 끝나면 cnt를 빈 리스트로 초기화 해준다.
        k+=1 # 동일 열의 아래 행을 검사하기 위해 k의 값을 1씩 추가해준다.
print(res) # 최종 회문수 갯수 출력

# 소스 코드
import sys
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2): # 가운데 수를 제외하고 0번째와 4번째 값이 같은지 & 1번재와 3번째 값이 같은이 확인하여 회문수를 판별한다.
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt+=1
print(cnt)