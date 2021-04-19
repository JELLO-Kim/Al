import sys
# 내가 짠 코드2ver _ list 생성해놓기
N, M = map(int, input().split())
cnt=[0]*(N+M+1) # 두개의 정다면체의 면의 갯수합 +1만큼의 0을 가진 list를 선언한다.
for n in range(1, N+1): # 정 N면체의 면의 갯수만큼 반복문 진행
    for m in range(1, M+1): # 정 M면체의 면의 갯수만큼 반복문 진행
        cnt[n+m]+=1 # 반복문을 진행하는 각 정다면체의 수의 합에 해당하는 cnt의 index값에 1을 추가한다.
max_count=max(cnt) # cnt의 최대값을 max_count 변수에 선언한다.
for num, count in enumerate(cnt): # cnt 리스트 중 값이 max_count인 것의 index를 구한다. 이때의 index는 곧 두 정다면체의 합이다.
    if count==max_count:
        print(num, end=' ')

# 내 원래 코드
tmp=[]
for n in range(1, N+1):
    for m in range(1, M+1):
        tmp.append(n+m) # 두개 정다면체의 합을 빈 리스트인 tmp에 append 한다.
set_tmp=set(tmp) # 중복되는 값을 없애주어 set_tmp라는 변수에 저장한다.
result=[]
for s in set_tmp:
    tt=[tmp.count(s), s] # tt라는 리스트에 반복문을 진행하는 정다면체 합의 경우의 갯수와 그 합을 기록한다.
    result.append(tt) # 그 값으로 나온 List를 result라는 빈 list에 append 한다.
result.sort() # 갯수의 내림차순으로 정렬한다.
answer=[a[1] for a in result if a[0]==result[-1][0]] # 반복문을 진행하면서 각각 list의 count수가 제일 큰 count수와 같다면 answer라는 list에 그 값을 기록한다. (값 = 두 정다면체의 합의 수)
for row in answer:
    print(row, end=' ')