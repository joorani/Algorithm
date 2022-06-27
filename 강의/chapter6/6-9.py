'''
6.27(월)

수열 추측하기(순열, 파스칼 응용)

* 문제풀이
이항계수로 풀면 된다.

같은 인덱스의 이항계수와 수열의 자리수를 더합 값이 f와 같으면 수열을 리턴한다.

4 16
'''
import sys


def DFS(L, sum):
    if L == n and sum == f:
        for x in res:
            print(x, end=' ')
        sys.exit(0) #최초 발견된 후 프로그램 종료
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1  # 사용했다.
                res[L] = i
                DFS(L + 1, sum + (res[L] * b[L]))
                ch[i] = 0  # 재사용하려면 체크리스트 다시 0으로 만들어주기

if __name__ == '__main__':
    n, f = map(int, input().split())
    res = [0]*n #결과 수열이 담기는 리스트
    b = [1]*n #이항정리 담는 리스트
    ch = [0]*(n+1) #사용 유무 확인하는 리스트
    for i in range(1, n):
        b[i] = b[i-1]*(n-i)//i
    DFS(0, 0)
    #
    # for x in b:
    #     print(x, end=' ')

