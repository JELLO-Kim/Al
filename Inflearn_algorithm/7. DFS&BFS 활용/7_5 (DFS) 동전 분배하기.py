import sys
from time import time
sys.stdin = open("input.txt", "r")
start = time()

n = int(input())
coin = [int(input()) for _ in range(n)]
money = [0]*3
res = sum(coin)
def DFS(L):
    global money
    global res
    if L == n:
        # money = money[1:]
        if len(list(set(money))) == 3:
            max_p = max(money)
            min_p = min(money)
            if max_p-min_p < res:
                res = max_p-min_p
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]

DFS(0)
print(res)
end = time()
print(f"소요시간 : {end-start}")  # 0.9498510360717773