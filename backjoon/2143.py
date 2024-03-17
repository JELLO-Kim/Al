import sys
sys.stdin = open("input.txt")
T = int(input())
N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

# N 누적합 구하기
p_n = {}
for i in range(N):
    s = n_list[i]
    if p_n.get(s):
        p_n[s] += 1
    else:
        p_n[s] = 1
    for j in n_list[i+1:]:
        s += j
        if p_n.get(s):
            p_n[s] += 1
        else:
            p_n[s] = 1
# {1: 2, 2: 1, 3: 2, 4: 2, 5: 1, 6: 1, 7: 1}

p_m = {}
for ii in range(M):
    ss = m_list[ii]
    if p_m.get(ss):
        p_m[ss] += 1
    else:
        p_m[ss] = 1
    for jj in m_list[ii+1:]:
        ss += jj
        if p_m.get(ss):
            p_m[ss] += 1
        else:
            p_m[ss] = 1

# {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
count = 0
for n_key in p_n:
    m_value = T - n_key
    if p_m.get(m_value):
        count += p_n[n_key] * p_m[m_value]

print(count)
