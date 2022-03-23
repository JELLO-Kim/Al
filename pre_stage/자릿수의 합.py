import sys
# 내가 푼 답
N = int(input())
num = list(map(int, input().split( ))) # 주어진 수들을 list 형태로 담는다.
tmp=[0]*(N)

# 들어온 자연수의 각 자리수 합을 구하는 함수
def digit_sum(x):
    tmp=0
    for i in str(x): # 자연수 하나를 각 자리수별로 자르기 위해 string화 하여 반복문을 진행한다.
        tmp+=int(i) # 들어온 string 형태의 숫자를 int로 변환해 tmp 값에 더해준다.
    return tmp # 반복문이 끝나면 최종 합을 반환한다.


for idx, one in enumerate(num):
    tmp[idx]=digit_sum(one)
print(num[tmp.index(max(tmp))]) # 각 수들의 합중 가장 큰 값에 해당하는 Index와 같은 위치의 num list의 값을 출력한다.

# 소스코드 => 함수 이후 반복문만 참고

maxx=0 # 비교할 maxx의 값을 0으로 초기화 한다.
for x in num:
    tot=digit_sum(x)
    if tot>maxx: # 계산된 값이 기존의 maxx의 값보다 클 경우 maxx를 계산된 값으로 갱신해준다.
        maxx=tot
        res=x # 갱신된 tot의 값을 생성한 수를 res에 담는다.
print(res) # 최대값이 기록됐을 때의 수를 출력한다.