# 최소힙 (힙)
"""
5
3
6
0
5
0
2
4
0
-1

출력
3
5
2
"""
import sys
import heapq as hq
sys.stdin = open("input.txt", "r")
# num_list = map(int, open("input.txt", "r").read().split())

a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a) ==0:
            print((-1))
        else:
            print(hq.heappop(a))  # a의 루트노드 값을 pop 시켜준다.
    else:
        hq.heappush(a, n)  # a list에 n 값을 push 한다. (최소힙의 형태로 들어간다.)
