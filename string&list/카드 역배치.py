import sys
# 내가 푼 코드
N = [list(map(int, input().split())) for _ in range(10)]
card=list(range(21))

for i in N:
    rep=card[i[0]-1:i[1]]
    card[i[0]-1:i[1]]=rep[::-1]

for j in card:
    print(j, end=' ')

# 소스코드
card=list(range(21))
for _ in range(10):
    s, e=map(int, input().split())
    for i in range((e-s+1)//2):
        card[s+i], card[e-i] = card[e-i], card[s+i]

card.pop(0)
for x in card:
    print(x, end=' ')