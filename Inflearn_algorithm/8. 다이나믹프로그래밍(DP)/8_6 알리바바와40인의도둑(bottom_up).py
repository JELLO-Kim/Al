import sys

sys.stdin = open("../input.txt")
dx = [0, 1]
dy = [1, 0]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0] * n for _ in range(n)]
dy[0][0] = arr[0][0]
for x in range(n):
    for y in range(n):
        # 위에서 온것 확인
        aa = None
        if x > 0:
            aa = dy[x - 1][y]
        # 왼쪽에서 온것 확인
        if y > 0:
            if aa:
                aa = min(aa, dy[x][y - 1])
            else:
                aa = dy[x][y - 1]
        if not aa:
            dy[x][y] = arr[x][y]
        else:
            dy[x][y] = aa + arr[x][y]
print(dy[n-1][n-1])