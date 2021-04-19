import sys
# 혼자서 해결 X , 소스 코드 참고함

# 해결하지 못한 부분
# 연속된 정답일 경우 가산점 부여해주기!

N = int(input())
K = list(map(int, input().split()))
cnt=0 # 가산점을 저장할 변수 cnt를 0으로 초기화한다.
score=0
for i in range(N):
    if K[i]==1: # 반복문을 진행하는 점수가 정답일 경우 가산점을 1로 갱신하고 최종 점수를 갱신한다.
        cnt+=1
        score+=cnt
    else: # 반복문을 진행하는 점수가 오답일경우 쌓여가던 가산점을 0으로 초기화 한다.
        cnt=0
print(score) # 최종 점수를 출력한다.
