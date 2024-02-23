import sys
sys.stdin = open("input.txt")
n, m = map(int, input().split())
chart = []

chart_sum = [[0]*(n+1)]
for x in range(1, n+1):
    row = list(map(int, input().split()))
    tmp_sum_row = [0]*(n+1)
    tmp_row = []
    for y in range(1, n+1):
        tmp_sum_row[y] = tmp_sum_row[y-1] + row[y-1]
        tmp_row.append(row[y-1])
    chart.append(tmp_row)
    chart_sum.append(tmp_sum_row)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    summ = 0
    for xx in range(x1, x2+1):
        summ += (chart_sum[xx][y2] - chart_sum[xx][y1-1])
    print(summ)