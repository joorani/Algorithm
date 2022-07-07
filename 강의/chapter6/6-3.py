'''
부분집합 구하기(DFS)

'''

def DFS(v):
    #종료
    if v == n+1:
        #부분집합 출력
        for i in range(1, n+1):

            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1 #사용하는 경우
        DFS(v+1)
        ch[v] = 0 #사용하지 않는 경우
        DFS(v+1)
        print('f 끝')

if __name__ == '__main__':
    n = int(input())
    #원소를 사용했나 안했나 체크하는 변수
    ch=[0]*(n+1) #1부터 n까지
    DFS(1)
