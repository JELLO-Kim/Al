import sys
sys.stdin = open("input.txt", "r")
min = 21740000
max = -21740000

min_xy = []
max_xy = []

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*6 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if m[i][j] > max:
            max = m[i][j]
            max_xy = [i, j]
        if m[i][j] < min:
            min = m[i][j]
            min_xy = [i, j]

# 최대 최소는 구했다.
            
dx = [-1,0,1,0]
dy = [0,-1,0,1]


cnt = 0
def DFS(x, y, ch):
    global cnt
    if m[x][y] == max:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<n and m[xx][yy] > m[x][y] and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                DFS(xx, yy, ch)
                ch[xx][yy] = 0
ch[min_xy[0]][min_xy[1]] = 1
DFS(min_xy[0], min_xy[1], ch)
print(cnt)