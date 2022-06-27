'''
6.27(월)
순열구하기

*문제풀이

상태트리는 중복순열과 같이 뻗지만
중복이 안되니깐 체크 리스트 만들어서 사용한 값은 체크

3 2
'''


def DFS(L):
    global cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        cnt += 1
        print()
    else:
        for i in range(1, n+1):
            if ch[i] == 0:  # 적용안된경우
                ch[i] = 1
                res[L] = i
                DFS(L + 1)
                ch[i] == 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0]*m #결과값
    ch = [0]*(n+1) #사용 유무를 확인하는 체크리스트
    cnt = 0
    DFS(0)
    print(cnt)
