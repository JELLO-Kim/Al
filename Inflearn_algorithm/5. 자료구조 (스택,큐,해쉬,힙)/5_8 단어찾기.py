# 딕셔너리 활용
"""
5
big
good
sky
blue
mouse
sky
good
mouse
big

출력 : blue
"""
n, *all_list = open("input.txt", "r").read().split()
note_dict = {i:0 for i in all_list[:int(n)]}
do_list = all_list[int(n):]

for row in all_list[int(n):]:
    note_dict[row] += 1

note_dict = sorted(note_dict.items(), key=lambda x:x[1])
print(note_dict[0][0])

