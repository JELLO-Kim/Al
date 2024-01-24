# 격자판 회문수 (5) 구하기
"""
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5
"""
import sys
sys.stdin = open("input.txt", "rt")
pal_list = [list(input().split()) for _ in range(7)]

def reverse(x):
    t = 0
    while x>0:
        t = t*10 + x%10
        x = x//10
    return str(t)

cnt = 0
for i in range(7):
    for j in range(3):
        check_num = "".join(pal_list[i][j:j+5])
        reverse_num = reverse(int(check_num))
        if check_num == reverse_num:
            cnt+=1
        check_num2 = "".join(pal_list[j+k][i] for k in range(5))
        reverse_num2 = reverse(int(check_num2))
        if check_num2 == reverse_num2:
            cnt+=1
print(cnt)
