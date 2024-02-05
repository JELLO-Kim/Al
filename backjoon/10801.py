# 정수 list 에서 특정 정수 노출 횟수 찾기

import sys
input = sys.stdin.readline

def my_sol():
    # count = int(input())
    # N_list = list(map(int, input().split()))
    # target = int(input())

    count = 11
    N_list = [1, 4, 1, 2, 4, 2, 4, 2, 3, 4, 4]
    target = 2
    res = [str(x) for x in N_list if x == target]
    print(len(res))

def short_sol():
    i=input;i();print(i().split().count(i()))
"""
굳이 필요없는 값을 사용하려 할 필욘없군...
"""