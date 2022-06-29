
'''
6.28(화)

휴가(삼성 SW역량평가 기출문제 : DFS활용)

7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
'''
def DFS(L, sum):
    global res

    if L == n:
        if sum> res:
            res= sum
    else:
        if L+pt[L] <= n:
            DFS(L + pt[L], sum+pp[L]) #하는 경우
        DFS(L+1, sum) #하지 않는 경우

if __name__ == '__main__':
    n = int(input())
    pt = []
    pp = []

    for i in range(n):
        t, p = map(int, input().split())
        pt.append(t)
        pp.append(p)
    res = 0
    DFS(0, 0)
    print(res)
