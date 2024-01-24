# 이중배열 상하좌우 비교하여 최대값 여부 확인
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
m_list = [list(map(int, input().split()))for _ in range(n)]
m_list.append([0]*n)
m_list.insert(0, [0]*n)
for m in m_list:
    m.append(0)
    m.insert(0, 0)
# print(m_list)
    
# 봉우리 확인하기
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        point = m_list[i][j]
        if all(point>m_list[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt +=1
print(cnt)
