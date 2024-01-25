# 그리디 (창고정리)
"""
10
69 42 68 76 40 87 14 65 76 81
50

출력 : 20
"""

import sys
sys.stdin = open("input.txt")
def my_sol():
    N = int(input())
    box_list = list(map(int, input().split()))
    box_list.sort(reverse=True)
    M = int(input())
    for _ in range(M):
        box_list[0] -= 1
        box_list[-1] += 1
        box_list.sort(reverse=True)
    print(box_list[0] - box_list[-1])
my_sol()