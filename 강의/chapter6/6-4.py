'''
6.25(토)
합이 같은 부분집합(DFS)

*문제풀이
트리를 이용해 만들 수 있는 집합을 다 만든다.
집합1을 만들 떄 사용한 원소들을 제외한 나머지 값들이 집합2가 된다.
주어진 집합의 총 합에서 만든 집합 1의 sum을 뺸 값과 집합2의 값이 같으면 YES를 출력한다.
6
1 3 5 6 7 10

total sum의 절반을 만든 부분 집합들의 sum이 넘어버린다면 더 이상 보지않고 NO를 리턴해주면 된다.


'''
import sys


def DFS(L, sum):
    #L은 a리스트의 인덱스 번호, sum은 만든 집합의 합을 누적
    if sum > total//2:
        return
    if L == n:
        #종료
        if sum == (total-sum):
            print("YES")
            sys.exit(0) #프로그램 종료시켜줌.
    else:
        DFS(L+1, sum+a[L]) #사용하는 경우
        DFS(L+1, sum) #사용하지 않음


if __name__ == '__main__':
    n = int(input())
    a=list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")