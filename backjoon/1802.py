import sys
sys.stdin = open("input.txt")
# input = sys.stdin.readline
n = int(input())
def fold(case):
    # 안접는 경우 무조건 가능
    if len(case) == 1:
        return True
    middle_num = len(case) // 2
    for j in range(middle_num):
        if case[j] == case[-j-1]:
            return False
    return fold(case[:middle_num]) and fold(case[middle_num+1:])

for _ in range(n):
    fold_list = list(input().rstrip())
    is_possible = fold(fold_list)
    if is_possible:
        print("YES")
    else:
        print("NO")