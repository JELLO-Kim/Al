import sys
# 내가 푼 코드
N = input()
K = len(N)
num="" # 빈 string을 선언한다
for i in range(K):
    try:
        if type(int(N[i])) is int: # for문이 진행되는 문자열 하나를 int형으로 변환했을때 그 타입이 int가 맞을 경우
            num+=N[i]
    except: # int형으로 타입 변환이 되지 않아 error 상황에 걸릴 경우 pass 한다.
        pass
res=int(num) # num을 int로 변환한다
cnt=0
for j in range(1, res+1): # 해당 수의 약수의 갯수를 구한다
    if res%j==0:
        cnt+=1

print(res)
print(cnt)

# 소스코드
N=input()
res=0
for i in N:
    if i.isdecimal(): # ".isdecimal()"함수를 사용해 숫자인지 유무를 확인한다
        res=res*10+int(i)
print(res)
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)