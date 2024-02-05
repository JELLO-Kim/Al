# DFS로 풀기

import sys
sys.stdin = open("input2.txt", "r")


"""
가로, 세로, 우 대각선, 좌 대각선 네가지 경우의 수 확인해야 한다.
5개가 넘는지도 확인이 필요하므로 6번 확인한다.
a_res = 가로
b_res = 세로
c_res = 좌상우하 대각선
d_res = 우상좌하 대각선
"""


dook = [list(map(int, input().split())) for _ in range(19)]


def DFS_are(x, y, l):
    global ch1
    global p_res
    # cut
    if x >= 19:
        if l == 5:
            return True
        return
    if ch1[x][y] == 1:
        return
    ch1[x][y] = 1
    # x 값을 +1 씩 해주기
    if dook[x][y] == p:
        if l == 0:
            # 답 기록
            p_res = [x, y]
        l += 1
    else:
        if l == 5:
            return True
        l = 0
    return DFS_are(x+1, y, l)


def DFS_right(x, y, l):
    global ch2
    global p_res
    # cut
    if y >= 19:
        if l == 5:
            return True
        return
    if ch2[x][y] == 1:
        return
    ch2[x][y] = 1
    # y 값을 +1 씩 해주기
    if dook[x][y] == p:
        if l == 0:
            # 답 기록
            p_res = [x, y]
        l += 1
    else:
        if l == 5:
            return True
        l = 0
    return DFS_right(x, y+1, l)

def DFS_left_up_left_down(x, y, l):
    global ch3
    global p_res
    if 0<= x < 19 and 0<= y < 19 and ch3[x][y] == 0:
        ch3[x][y] = 1
        if dook[x][y] == p:
            if l == 0:
                # 답 기록
                p_res = [x, y]
            l += 1
        else:
            if l == 5:
                # 답 기록
                return True
            l = 0
        return DFS_left_up_left_down(x+1, y+1, l)
    else:
        if l == 5:
            return True
        return

def DFS_right_up_left_down(x, y, l):
    global ch4
    global p_res
    if 0<= x < 19 and 0<= y < 19 and ch4[x][y] == 0:
        ch4[x][y] = 1
        if dook[x][y] == p:
            l += 1
        else:
            if l == 5:
                p_res = [x-1, y+1]
                # 답 기록
                return True
            l = 0
        return DFS_right_up_left_down(x+1, y-1, l)
    else:
        if l == 5:
            p_res = [x-1, y+1]
            return True
        return

for p in range(1, 3):
    ch1 = [[0]*19 for _ in range(19)]
    ch2 = [[0]*19 for _ in range(19)]
    ch3 = [[0]*19 for _ in range(19)]
    ch4 = [[0]*19 for _ in range(19)]
    p_find = False
    p_res = []
    for x in range(19):
        for y in range(19):
            if dook[x][y] == p:
                # 아래로 보내기
                if ch1[x][y] == 0:
                    if DFS_are(x, y, 0):
                        p_find = True
                        break
                # 오른쪽으로 보내기
                if ch2[x][y] == 0:
                    if DFS_right(x, y, 0):
                        p_find = True
                        break
                # 좌상우하 대각선으로 보내기
                if ch3[x][y] == 0:
                    if DFS_left_up_left_down(x, y, 0):
                        p_find = True
                        break
                # 우상좌하 대각선으로 보내기
                if ch4[x][y] == 0:
                    if DFS_right_up_left_down(x, y, 0):
                        p_find = True
                        break
        if p_find:
            break
    if p_find:
        print(p)
        print(p_res[0]+1, end=" ")
        print(p_res[1]+1)
        break
    else:
        if p == 2:
            print(0)