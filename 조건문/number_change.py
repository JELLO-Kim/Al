# 주어진 시간에서 45분 뺀 시간 구하기
# 주어진 시간에서 특정시간 구하기
"""
새로 알게 된 것
특정 값에 대한 음수값의 나머지는 양수값이 된다.
"""
def time_diff():
    h, m = map(int, input())
    new_h = h-(m<45)%24 # 시간은 24시간
    new_m = (m-45)%60 # 분은 60분

    print(h-(m<45)%24, (m-45)%60)

    # 10 10 -> 9 35

def time_add():
    # h, m = map(int, input())
    # cook = int(input())
    h, m = 23, 48
    cook = 25
    print((h+((m+cook)//60))%24, (m+cook)%60)

def set_list():
    A,B,C=3, 3, 6
    num_set_list=list(set([A,B,C]))
    if len(num_set_list) == 3:
        print(max([A,B,C])*100)
    elif len(num_set_list) == 2:
        tmp_list = [A,B,C]
        tmp_list.sort()
        print(1000+tmp_list[1]*100)
    else:
        print(10000+A*1000)
set_list()