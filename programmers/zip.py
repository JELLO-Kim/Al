# python의 zip() 함수 활용하기

# 기존 풀이
def origin_solution(n, control):
    for row in control:
        if row == "w":
            n+=1
        elif row == "s":
            n -=1
        elif row == "d":
            n += 10
        else:
            n -= 10
    return n

def zip_solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])