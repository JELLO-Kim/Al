"""
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.

첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
"""
# sort() 함수는 nlogn 의 시간복잡도를 가진다
# 해당문자는 n번 반복으로 간단하게 풀 수 있다
import sys
sys.stdin = open("input.txt", "rt")
def my_sol():
    list_all = []
    for _ in range(2):
        input()
        list_all.append(list(map(int, input().split())))
    
    a_list = list_all[0]
    b_list = list_all[1]
    a_p = 0
    b_p = 0
    res_list = list()
    for _ in range(len(a_list) + len(b_list)):
        if a_list[a_p] <= b_list[b_p]:
            res_list.append(a_list[a_p])
            a_p += 1
        else:
            res_list.append(b_list[b_p])
            b_p += 1
    print(res_list)

def sol():
    sys.stdin=open("input.txt", "rt")
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    p1=p2=0
    c = []
    while p1<n and p2<m:
        if a[p1] <= b[p2]:
            c.append(a[p1])
            p1 += 1
        else:
            c.append(b[p2])
            p2 += 1
    if p1<n:
        c.extend(a[p1:])
    if p2<m:
        c.extend(b[p2:])
    print(c)
sol()
