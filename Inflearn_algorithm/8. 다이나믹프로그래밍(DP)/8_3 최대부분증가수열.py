import sys
sys.stdin = open("../input.txt")

n = int(input())
arr = [0] + list(map(int, input().split()))
dy = [0] * (n+1) # 가장 긴 수열의 길이 값 저장
dy[1] = 1
res = 0
for i in range(2, n+1):
    max_n = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max_n:
            max_n = dy[j]
    dy[i] = max_n + 1
print(max(dy))