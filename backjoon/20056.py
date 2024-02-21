import sys
sys.stdin = open("input.txt","r")

from collections import deque

fire_dq = deque()
n, m, k = map(int, input().split())

play = []
for _ in range(n):
    tmp = []
    for _ in range(n):
        tmp.append([])
    play.append(tmp)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    tmp = list(map(int, input().split()))
    tmp[0] -= 1
    tmp[1] -= 1
    fire_dq.append(tmp)

def separate_work(x, y, balls):
    # 분할처리 해주는 곳
    m_sum = 0
    s_sum = 0
    is_odd = False
    is_even = False
    for one in balls:
        m_sum += one[0]
        s_sum += one[1]
        # 모두 홀수 or 모두 짝수 확인하기
        if one[2] % 2 == 0:
            # 짝수
            is_odd = True
        else:
            is_even = True
    
    new_m = m_sum//5
    new_s = s_sum//len(balls)

    # 만약 새로운 질량이 0이면 파이어볼은 소멸한다.
    if new_m == 0:
        return []

    # 모두 홀수 or 모두 짝수면 방향은 0, 2, 4, 6이다.
    if is_odd and is_even:
        new_d = [1, 3, 5, 7]
    else:
        new_d = [0, 2, 4, 6]
    
    new_balls = []
    for row in new_d:
        new_balls.append((new_m, new_s, row))
    return new_balls
        

for _ in range(k):
    new_play = []
    for _ in range(n):
        tmp = []
        for _ in range(n):
            tmp.append([])
        new_play.append(tmp)
    for _ in range(len(fire_dq)):
        target = fire_dq.popleft()
        # 큐에서 빼기
        r = target[0]
        c = target[1]
        m = target[2]
        s = target[3]
        d = target[4]

        new_r = r + (dx[d])*s
        while True:
            if new_r < 0:
                new_r = n + new_r
            elif new_r >= n:
                new_r = new_r%n
            if 0<= new_r < n:
                break
        new_c = c + (dy[d]) * s
        while True:
            if new_c < 0:
                new_c = n + new_c
            elif new_c >= n:
                new_c = new_c%n
            if 0<= new_c < n:
                break

        new_play[new_r][new_c].append((m, s, d))


    # play 를 new_play 로 대체
    play = new_play
    # k번 이동 후에 겹쳐져 있는것은 분할처리 해준다.
    for x in range(n):
        for y in range(n):
            if len(play[x][y]) > 1:
                # 분할! -> dq에 넣어주기!
                play[x][y] = separate_work(x, y, play[x][y])
                for kkk in play[x][y]:
                    tt = [x, y, kkk[0], kkk[1], kkk[2]]
                    fire_dq.append(tt)
            elif len(play[x][y]) == 1:
                tt = [x, y, play[x][y][0][0], play[x][y][0][1], play[x][y][0][2]]
                fire_dq.append(tt)

# 이동 횟수 끝났으면 play 에서 계산하기
total_m = 0
for ball in play:
    for row in ball:
        if row:
            for check in row:
                total_m += check[0]
print(total_m)