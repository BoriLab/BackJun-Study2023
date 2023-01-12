#캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가
#캠핑장은 연속하는 20일 중 10일동안만 사용
#(1 < L < P < V)
L = []
P = []
V = []
i = 0
while(True):
    case_input = str(input())
    case_split = case_input.split(' ')
    if(case_split[0] == '0' and case_split[1] == '0' and case_split[2] == '0'):
        break
    L.append(int(case_split[0]))
    P.append(int(case_split[1]))
    V.append(int(case_split[2]))
    day_cnt = V[i]//P[i] # 캠핑 일수
    day_rem = V[i]%P[i] # 남은일수
    if(L[i] < day_rem):# 남은 일수가 L보다 크면 한번 더 L만큼 사용
        day_rem = L[i]
    print("Case %d: %d" %(i+1, day_cnt*L[i]+day_rem))
    i += 1