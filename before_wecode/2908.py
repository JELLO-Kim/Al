# 뒤집은 수 중 큰수 출력
"""
734 893 -> 437
"""
# max내장함수는 list 속 인자들을 int로 변환하여 비교하게 한다. (자동변환)

def reverse(x):
    t = 0
    while x>0:
        t = t*10 + x%10
        x = x//10
    return t

def sol_one():
    a, b = map(int, input().split())
    c = a.reverse()
    print(c)
    a_revers = reverse(a)
    b_revers = reverse(b)
    print(max(a_revers, b_revers))

def sol_two():
    a, b = input().split()
    print(max(int(a[::-1]),int(b[::-1])))

def sol_three():
    print(max(input()[::-1].split()))