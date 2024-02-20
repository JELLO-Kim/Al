# 비트마스킹 방식으로 문제풀기
import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt")

m = int(input())
s = 0
for _ in range(m):
    order_info = list(input().split())
    order = order_info[0]
    n = None if len(order_info) == 1 else int(order_info[1])
    if order == "add":
        # S |= (1 << idx)
        s |= (1 << n-1)
    elif order == "remove":
        # s &= ~(1<<idx)
        s &= ~(1 << n-1)
    elif order == "toggle":
        if (s&(1<<(n-1))):
            s &= ~(1<<(n-1))
        else:
            s |= (1<<(n-1))
    elif order == "check":
        if (s&(1<<(n-1))):
            print(1)
        else:
            print(0)
    elif order == "all":
        s = (1<<20)-1
    elif order == "empty":
        s = 0
print(s)