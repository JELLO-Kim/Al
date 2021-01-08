# 19:55 star - 20:17 풀이 도움 - 20:31 이해완료 - 20:45 채점
n = int(input())
m = list(map(int, input().split()))
sum = [m[0]]
for i in range (n-1):
    sum.append(max(sum[i] + m[i+1], m[i+1]))
print(max(sum))

# # 풀이
# # m = -5, +2, -4, +3, +6, -4 , ...
# # i = 0
# sum.append(max(sum[0] +m[0+1], m[0+1]))
# sum.append(max(-5 + (+2), +2)
# sum.append(max(-3, +2)) # sum = [-5, +2]

# # i = 1
# sum.append(max(sum[1) + m[1+1], m[1+1])
# sum.append(max(+2 +(-4), -4))
# sum.append(max(-2, -4)) # sum = [-5, +2, -2]

# # i = 2
# sum.append(max(sum[2] + m[2+1], m[2+1]))
# sum.append(max(-2 + (+3)), +3)
# sum.append(max(+1, +3)) # sum = [-5, +2, -2, +3]

# # i = 3
# sum.append(max(sum[3] + m[3+1], m[3+1))
# sum.append(max(+3 + (+6), +6))
# sum.append(max(+9, +3)) # sum = [-5, +2, -2, +3, +9]

# # 이런식으로 sum 리스트가 채워진다. (0번째부터 n-1번째 까지 진행 / 총 횟수 = n번)
# # 그 중에서 가장 최대값을 Print 한다.