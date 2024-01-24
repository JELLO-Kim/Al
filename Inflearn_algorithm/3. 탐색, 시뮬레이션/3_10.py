# 스도쿠 검사 : 9*9 스도쿠가 올바르게 풀렸는지 확인하기
"""
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7
"""
import sys
sys.stdin = open("input.txt", "rt")
def my_sol():
    # 포기..ㅜㅜ
    docu_list = [list(map(int, input().split())) for _ in range(9)]
    one_set = 3
    dx = [1, 0]
    dy = [0, 1]
    for i in range(9):
        if len(list(set(docu_list[i]))) != 9:
            print("NO")
            break
        for j in range(9):
            new_one_set = list()
            for k in range(one_set):
                new_one_set.append(docu_list[i+dx[k]])

def sol():
    docu_list = [list(map(int, input().split())) for _ in range(9)]
    # ch1 : 행체크 / ch2 : 열체크 : ch3 : 네모체크
    for i in range(9):
        ch1 = ch2 = [0]*10
        for j in range(9):
            ch1[docu_list[i][j]] = 1
            ch2[docu_list[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            print("NO")
            break
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[docu_list[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                print("NO")
                break
    print("YES")

sol()