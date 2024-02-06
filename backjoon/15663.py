import sys
# import copy
from itertools import combinations, permutations
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
a = list(set(permutations(num, m)))
a.sort()
for i in a:
    print(*i)