import sys
import time

sys.stdin = open("input.txt")
from collections import deque
n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]

one_count = 0
for i in city:
    for j in i:
        if j == 1:
            one_count += 1
print(one_count/(n*n) * 100)


# bfs 버전 (N^3)
def solution_bfs():
    visit = [[0]*n for _ in range(n)]
    dq = deque()
    for from_first, m in enumerate(city):
        for to_city, moving in enumerate(m):
            if moving == 1 and visit[from_first][to_city] == 0:
                visit[from_first][to_city] = 1
                dq.append(to_city)
                while dq:
                    to_city = dq.popleft()
                    for next_to, next_move in enumerate(city[to_city]):
                        if next_move == 1 and visit[from_first][next_to] == 0:
                            visit[from_first][next_to] = 1
                            dq.append(next_to)

    for i in visit:
        print(*i)

def solution_floid():
    """
    i에서 j의 경로를 탐색하면서 거쳐가는 k 노드의 값을 확인, k 값으로 연결된 i, j는 연결가능하다
    """
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if city[i][k] == 1 and city[k][j] == 1:
                    city[i][j] = 1
    for row in city:
        print(*row)


s_one = time.time()
solution_bfs()
e_one = time.time()
print(f"deque 소요시간 : {e_one - s_one}")
s_two = time.time()
solution_floid()
e_two = time.time()
print(f"floyd 소요시간 : {e_two - s_two}")
