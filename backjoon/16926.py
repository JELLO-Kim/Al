import sys
from collections import deque
sys.stdin = open("input.txt", "r")
n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
new_board = [[0]*m for _ in range(n)]
q = deque()
# 2차원 배열을 1차원 배열로 펼치기
loop_count = min(n, m) // 2

for i in range(loop_count):
    q.clear()
    # 위쪽
    q.extend(board[i][i:m-i])
    # 오른쪽 (모서리 제외)
    q.extend([row[m-i-1] for row in board[i+1:n-i-1]])
    # 아래쪽
    q.extend(board[n-i-1][i:m-i][::-1])
    # 왼쪽 (모서리 제외)
    q.extend([row[i] for row in board[i+1:n-i-1][::-1]])
    q.rotate(-r)

    # 다시 board 정렬하기
    # 위
    for j in range(i, m-i):
        new_board[i][j] = q.popleft()
    # 오른쪽
    for j in range(i+1, n-(i+1)):
        new_board[j][m-i-1] = q.popleft()
    # 아래쪽
    for j in range(m-i-1, i-1, -1):
        new_board[n-i-1][j] = q.popleft()

    # 왼쪽
    for j in range(n-i-2, i, -1):
        new_board[j][i] = q.popleft()

for row in new_board:
    print(*row)

"""
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14
"""