'''

6.21(화)
격자판 회문수

'''

a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0


# while True:
#     for i in range(7):
#         for j in range(s, s+e//2):
#             if a[i][j] == a[i][e-j]:
#
for i in range(3):
    #i는 0, 1, 2까지만 돌면 된다.
    for j in range(7):
        #행 확인
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        #k는 5개 내에서 움직이는 용도로 사용됨.
        #열 확인
        for k in range(3):
            if a[i+k][j] != a[i+5-k-1][j]:
                break
        else:
            cnt += 1
print(cnt)
