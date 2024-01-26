# 그리디 (역수열)
"""
8
5 3 4 0 2 1 1 0
출력 : 4 8 6 2 5 1 3 7
"""
import sys
sys.stdin = open("input.txt")
def sol():
    N, *num_list = map(int, sys.stdin.read().split())
    for idx in range(1, N+1):
        big_count = len([str(i) for i in num_list[:num_list.index(idx)] if i > idx])
        print(big_count)

def my_sol():
    N, *num_list = map(int, sys.stdin.read().split())
    new_num = [0]*N
    for idx, row in enumerate(num_list):
        need_check_count = row
        for idxx, i in enumerate(new_num):
            if new_num[idxx] == 0:
                need_check_count -= 1
                if need_check_count == -1:
                    new_num[idxx] = idx+1
                    break

    print(new_num)

def sol2():
    N, *num_list = map(int, sys.stdin.read().split())
    new_num = [0]*N
    for i in range(N):
        for j in range(N):
            if num_list[i] == 0 and new_num[j] == 0:
                new_num[j] = i+1
                break
            elif new_num[j] == 0:
                num_list[i] -= 1
    for x in new_num:
        print(x, end = " ")
sol2()