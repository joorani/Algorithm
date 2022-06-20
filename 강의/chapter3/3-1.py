'''
# 회문 문자열 검사

5
level
moon
abcba
soon
gooG

'''

# # 내풀이
# def solution(word):
#     lng = len(word)
#     for i in range(lng // 2):
#         if word[i] != word[lng - 1 - i]:
#             return False
#             break
#     else:
#         return True
#
#
# n = int(input())
# for i in range(n):
#     word = input()
#     if solution(word.upper()):
#         print(f'#{i+1} YES')
#     else:
#         print(f'#{i+1} NO')

# 강사풀이
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print(f'#{i + 1} YES')
    else:
        print(f'#{i + 1} NO')
