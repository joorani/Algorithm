'''
7.7(목)
양팔저울(DFS)

음수와 양수가 대칭되므로 나온 값에서 음수는 무시해도 된다.

3
1 5 7

'''

def DFS(L, sum):
    global res
    if L == k:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L + 1, sum + a[L])  # 왼(+)
        DFS(L + 1, sum - a[L])  # 오(-)
        DFS(L + 1, sum)  # 안쓰는 경우


if __name__ == '__main__':
    k = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    res = set()  #중복을 제거하면서 값을 추가
    DFS(0, 0)
    print(s-len(res))


