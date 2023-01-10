#5개 줄에 요원의 첩보원명이 주어진다. 첩보원명은 알파벳 대문자,
#숫자 0~9, 대시 (-)로만 이루어져 있으며, 최대 10글자이다.
fbi_list = []
cnt = 0
#리스트 생성
while(cnt <=4):
    input_fbi = str(input())
    if(len(input_fbi)<=10):
        fbi_list.append(input_fbi)
        cnt += 1
        # print(cnt)
    else:
        print("MAX 10")
# 일치  찾기
cond = 0
for num in range(len(fbi_list)):
    if('FBI' in fbi_list[num]):
        print(num + 1)
        cond +=1
if(cond ==0):
    print("HE GOT AWAY!")