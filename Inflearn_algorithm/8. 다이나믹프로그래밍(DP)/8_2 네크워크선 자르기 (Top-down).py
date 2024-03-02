# 입력 : 33 / 출력 : 5702887
import sys
sys.stdin = open("../input.txt", "r")
n = int(input())
dy = [0] * (n + 1)
def top_down(n):
    if dy[n] > 0:
        return dy[n]
    if n == 1 or n == 2:
        return n
    dy[n] = bottom_up(n-1) + bottom_up(n-2)
    return dy[n]
print(top_down(n))

##################################################
def bottom_up(n):
    dy = [0] * (n + 1)
    dy[1] = 1
    dy[2] = 2
    for i in range(3, n+1):
        dy[i] = dy[i-1] + dy[i-2]
    return dy[n]
print(bottom_up(n))