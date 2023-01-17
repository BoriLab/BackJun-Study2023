import sys
input = sys.stdin.readline#코테 시 중요!!
N, M = map(int, input().split())
#원본 리스트
A = [[0] * (N+1)]# 인덱스를 맞춰주려고 // 우리가 (1,1) (3,4)의 범위를 찾을때 파이썬 인덱스는 0부터 시작이니까 0을 통해 인덱스 맞추기
#구간합 배열
D = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

#합배열 연산
for i in range(1, N + 1):
    for j in range(1, N+1):
        D[i][j] = D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(res)