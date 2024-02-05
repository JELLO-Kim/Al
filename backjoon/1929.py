# N부터 M 까지의 수 중 소수 구하기
def find_minority():
    N, M = map(int, open("input.txt").read().split())
    ch = [0]*(M+2)
    answer = 0
    for i in range(2, M+1):
        if ch[i] == 0:
            if i >= N:
                print(i)
            for j in range(i, M+1, i):
                ch[j] = 1

# 숫자 뒤집기
def reverse(x):
    res = 0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

# 소수인지 확인하는 함수
def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True

# 주어진 수의 뒤집은 수가 소수인거 찾기
def find_reverse_minority():
    N, *ch = open("input.txt").read().split()
    for row in ch:
        reverse_row = reverse(int(row))
        if isPrime(reverse_row):
            print(reverse_row, end=" ")

find_reverse_minority()