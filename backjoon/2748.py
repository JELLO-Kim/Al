import sys
input = sys.stdin.readline
# n = int(input())
n = 1
def dp_fibo(n):
    dp = [0] * (n+1)
    dp[0], dp[1], dp[2] = 0, 1, 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]

print(dp_fibo(n))