'''
6.21(화)
스토쿠 검사

1 2 3 4 5 6 7 8 9
1 1 4 3 6 5 8 9 7
1 4 1 2 7 8 9 5 6
1 3 2 1 8 9 6 7 5
5 6 7 8 9 1 2 3 4
6 5 8 9 1 7 3 4 2
7 8 9 5 2 3 4 6 1
8 9 6 7 4 2 5 1 3
9 7 5 6 3 4 1 2 8

NO

1. 1-9 인덱스
for문으로 숫자 확인하고 나오는 숫자는 +1
'''
# a = [list(map(int, input().split())) for _ in range(9)]
#
# # 각 행 중복 확인
# def checkH():
#     for i in range(9):
#         pre = [0] * 10
#         for j in range(9):
#             pre[a[i][j]] += 1
#         for x in pre:
#             if x > 1:
#                 return False
#     else:
#         return True
#
# #각 열 확인
# def checkY():
#     for i in range(9):
#         pre = [0] * 10
#         for j in range(9):
#             pre[a[j][i]] += 1
#
#         for x in pre:
#             if x > 1:
#                 return False
#     else:
#         return True
#
# #3X3 보드 중복확인
# def checkBoard():
#     for i in range(0, 9, 3):
#         print(i)
#
#
#
# if checkH() and checkY():
#     print("YES")
# else:
#     print("NO")



# ==== 강사풀이 ======
def check(a):
    #행, 열 중복 확인
    for i in range(9):
        ch1 = [0] * 10 #행 체크
        ch2 = [0] * 10 #열 체크

        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    #그룹 탐색
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
# if check(a):
#
#     print("YES")
# else:
#     print("NO")


#======= set 이용 =====
# def check_lines(i, j):
#     set(a[i])

print(set(a[:][0]))
