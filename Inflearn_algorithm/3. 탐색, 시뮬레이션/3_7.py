# 사과농장에서 이중 배열일때 다이아몬드 모양 안의 갯수들 더하기
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
apple_list = [list(map(int, input().split())) for _ in range(5)]
s=e=n//2
apple_sum = 0
for j in range(n):
    apple_sum += sum(apple_list[j][s:e+1])
    if j < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(apple_sum)