# 20:46 start - 
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [1, 1, 1, 2, 2]
    if N > 5:
        for j in range(5, N):
            dp.append(dp[j-1] + dp[j-5])
    print(dp[N-1])

# 왜 이건 안됨??!!!!!!!!!!
T = int(input())
dp = [1, 1, 1, 2, 2]
for _ in range(T):
    N = int(input())
    if N > 5:
        for j in range(5, N):
            dp.append(dp[j-1] + dp[j-5])
    print(dp[N-1])