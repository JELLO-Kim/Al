import sys
sys.stdin = open("input.txt", "r")

answer = list(map(int, input().split()))

s = 0
def dfs2(l, score, check, answer_set, answer_num):
    global s
    if l == 10:
        if score >= 5:
            s += 1
            print(f"경우의 수 !! {s} | {answer_set} | {answer_num}")
        return
    elif (10-l) < 5 - score:
        return
    else:
        for i in range(1, 6):  # [0, 2, 0, 0, 0, 0]
            if check[i] >= 2:  # 연속 세번은 안된다.
                continue
            if answer[l] == i:
                answer_set += "1"
                new_score = score + 1
            else:
                new_score = score
                answer_set += "0"
            next_check = [0]*6
            if check[i] == 1:
                next_check[i] = 2
            else:
                next_check[i] = 1
            dfs2(l+1, new_score, next_check, answer_set, answer_num + str(i))
            check[i] -= 1
            answer_set = answer_set[:-1]

done_answer = []
check = [0]*6
dfs2(0, 0, check, "", "")
print(s)
