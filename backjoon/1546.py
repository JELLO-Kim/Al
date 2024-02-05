# 조작된 수 평균 구하기
# 새 점수 = 기존점수/(최대점수) * 100
N, *num_list = map(int, open("input.txt").read().split())
best_score = max(num_list)
new_score_sum = 0
for row in num_list:
    row = row/best_score *100
    new_score_sum += row
print(new_score_sum/N)