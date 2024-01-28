import sys
sys.stdin=open("input.txt")
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(9)]

s = [[0]*n for _ in range(n)]

for i in a:
    from_p = i[0]
    to_p = i[1]
    pp = i[2]
    s[from_p-1][to_p-1] = pp
for j in s:
    for k in j:
        print(k, end=" ")
    print()