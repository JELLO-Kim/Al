import sys
sys.stdin = open("input.txt", "r")

n = int(input())
apt = [list(map(int, input())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

d = 1
d_count = 1

def DFS(x, y):
    global ch
    global d_count
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and apt[xx][yy] == 1:
            apt[xx][yy] = 0
            ch[xx][yy] = d
            d_count += 1
            DFS(xx, yy)


res = {}
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            apt[i][j] = 0
            ch[i][j] = d
            DFS(i, j)
            res[d] = d_count
            d_count = 1
            d += 1
print(len(list(res.keys())))
res = sorted(res.items(), key=lambda x:x[1])
for dd in res:
    print(dd[1])