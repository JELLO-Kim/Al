import sys
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]


def check(a):
    if a == 0:
        return True
    # 완전제곱수인지 체크
    for k in range(1, a//2):
        if k**2 == a:
            return True
    return False

def reverse(target):
    tmp = 0
    while target > 0:
        new_a = target%10
        tmp = tmp*10 + new_a
        target = target//10
    return tmp


max_a = -1
for x in range(n):
    for y in range(m):
        for xk in range(1, n):
            for yk in range(-m+1, m):
                if yk == 0:
                    continue
                a = 0
                kk = 0
                while 0 <= x+xk*kk < n and 0 <= y+yk*kk < m:
                    # 한 루프 끝나면 xk랑 yk + 1씩 해준다.
                    a = a * 10 + board[x + xk*kk][y + yk*kk]
                    if check(a):
                        max_a = max(max_a, a)
                    # a의 역수도 체크해준다
                    reverse_a = reverse(a)
                    if check(reverse_a):
                        max_a = max(max_a, reverse_a)
                    kk += 1
print(max_a)
