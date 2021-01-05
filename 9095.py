# 22:45 start - 23:01 Failed
# t = int(input())
# dp = [1, 2, 4] * 12
# for i in range (4, t+1):
#     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# print(dp[t])

# # # 23:03 Re start - 23:14 End Success 
t = int(input()) # test-case 입력하기
for i in range(t): # test-case 횟수만큼 다음의 행동반복된다.
    dp = [1, 2, 4] # dp의 초깃값 설정 #0 = 1, #1 = 2, #2 = 4
    n = int(input()) # 구하고자 하는 순번 입력
    for i in range(3, n): # dp순서가 0번째부터 시작했으므로 n+1이 아닌 n 번째에서 끝나는게 맞다
        dp.append(dp[i-3] + dp[i-2] + dp[i-1]) # dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n-1]) # dp의 순서가 0번째 부터 시작이므로 n을 입력하여 이에 대항하는 값을 찾으려면 n-1번째 순서가 맞다.

# IndexError !!
t = int(input())
for i in range(t):
    n = int(input())
    dp = [1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(3, n):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n-1])

# IndexError: list assignment index out of range 라고 뜬다.
# 원소가 없는 상태에서는 새로 지정하지 못한다!!!!!!!
# dp[i]의 값이 현재 존재하지 않기 때문에 dp[i] =  ~~~ 라고 설정하지 못한다.
# 이를 대체하기 위해 appen나 insert를 사용한다.