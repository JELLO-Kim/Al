import sys
sys.stdin = open("../input.txt")
# 한번에 최대 두계단씩 이동한다
# 입력 : 7 / 출력 : 21
n = 7
dy = [0] * (n + 1)


def bottom_up(n):
    dy[1] = 1
    dy[2] = 2
    for i in range(3, n+1):
        dy[i]=dy[i-1] + dy[i-2]
    return dy[n]

def top_down(n):
    if dy[n] > 0:
        return dy[n]
    if n == 1 or n == 2:
        return n
    else:
        dy[n] = top_down(n-1) + top_down(n-2)
        return dy[n]

print(f"bottom up : {bottom_up(n)}")
print(f"top down : {top_down(n)}")
