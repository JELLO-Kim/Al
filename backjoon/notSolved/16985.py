import sys
from itertools import combinations, permutations, product
sys.stdin = open("input.txt")
n = 5
m_list = [[list(map(int, input().split())) for _ in range(n)] for _ in range(n)]

# for i in m_list:
#     print(i)

turn_choice = [0, 1, 2, 3]
turn_one_list = []
for i in product(turn_choice, repeat=5):
    turn_one_list.append(i)
#
# for i in permutations(turn_choice, 4):
#     turn_one_list.append(i)

turn_five_list = []
# for j in product(turn_one_list, repeat=5):
#     turn_five_list.append(j)
print(len(turn_five_list))


# 시계방향 회전시키기
def turn_right_one(m):
    clock_m = [[0] * n for _ in range(n)]
    for x, x_a in enumerate(m):
        for y, y_a in enumerate(x_a):
            clock_m[y][(n-x-1)] = y_a
    return clock_m

def turn_right_two(m):
    clock_m = [[0] * n for _ in range(n)]
    for x, x_a in enumerate(m):
        for y, y_a in enumerate(x_a):
            clock_m[n-x-1][n-y-1] = y_a
    return clock_m

def turn_right_three(m):
    clock_m = [[0] * n for _ in range(n)]
    for x, x_a in enumerate(m):
        for y, y_a in enumerate(x_a):
            clock_m[n-y-1][x] = y_a
    return clock_m
# 반시계방향 회전시키기
def turn_left_one(m):
    r_clock_m = [[0] * n for _ in range(n)]
    for x, x_a in enumerate(m):
        for y, y_a in enumerate(x_a):
            r_clock_m[(n-y-1)][x] = y_a
    return r_clock_m

def turn_left_two(m):
    r_clock_m = [[0] * n for _ in range(n)]
    for x, x_a in enumerate(m):
        for y, y_a in enumerate(x_a):
            r_clock_m[n-x-1][n-y-1] = y_a
    return r_clock_m

def turn_left_three(m):
    r_clock_m = [[0] * n for _ in range(n)]
    for x, x_a in enumerate(m):
        for y, y_a in enumerate(x_a):
            r_clock_m[y][n-x-1] = y_a
    return r_clock_m