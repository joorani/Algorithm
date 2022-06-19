# # 최댓값
# answer = []
# data = dict()
# for i in range(9):
#     k, v = i+1, int(input())
#     data[k] = v
#
# lst = sorted(data.values())
# max_num = lst[-1]
# answer.append(max_num)
#
# def answer_make():
#     global k
#     for k in data.keys():
#         if data[k] == max_num:
#             answer.append(k)
#
#
# answer_make()
#
# for i in answer:
#     print(i)

#2번 max를 사용하자
num = []
for i in range(9):
    n = int(input())
    num.append(n)

print(max(num), num.index(max(num))+1)