import sys
sys.stdin = open("input.txt")
n = int(input())
a, b = map(int, input().split())
a_list = [int(input()) for _ in range(a)]
b_list = [int(input()) for _ in range(b)]

# 전체 합은 딱 한번만 계산되도록 한다.

def get_sum(target_list, target_len):
    target_sum = {}
    for i in range(target_len):
        if i == 0:
            circle_list = target_list[i:-1]
        else:
            circle_list = target_list[i:] + target_list[:i-1]
        s = 0
        for j in circle_list:
            s += j
            if s > n:
                break
            target_sum[s] = target_sum.get(s, 0) + 1
    return target_sum

# a 의 누적합
a_sum = get_sum(a_list, a)
a_sum.update({
    sum(a_list): 1
})
# b 의 누적합
b_sum = get_sum(b_list, b)
b_sum.update({
    sum(b_list): 1
})

# 답 구하기
count = a_sum.get(n, 0) + b_sum.get(n, 0)
for aa in a_sum:
    if aa == n:
        continue
    need_sum = n - aa
    if need_sum in b_sum:
        count += (a_sum[aa] * b_sum[need_sum])
print(count)