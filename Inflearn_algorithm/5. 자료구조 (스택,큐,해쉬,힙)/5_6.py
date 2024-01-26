"""
응급실 (큐)

입력 1
5 2
60 50 70 80 90
출력 1: 3

입력 2
6 0
60 60 90 60 60 60
출력 2 : 5
"""
from collections import deque

# import sys
# sys.stdin = open("input.txt")

def my_sol():
    """ 포기 !! """
    N, M, *patient_list = map(int, open("input.txt", "r").read().split())
    p_que = deque(patient_list)
    tmp = 0
    start_wait = False
    while True:
        target = p_que.popleft()
        if start_wait:
            tmp += 1
        else:
            # 지정인인지 확인
            if patient_list.index(target) == M:
                start_wait = True
                tmp += 1
        if target == max(p_que):
            pass
        else:
            p_que.append(target)

def sol():
    N, M, *patient_list_temp = map(int, open("input.txt", "r").read().split())
    p_list = [(pos, val) for pos, val in enumerate(patient_list_temp)]
    # 순서와 위험도 담기 : [(0, 60), (1, 60), (2, 90), (3, 60), (4, 60), (5, 60)]
    cnt = 0
    p_que = deque(p_list)
    while True:
        cur = p_que.popleft()
        if any(cur[1]<x[1] for x in p_que):
            p_que.append(cur)
        else:
            cnt += 1
            if cur[0] == M:
                break
    print(cnt)

sol()