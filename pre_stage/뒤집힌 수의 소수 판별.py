import sys
N = int(input())
K = list(map(int, input().split()))
# 내가 푼 코드 1

# 수를 뒤집는 함수
def reverse(x):
    x_r=int(str(x)[::-1])
    return x_r

# 들어온 값이 소수인지 판별하는 함수
def isPrime(x):
    if x==1:
        return False
    for i in range(3, x):
        if x%i==0:
            return False
    return True

# 반복문을 통해 들어온 값의 뒤집은 값이 소수일 경우 그 수들을 한줄로 출력한다.
for k in K:
    if isPrime(reverse(k)):
        print(reverse(k), end=' ')