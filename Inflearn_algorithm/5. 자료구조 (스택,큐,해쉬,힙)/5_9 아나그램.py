"""
AbaAeCe
baeeACA
출력 : YES
"""

a, b = open("input.txt", "r").read().split()
a_dict = {i: 0 for i in a}

for row in b:
    if row not in list(a_dict.keys()):
        print("NO")
        break
    else:
        a_dict[row] = 1
a_dict = sorted(a_dict.items(), key=lambda x: x[1])
if a_dict[0][0] == 0:
    print("NO")
else:
    print("YES")