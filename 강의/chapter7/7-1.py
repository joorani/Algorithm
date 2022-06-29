'''
6.28(화)

최대점수 구하기(DFS)

*문제풀이
부분집합으로 풀면 된다. 문제를 풀거냐 아니냐 선택하는 방식으로 접근한다.

5 20
10 5
25 12
15 8
6 3
7 4

'''
def DFS(L, time, score):
    global res
    if time > m:
        return
    if L == n:
        if score>res:
            res=score
    else:
        DFS(L+1,time+a[L][1], score+a[L][0]) #L번째 문제를 푸는 경우
        DFS(L+1, time, score) # 풀지 않는 경우

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append((x, y))
    print(a)
    res = 0 # 최종점수
    DFS(0, 0, 0)
    print(res)
