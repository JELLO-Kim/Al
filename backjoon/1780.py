import sys
sys.stdin = open("input.txt")
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
check_num = [0]*3
def cut_paper(x, y, n):
    num = board[x][y]
    if n == 1:
        check_num[num] += 1
    else:
        for xx in range(n):
            for yy in range(n):
                if board[x+xx][y+yy] != num:
                    # 9등분 한다  : 3x3
                    standard = n//3
                    if standard == 1:
                        for j in range(3):
                            check_num[board[x][y + (standard*j)]] += 1
                            check_num[board[x + standard][y + (standard * j)]] += 1
                            check_num[board[x + (standard*2)][y + (standard * j)]] += 1
                        return
                    else:
                        # 윗줄부터
                        cut_paper(x, y, standard)
                        cut_paper(x, y + standard, standard)
                        cut_paper(x, y + (standard*2), standard)
                        # 중간줄
                        cut_paper(x+standard, y, standard)
                        cut_paper(x+standard, y + standard, standard)
                        cut_paper(x+standard, y + (standard*2), standard)
                        # 아래줄
                        cut_paper(x+(standard*2), y, standard)
                        cut_paper(x+(standard*2), y + standard, standard)
                        cut_paper(x+(standard*2), y + (standard*2), standard)
                    return
        check_num[num] += 1

cut_paper(0, 0, n)

for i in range(-1, 2):
    print(check_num[i])
