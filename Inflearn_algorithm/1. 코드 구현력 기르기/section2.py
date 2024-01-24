import sys
sys.stdin=open("input.txt", "r")
# 두개의 정다면체를 던져 나온 합 중 가장 확률 높은 숫자 출력 (여러개일 경우 오름차순)

def two_five():
    N, M = map(int, input().split())
    answer_list = [0]*(N+M+1)  # 두 수의 합은 2 ~ 두개 정육면체의 최대값 만큼이다

    for n in range(1, N+1):
        for m in range(1, M+1):
            answer_list[n+m] += 1
    max_answer = -1

    for row in answer_list:
        if row >= max_answer:
            max_answer = row

    for idx, final_row in enumerate(answer_list):
            if final_row == max_answer:
                print(idx, end=" ")

def two_six():
    N = int(input())
    a = list(map(int, input().split()))

    max_now = 1
    answer = 0
    for i in range(N):
        idx_sum = 0
        for row in str(a[i]):
            idx_sum += int(row)
        if idx_sum > max_now:
            answer = i
    print(a[answer])