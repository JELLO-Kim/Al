# 공주구하기 (큐)
"""
입력 : 8 3
출력 : 7
"""
"""
큐 : First In First Out (FIFO) 형태의 자료구조
python : deque 라이브러리 활용한다.
"""
from collections import deque

prince_que = deque()
import sys
sys.stdin = open("input.txt")

def my_sol():
    N, K = map(int, input().split())
    for i in range(1, N+1):
        prince_que.append(i)
    m = 1
    while len(prince_que)> 1:
        target = prince_que.popleft()
        if m != K: 
            prince_que.append(target)
            m += 1
        else:
            m = 1
    print(prince_que[0])
my_sol()
