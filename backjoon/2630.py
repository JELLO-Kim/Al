import sys
sys.stdin = open("input.txt")
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0
def cut(x, y, n):
    global white
    global blue
    check_color = board[x][y]
    for xx in range(x, x+n):
        for yy in range(y, y+n):
            if board[xx][yy] != check_color: # 조건 1 부합 : 4분할 진행
                cut(x=x, y=y, n=n//2) # 1영역 : x = x ~ x+(n//2) | y = y ~ y+(n//2) | n = n//2
                cut(x=x, y=y+n//2, n=n//2) # 2영역 : x = x ~ x+(n//2) | y = y+n//2 ~ y+n//2+n | n = n//2
                cut(x=x+n//2, y=y, n=n//2) # 3영역 : x = x+n//2 ~ x+n//2+n | y = y ~ y+(n//2) | n = n//2
                cut(x=x+n//2, y=y+n//2, n=n//2) # 4영역 : x = x+n//2 ~ x+n//2+n | y = y+n//2 ~ y+n//2+n | n = n//2
                return # 분할은 분할대로 호출해놓고, 값에 적용되는걸 막기 위해 분할 뒤 return 한다.
    # 분할되지 않으면 모두 색이 같다는 것으로 정답으로 기록한다.
    if check_color == 1:
        blue += 1
    else:
        white += 1

cut(0, 0, n)
print(f"{white}\n{blue}")