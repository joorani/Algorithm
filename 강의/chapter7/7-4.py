'''
7.7(목)

동전 바꿔주기(DFS)

20
3
5 3
10 2
1 5

동전의 개수 + 1 만큼 가지를 뻗는다.
'''

def DFS(L, sum):
    global cnt
    if sum > t:
        return
    if L == k:
        if sum == t:
            cnt += 1

    else:
        for i in range(n[L]+1):
            DFS(L+1, sum +(p[L] * i))



if __name__ == '__main__':
    t = int(input())
    k = int(input())
    p = [] #동전의 금액
    n = [] #동전의 개수
    for i in range(k):
        a, b = map(int, input().split())
        p.append(a)
        n.append(b)
    cnt = 0
    DFS(0,0)
    print(cnt)

