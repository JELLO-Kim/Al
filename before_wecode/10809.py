# 아스키코드 내장함수 활용
# print(ord('a')) # 97

ch = [-1]*(ord('z')-ord('a')+1)
idx = 0
for i in open("input.txt").read().strip():
    if ch[ord(i) - ord('a')] == -1: 
        ch[ord(i) - ord('a')] = idx
    idx += 1

print(" ".join(map(str, ch)))
# for row in ch:
#     print(str(row), end=" ")
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 6 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 %                            
input().find()
