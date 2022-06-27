'''
6.27(월)
조합 구하기

조합은 순열과 다르게 순서가 상관없다.

4 2
'''

def DFS(L, S):
    global cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(S, n + 1):
            res[L] = i
            DFS(L + 1, i + 1)



if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0, 1)
    print(cnt)
