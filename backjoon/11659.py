import sys, time
start = time.time()
sys.stdin = open("input.txt")

n, m = map(int, input().split())
sum_list = [0]
sum_now = 0
for i in list(map(int, input().split())):
    sum_now += i
    sum_list.append(sum_now)

for _ in range(m):
    start_, end_ = map(int, input().split())
    print(sum_list[end_] - sum_list[start_-1])
end = time.time()
print(f"소요시간 : {end-start}")