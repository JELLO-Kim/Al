import sys
# 내가 푼 코드
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

# 행의 합 구하는 함수
def res_1(x):
    sum_1=0
    for i in x:
        if sum(i)>sum_1:
            sum_1=sum(i)
    return sum_1

# 열의 합 구하는 함수
def res_2(y):
    sum_2 = 0
    for i in range(N):
        a = [num[i] for num in y]
        if sum(a)>sum_2:
            sum_2=sum(a)
    return sum_2

# 좌-상 부터 우-하 까지 합을 구하는 함수
def res_3(z):
    sum_3 = 0
    a=0
    for row in z:
        sum_3+=row[a]
        a+=1
        if a>N:
            break
    return sum_3
# 우-상 부터 좌-하 까지 합을 구하는 함수
def res_4(g):
    sum_4 = 0
    a=N-1
    for row in g:
        sum_4+=row[a]
        a-=1
        if a<0:
            break
    return sum_4

a = res_1(M)
b = res_2(M)
c = res_3(M)
d = res_4(M)
print(max(a, b, c, d)) # 각 합의 최대값을 출력한다.

# 소스 코드

# 1. 행과열의 합 한번에 구하기 / 이 중 큰 수를 largest에 저장한다.      
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
largest=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
# 2. 두종류의 대각선의 합을 한번에 구하기 / 위의 반복문과 비교했을때 더 큰값을 largest에 저장한다.
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest) # 최종 largest값을 출력한다.