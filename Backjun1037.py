# 이 문제에서 중요한 건 N에 대한 약수가 모두 주어졌을 때 N의 값을 구하는 건데
# 이 약수들 중 가장 작은 수와 가장 큰 수를 곱하면 N을 구할 수 있다.
n = int(input())
mea = list(map(int, input().split()))
min_num = min(mea)
max_num = max(mea)
print(min_num * max_num)