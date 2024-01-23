all_list = [0]*30
for row in open("input.txt").readlines():
    all_list[int(row.strip())-1] = 1
aa = list()
for idx, i in enumerate(all_list):
    if i == 0:
        aa.append(idx+1)
