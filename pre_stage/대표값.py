import sys
# 내가 푼 코드
N = int(input())
score = list(map(int, input().split()))
ave_score = sum(score)/N # 해당 점수들의 평균을 구한다
final_ave=int(round(ave_score+0.5, 0)) # 평균점수의 소수 첫째자리에서 반올림 한다. 이때 round함수는 round_half_even 방식이므로 0.5를 더한 뒤 반올림 해준다.

winner=[0, score[0]] # 해당 점수를 판별할 index 번호와 점수를 저장할 winner라는 임시 list를 선언한다. 기본값으로 0번째와 첫번째 점수에 대한 값이 저장되어 있다.
for index, row in enumerate(score):
    tmp = abs(row-final_ave) # tmp는 반복문을 진행중인 점수 한개와 평균점수 차의 절댓값을 담는다.
    if tmp < abs(final_ave-winner[1]): # tmp값이 기존의 winner에 저장된 값의 절댓값 보다 작을 경우
        winner[1]=row
        winner[0]=index+1 # 0부터 시작하는 index값에 +1 하여 "몇번째"학색인지 기록한다.
    elif tmp == abs(final_ave-winner[1]): # 두개의 값이 같다면 점수가 더 큰 것을 선별해야 한다.
        if row > winner[1]:
            winner[1] = row
            winner[0] = index+1
        
print(final_ave, winner[0])

#enumerate를 사용하지 않았을 경우의 코드
winner=score[0]
for row in score[1:]:
    if abs(final_ave - winner) >= abs(final_ave - row):
        if abs(final_ave - winner) == abs(final_ave - row):
            winner=max(winner, row)
        else:
            winner=row
print(final_ave, score.index(winner)+1)