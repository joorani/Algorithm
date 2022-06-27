'''
6.25(토)
중복순열 구하기

n가닥 트리

3 2
'''
# import sys
# input = sys.stdin.readline #대량의 데이터를 읽는데 더 빠름
# s = input().rstrip()


def DFS(L):
    global cnt
    if L == m:
        #종료
        for x in res:
            print(x, end=' ')
        print()
        cnt+= 1
    else:
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0]*m
    cnt = 0
    DFS(0)
    print(cnt)

