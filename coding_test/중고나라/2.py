# s = [3, -1, 0, 4]
#
# #지그재그 수열
# def solution(s):
#     count = 0
#     answer = 0
#     for i in range(0, len(s)-1):
#         #횟수가 짝수일 때
#         if count % 2 == 0:
#             if not s[i] < s[i+1] or s[i]== s[i+1]:
#                 answer += 1
#         else:
#             #횟수가 홀수 일때
#             if not s[i] > s[i+1] or s[i]== s[i+1]:
#                 answer += 1
#         count += 1
#     return answer
#
# print(solution(s))