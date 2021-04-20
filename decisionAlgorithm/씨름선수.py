import sys

# 두가지 조건을 비교해 결과값 도출하기
# 한가지 승리조건대로 정렬 후, 나머지 값을 비교하기

k, n = map(int, input().split())
m = [tuple(map(int, input().split())) for _ in range(n)] # list속 tuple 형태로 개개인의 키와 몸무게를 담았다

m.sort(reverse=True) # 키의 내림차순으로 정렬한다
tmp=0 # 비교될 몸무게가 기록될 변수
res=0 # 승리자 표시 변수
for a, b in m:
    if b>tmp: # 키가 내림차순으로 정렬되어 있어 몸무게가 이전것보다 더 무거울 경우 승리자가 된다
        tmp=b # 더 무거운 값의 몸무게로 tmp값이 갱신된다
        res+=1
print(res)