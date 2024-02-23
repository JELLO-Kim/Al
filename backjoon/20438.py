import sys
sys.stdin = open("input.txt")

"""
10 1 3 1
7
3 5 7
3 12
"""
n, k, q, m = map(int, input().split())
student = [False]*3 + [True] * n
# student = ["-"]*3 + ["X"] * n

sleep_s = list(map(int, input().split()))
check_count = list(map(int, input().split()))
for check in check_count:
    if check in sleep_s:
        continue
    i = 1
    while True:
        this_check = check * i
        if this_check > n+2:
            break
        if this_check not in sleep_s:
            student[this_check] = False
        # student[this_check] = "O"
        i += 1
    # print(student)
print_list = [list(map(int, input().split())) for _ in range(m)]
for se in print_list:
    print(sum([int(i) for i in student[se[0]:se[1]+1]]))


