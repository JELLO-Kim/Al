# 그리디 (침몰하는 타이타닉)
"""
5 140
90 50 70 100 60
출력 : 3
"""


import sys
sys.stdin = open("input.txt")
def my_sol():
    N, M, *weight_list = map(int, sys.stdin.read().split())
    weight_list.sort(reverse=True)
    lt = 0
    rt = N
    cnt = 0
    while lt < rt:
        if weight_list[lt] < M:
            if weight_list[lt] + weight_list[rt-1] <= M:
                rt -= 1
            lt += 1
            cnt += 1
    print(cnt)
my_sol()