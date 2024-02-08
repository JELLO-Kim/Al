import sys
sys.stdin = open("input.txt", "r")
n = int(input())
sand = [list(map(int, input().split())) for _ in range(n)]


m = 7//2 + 1

x = 1
y = 1

def moving(x, y):
    if x > m:
        if y < m:
            if y == 1:
                if x == n:
                    y += 1
                else:
                    x += 1
            else:
                y += 1
        elif y == m:
            y += 1
        elif y > m:
            if x == n:
                if y == n:
                    x -= 1
                else:
                    y += 1
            else:
                x -= 1
    elif x < m:
        if y > m:
            if y == n:
                if x == 1:
                    y -= 1
                else:
                    x -= 1
            else:
                y -= 1
        elif y == m:
            y -= 1
        elif y < m:
            if y == 1:
                x += 1
            else:
                y -= 1
    else: # x == m
        if y == m:
            y -= 1
        elif y < m:
            x += 1
        elif y > m:
            x -= 1
    return x, y


test_sand = [[7] * n for _ in range(7)]

start_x = 4
start_y = 4

for t in range(1, 49):
    start_x, start_y = moving(start_x, start_y)
    print(f"{t}번째 움직임 결과 (x,y) = ({start_x},{start_y})")
