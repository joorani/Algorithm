'''
6.19(일)
숫자만 추출
g0en2Ts8eSoft
'''

# str = input()
# # 1. 자연수 추출
# result = []
# for x in str:
#     if x.isdecimal(): #숫자(0~9) 판별 함수
#         result.append(x)
#
# s = ''
# for re in result:
#     if re != '0':
#         s += re
# s = int(s)
# # 2. 약수 개수 구하기
# cnt = 0
# for i in range(1, s+1):
#     if s % i == 0:
#         cnt+=1
# else:
#     print(s)
#     print(cnt)


# 강사풀이
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)  # 앞의 0은 무시된다.

print(res)
