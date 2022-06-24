'''
아나그램

AbaAeCe
baeeACA
'''

a = input()
b = input()

# dictionary 생성
# aDic = dict()
# bDic = dict()
#
# for x in a:
#     aDic[x] = aDic.get(x, 0) + 1 #key가 있으면 value값, 없다면 지정한 기본값 리턴함
# for x in b:
#     bDic[x] = bDic.get(x, 0) + 1
#
# for i in aDic.keys():
#     if i in bDic.keys():
#         if aDic[i] != bDic[i]:
#             print('NO')
#             break
#     else:
#         print('NO')
#         break
# else:
#     print("YES")


# 코드 개선
sH = dict()
for x in a:
    sH[x] = sH.get(x, 0) + 1
for x in b:
    sH[x] = sH.get(x, 0) -1

print(sH)
# 모든 값이 0 이 아니라면 아나그램이 아니다.
for v in sH.values():
    if v != 0:
        print("NO")
        break
else:
    print("YES")

# 리스트 해쉬 방법
str1 =[0]* 52 #알파벳 대소문자 26+26
str2 = [0]*52

for x in a:
    if x.isupper():
        #대문자는 인덱스 0~25까지 사용, 소문자는 인덱스 26~51까지 사용
        str1[ord(x)-65] += 1#아스키넘버로 변환해주는 함수(대문자 65~90)
    else: #소문자는 아스키넘버 97~
        str1[ord(x)-71] += 1

for x in b:
    if x.isupper():
        #대문자는 인덱스 0~25까지 사용, 소문자는 인덱스 26~51까지 사용
        str2[ord(x)-65] += 1#아스키넘버로 변환해주는 함수(대문자 65~90)
    else: #소문자는 아스키넘버 97~
        str2[ord(x)-71] += 1

print(str1)
print(str2)

#같은지 비교
for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print('YES')
