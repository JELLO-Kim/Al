import sys
sys.stdin = open("../input.txt")
n = int(input())
doll = [list(map(int, input().split()))for _ in range(n)]
doll.sort(key=lambda x:x[0], reverse=True)
dy = [0] * n

dy[0] = doll[0][1]

for i in range(1, n):
    this_max = [0]
    for j in range(i-1, -1, -1):
        # 넓이 조건 확인 and 무게 조건 확인
        if doll[j][2] > doll[i][2]:
            this_max.append(dy[j])
    dy[i] = max(this_max) + doll[i][1]
print(max(dy))

