import sys
# 내가 푼 코드
N = int(input())
K = [list(map(int, input().split())) for _ in range(N)]
price=[]
for k in K:
    for i in k:
        if k.count(i)==3: # 3번 던진 눈의 값이 모두 같을 경우
            price.append(10000+(i*1000))
        elif k.count(i)==2: # 3번 던진 눈들 중 두개의 값이 같을 경우
            price.append(1000+(i*100))
        else: # 3번 던진 눈이 모두 다른 값일 경우 나온 눈들 중 가장 큰 값으로 상금이 책정된다.
            price.append(max(k)*100)
print(max(price)) # 저장된 상금금액들 중 가장 큰 값을 출력한다.
