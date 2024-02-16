import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("input.txt")
n, m = map(int, input().split())
all_train = deque([deque([0]*20) for _ in range(n)])
# 명령어 처리하기
for _ in range(m):
    order_infos = list(map(int, input().split()))
    order = order_infos[0]
    i = order_infos[1]
    if order == 1:
        all_train[i-1][order_infos[2]-1] = 1
    elif order == 2:
        all_train[i-1][order_infos[2]-1] = 0
    elif order == 3:
        all_train[i-1].pop()
        all_train[i-1].appendleft(0)
    elif order == 4:
        all_train[i-1].popleft()
        all_train[i-1].append(0)

# 기차에서 승객 내리기
check = []
cnt = 0
for train in all_train:
    if train not in check:
        check.append(train)
print(len(check))