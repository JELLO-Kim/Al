# 문자+숫자에서 숫자만 추출하여 순서대로 자연수 만들기
# 만들어진 자연수와 그 자연수의 약수 개수 출력하기
# g0en2Ts8eSoft => 28, 6
def my_sol():
    res_int = 0
    for i in input():
        try:
            i_int = int(i)
            res_int = res_int*10 + i_int
        except:
            continue
    res_count = 1
    for row in range(1, res_int):
        if res_int%row == 0:
            res_count += 1
    print(res_int)
    print(res_count)

def sol():
    """
    isdecimal() 함수 사용함
    - isdecimal = 0~9숫자 확인
    - isdigit = 숫자인지 확인
    """
    res_int = 0
    for i in input():
        if i.isdecimal():
            res_int = res_int*10 + int(i)
    res_count = 0
    for row in range(1, res_int+1):
        if res_int%row == 0:
            res_count += 1
    print(res_int)
    print(res_count)