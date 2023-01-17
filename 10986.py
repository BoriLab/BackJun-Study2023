import sys
input = sys.stdin.readline
N, M = map(int, input().split())
#원본 리스트
A = list(map(int, input().split()))
#저장공간
S = [0] * N
C = [0] * M

S[0] = A[0]
answer = 0
for i in range(1,N):
    S[i] = S[i-1] + A[i] #합배열 저장
for i in range(N):
    remainder = S[i] % M
    if remainder == 0: #0~i까지의 구간 합 자체가 0일떄 정답에 더함
        answer += 1
    C[remainder] += 1 #나머지가 같은 인덱스의 개수값 증가

for i in range(M):
    #나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if C[i]>1:
        answer += (C[i] * (C[i] -1)//2)
print(answer)