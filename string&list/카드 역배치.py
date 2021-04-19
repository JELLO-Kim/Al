import sys
# 내가 푼 코드
N = [list(map(int, input().split())) for _ in range(10)] # 구간의 조건들을 list속 list로 받는다
card=list(range(21)) # 0부터 20까지 있는 card라는 리스트를 생성한다.

for i in N: # 각 구간에 대해서 반복문을 진행한다
    rep=card[i[0]-1:i[1]] # 구간에 해당되는 card의 구간을 rep라는 리스트로 만든다.
    card[i[0]-1:i[1]]=rep[::-1] # 뒤집은 결과를 card에 갱신한다

for j in card:
    print(j, end=' ')

# 소스코드
card=list(range(21))
for _ in range(10):
    s, e=map(int, input().split()) # 각 구간의 조건을 두개의 변수에 따로 담아 바로 반복문을 진행한다
    for i in range((e-s+1)//2):
        card[s+i], card[e-i] = card[e-i], card[s+i]

card.pop(0) # 필요없는 0번째 card의 값을 제거한다 (1~20까지만 있으면 됨)
for x in card:
    print(x, end=' ')