# 그리디 (증가수열 만들기)
"""
5
2 4 5 1 3
출력 : LRLL

10
3 2 10 1 5 4 7 8 9 6

출력 : LRR
"""
import sys
sys.stdin = open("input.txt")
def sol():
    N, *num_list = map(int, sys.stdin.read().split())
    pre_num = 0
    res_string = ""
    lt = 0
    rt = N-1

    tmp = []

    while lt < rt:
        if pre_num < num_list[lt]:
            tmp.append((num_list[lt], "L"))
        if pre_num < num_list[rt]:
            tmp.append((num_list[rt], "R"))

        tmp.sort(key=lambda x:x[0])

        if len(tmp) == 0:
            break
        pre_num = tmp[0][0]
        res_string += tmp[0][1]

        if tmp[0][1] == "L": 
            lt += 1
        else:
            rt -= 1
        tmp.clear()
    print(res_string)

sol()