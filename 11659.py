#한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야 할 때는 input()으로
#입력 받는다면 시간초과가 발생할 수 있습니다.
import sys
input = sys.stdin.readline#코테 시 중요!!
N, M = map(int,input.split())
number = list(map(int,input().split()))
res_list = [0] #합배열 list
temp = 0

for i in number: #합배열
    temp = temp + i
    res_list.append(temp)

for i in range(M):
    start, end = map(int,input().split())
    print(res_list[end] - res_list[start - 1])
# import sys
# n = int(sys.stdin.readline())
# data = [sys.stdin.readline().strip() for i in range(n)]
# print(data)