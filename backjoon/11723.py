import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    order_info = list(input().split())
    order = order_info[0]
    n = None if len(order_info) == 1 else int(order_info[1])
    if order == "add":
        s.add(n)
    elif order == "remove":
        if n in s:
            s.remove(n)
    elif order == "check":
        if n in s:
            print(1)
        else:
            print(0)
    elif order == "toggle":
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    elif order == "all":
        s = {i for i in range(1, 21)}
    elif order == "empty":
        s.clear()
