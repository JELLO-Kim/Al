import sys

# lambda 함수를 활용하여 정렬하기

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
m.sort(key=lambda x:(x[1], x[0])) #lambda 함수를 사용해 회의끝나는 시간 오름차순으로 정렬하기
cnt=0
ep=0 # 첫번째 회의종료시간 비교값으로 0을 세팅
for i in m:
    if i[0]>=ep: # 저장된 회의종료시간보다 반복문을 도는 회의 시작시간이 더 나중일 경우 회의 가능!
        print(i)
        ep=i[1] # 해당 회의의 종료시간으로 ep값을 갱신한다
        cnt+=1 # 회의 횟수가 1회 추가된다
print(cnt)