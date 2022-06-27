'''
6.27(월)
수들의 조합

5 3
2 4 5 8 12
6
'''

def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
        return
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])


if __name__ == '__main__':
    n, k = map(int, input().split())
    a=list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
