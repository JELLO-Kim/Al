# 주어진 문자열의 각 문자 R번씩 반복 출력
"""
2
3 ABC
5 /HTP
"""
T, *ch_list = open("input.txt").read().split()
for i in range(0,llen(ch_list),2):
    print("".join([row*int(ch_list[i]) for row in ch_list[i+1]]))
