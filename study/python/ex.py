import sys
a = [i for i in range(100000)]
aa = sys.getsizeof(a)
b = (i for i in range(100000))
bb = sys.getsizeof(b)

print(aa)
print(bb)
