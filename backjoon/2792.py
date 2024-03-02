import sys
sys.stdin = open("input.txt")

students, color = map(int, input().split())
jewels = [int(input()) for _ in range(color)]

lt = 1
rt = max(jewels)
mid = 0
res = rt
while lt <= rt:
    mid = (lt + rt) // 2
    get_s = 0
    for j in jewels:
        if j % mid == 0:
            get_s += (j//mid) # 똑 나눠 떨어지면 몫이 곧 그 수만큼 나눠받은 학생 수
        else:
            get_s += (j//mid) + 1 # 안나눠떨어지면 몫에다가 나머지만큼 가져간 학생 수

    # 나눠받은 학생 수 가 주어진 학생수보다 많다면 더 많이씩 나눠줘야 한다.
    if get_s > students:
        lt = mid + 1
        res = min(res, mid)
    else:
        # 나눠받은 학생 수가 주어진 학생수보다 같거나 적다면 더 적게 나눠줘도 된다.
        rt = mid - 1
print(res)  #