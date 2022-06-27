'''
바둑이 승차(DFS)

*문제풀이
부분집합으로 풀면 된다.

259 5
81
58
42
33
61
'''

def DFS(L, sum, tsum):
    #sum은 집합에 포함된 무게들의 합
    #tsumd 집합에 포함 유무에 상관없이 판단 한 tree의 합
    #total-tsum : 앞으로 판단해야할 바둑이의 무
    global tmp
    #tmp의 최대값을 찾고 있기 때문에 tmp보다 작으면 더 이상 볼 필요가 없음.
    if sum + (total-tsum) < tmp:
        return
    if sum > c:
        return

    if L == n:
        if sum > tmp:
            tmp = sum

    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

if __name__ == '__main__':
    c, n = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(int(input()))
    total = sum(a)
    tmp = 0
    DFS(0, 0, 0)
    print(tmp)


# def DFS2():
#     global cnt #cnt는 전역변수라고 알려줌. 밑에서도 cnt값이 같이 바꿈
#     if cnt == 5:
#         cnt = cnt+1
#         print(cnt)
#
# if __name__ == '__main__':
#     cnt = 5
#     DFS2()
#     print(cnt)