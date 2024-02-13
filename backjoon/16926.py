import sys
sys.stdin = open("input.txt", "r")
n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]




for i in range(n//2):
    one = []
    two = []
    three = []
    four = []
    for j in range(m):
        if not one:
            # one = board[0+i][0+j+i:m-(j+i)]
            one = board[0+i][0+j+i:m-j]
        if not three:
            # three = board[n-1-i][0+j+i:m-(j+i)]
            three = board[n-1-i][0+j+i:m-j]
        # two.append(board[0+j][i])
        # four.append(board[m-1-j][n-1-i])
    for k in range(m//(2*i)):
        two.append(board[i+k][0+i])
        four.append(board[n-1-(i+k)][m-1-i])
    print("?")
