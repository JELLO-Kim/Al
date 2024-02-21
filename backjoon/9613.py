import sys
sys.stdin = open("input.txt")
from itertools import combinations

def figure_gcd(a, b):
    while True:
        # a > b
        tmp = a%b
        if not tmp:
            return b
        else:
            a = b
            b = tmp

for _ in range(int(input())):
    row = list(map(int, input().split()))[1:]
    row.sort(reverse=True)
    row_set = [i for i in combinations(row, 2)]
    gcd = 0
    for a, b in row_set:
        gcd_tmp = figure_gcd(a, b)
        gcd += gcd_tmp
    print(gcd)
