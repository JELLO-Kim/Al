import sys, time
from math import inf
sys.stdin = open("input.txt")
start = time.time()
def mine():
    n = int(input())
    stones = list(map(int, input().split()))
    dp = [-1] * (n)
    for i in range(n):
        for j in range(i+1, n):
            dp[j] = max(dp[j], (j - i) * (1 + abs(stones[i] - stones[j])))

    print(min(dp[1:]))
    print(f"소요시간 : {time.time() - start}") #  0.00016427040100097656

def sol():
    n = int(input())
    stones = list(map(int, input().split()))
    it = 1e9
    dp = [0] + ([it] * (n-1))
    check_list = [[] for _ in range(n+1)]
    for i in range(1, n):
        for j in range(0, i):
            new_k = (i - j) * (1 + abs(stones[i] - stones[j]))
            check_list[i].append(new_k)
            this_k = max(new_k, dp[j])
            dp[i] = min(dp[i], this_k)
    print(dp[n-1])
    print(f"소요시간 : {time.time() - start}") #  0.00016427040100097656

def sol2():
    n = int(input())
    stones = list(map(int, input().split()))
    it = 1e9
    # dp = [0] + ([it] * (n-1))
    dp = [0]*n
    for j in range(1, n):
        for i in range(n-1):
            if j <= i:
                break
            new_k = (j - i) * (1 + abs(stones[i] - stones[j]))
            this_k = max(new_k, dp[i])
            dp[j] = max(dp[j], this_k)
    print(dp[n-1])
    print(f"소요시간 : {time.time() - start}") #  0.00016427040100097656

sol()
