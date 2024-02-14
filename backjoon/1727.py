import sys
sys.stdin = open("input.txt", "r")

n = int(input())



def isPrime(n):
    # 소수 인지 확인
    for i in range(2, n//2):
        if n%i == 0:
            return False
    return True

def palindrome(n):
    tmp = 0
    while n > 0:
        new_n = n%10
        tmp = tmp*10 + new_n
        n = n//10
    return tmp

while True:
    if n == 1:
        n += 1
        continue
    if n != palindrome(n):
        n += 1
        continue
    if not isPrime(n):
        n += 1
        continue
    print(n)
    break