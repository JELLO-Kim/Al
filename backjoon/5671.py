import sys
sys.stdin = open("input.txt")
try:
    while True:
        count = 0
        n, m = map(int, input().split())
        for i in range(n, m+1):
            str_i = str(i)
            list_str_i = [j for j in str_i]
            if len(str_i) != len(list(set(list_str_i))):
                continue
            count += 1
        print(count)
except:
    sys.exit()