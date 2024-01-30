# 좌우 point 찍어 for loop 으로 풀던것을 BFS 방식으로 풀어보기
# BFS 는 Queue 자료구조를 활용한다.
import sys
from collections import deque
sys.stdin = open("input.txt","r")
n = int(input())
apple = list()
for _ in range(n):
    apple.append(list(map(int, input().split())))

# 정중앙에서부터 시작하는 마름모 모양
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
done_apple = [[0]*n for _ in range(n)]
dq = deque()
dq.append((n//2, n//2))
total_apple = 0

need_count = n//2  # n을 2로나는 몫 횟수 만큼 진행하면 된다.
try_count = 0

while dq:
    if try_count == need_count+1:
        print(total_apple)
        break
    for _ in range(len(dq)):
        target = dq.popleft()
        if done_apple[target[0]][target[1]] == 0:
            done_apple[target[0]][target[1]] = 1  # 확인 체크하기
            total_apple += apple[target[0]][target[1]]  # 갯수 더해주기
            for i in range(4):
                next_x = dx[i]
                next_y = dy[i]
                dq.append((target[0]+next_x, target[1]+next_y))
    try_count += 1