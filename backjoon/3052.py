# 내가 푼 방식
all_list = list()
for row in open("input.txt").readlines():
    all_list.append(int(row.strip())%42)
print(len(set(all_list)))

# 한줄로 끝내기
print(len({int(i)%42 for i in open(0)}))