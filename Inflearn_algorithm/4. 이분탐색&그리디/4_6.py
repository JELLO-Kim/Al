# 그리디 (씨름선수)
"""
5
172 67
183 65
180 70
170 72
181 60
"""
import sys
import copy
sys.stdin = open("input.txt", "r")
N = int(input())
p_infos = [tuple(map(int, input().split())) for _ in range(N)]
pick_count = 0

def my_sol():
    check_height = copy.deepcopy(p_infos)
    check_height.sort(key=lambda x: x[0], reverse=True)

    # 키 비교 : 이중포문...
    for i in range(1, N):
        check_now = p_infos[i]
        for row in p_infos[0:i]:
            if row[1] > check_now[1]:
                break
        else:
            pick_count += 1
    print(pick_count)

def sol():
    # 이중 for loop 필요없음
    """
    키 순서대로 정렬 한 후, 몸무게가 최고치로 갱신될때마다 pick 하면 된다.
    """
    p_infos.sort(key=lambda x: x[0], reverse=True)
    pick_count = 1
    max_weight = p_infos[0][1]
    for row in p_infos:
        if row[1] > max_weight:
            max_weight = row[1]
            pick_count += 1
    print(pick_count)
sol()