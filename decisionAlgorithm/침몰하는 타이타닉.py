import sys
# 제한된 인원수와 제한된 몸무게로 사용될 구명보트 수 구하기
n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort() # 몸무게 오름차순으로 정렬

cnt=0 # 사용되는 구명보트 수를 담을 변수
while l:
    if l[0]+l[-1]<=k: # 가장 가벼운 무게와 가장 무거운 무게를 합쳐 k 이하일 경우 함게 구명보트를 탄다
        l.pop()
        if len(l)!=2: # list에서 두명을 빼준다
            l.pop(0)
    else: # 그렇지 않을 경우 가장 무거운 무게만 따로 구명보트를 타게 한다
        l.pop() # list에서 구명보트를 탄 가장 무거운 무게만 뺀다
        
    cnt+=1

print(cnt)