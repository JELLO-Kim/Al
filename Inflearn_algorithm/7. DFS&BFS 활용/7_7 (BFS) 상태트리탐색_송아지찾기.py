# BFS 는 Queue 자료구조를 활용한다.
import sys
from collections import deque
sys.stdin = open("input.txt","r")
s, e = map(int, input().split())

max = 10000

ch = [0]*(max+1)
ch[s] = 1
t_count = [0] * (max+1)
move = [-1, 1, 5]
dq = deque()

dq.append(s)
while dq:  # deque()
    now = dq.popleft()  # now : 현재위치 / 이동 횟수 (try)
    if now == e:
        print(t_count[now])
        break
    for next in (now -1, now + 1, now + 5):
        if 0 < next < 10000:
            if ch[next] == 0:
                ch[next] = 1
                dq.append(next)
                t_count[next] = t_count[now] +1