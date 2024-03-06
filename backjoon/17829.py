import sys
sys.stdin = open("input.txt")
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def get_second_max(x, y):
    num_list = []
    for i in range(2):
        for j in range(2):
            num_list.append(board[x+i][y+j])
    num_list.sort(reverse=True)
    return num_list[1]


new_board = []

def _22polling(n):
    global board
    global new_board
    while n != 1:  # 1x1 행렬이 되면 종료
        # 22 polling 시작
        # 1 : 자르고 2순위 최대값 도출
        for xx in range(0, n, 2):  # 자르는 횟수 : 0, 1, 2, 3
            row_list = []
            for yy in range(0, n, 2):  # 자르는 기준은 열로 한다  :0, 1, 2, 3
                row_list.append(get_second_max(xx, yy)) # 첫행 : 크기는 n//2로 줄어든다
            new_board.append(row_list)
        board = new_board
        new_board = []  # new board 초기화
        n = n//2
    res = board[0][0]
    return res


print(_22polling(n))





