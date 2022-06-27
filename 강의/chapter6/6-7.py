'''
6.26(일)
동전교환

*문제풀이

중복순열이랑 뭔가 비슷...?
1. 가장 큰 동전을 뺄 수 있을 만큼 뺸다.
2.


'''
# import sys
# sys.setrecursionlimit(10 ** 6)
# # import os
# # os.environ["MKL_NUM_THREADS"] = "1"
# # os.environ["NUMEXPR_NUM_THREADS"] = "1"
# # os.environ["OMP_NUM_THREADS"] = "1"
# # # 작업 코드
# #
# #
def DFS(L, sum):
    global res
    # 나는 최소값을 찾고 있기 때문에 tmp보다 값이 크면 빨리 return해서 효율적으로 한다.
    if L > res:
        return
    if sum > money:
        return
    if sum == money:
        # 종료
        if L < res:
            res = L

    else:
        for i in range(n):
            DFS(L + 1, sum+a[i])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    money = int(input())

    a.sort(reverse=True)
    res = 21470000  # 최대값으로 지정해놔야됨
    DFS(0, 0)
    print(res)

# #
# # def DFS(L, money):
# #     global res
# #     #나는 최소값을 찾고 있기 때문에 tmp보다 값이 크면 빨리 return해서 효율적으로 한다.
# #     if L > res:
# #         return
# #
# #     if money == 0:
# #         # 종료
# #         if L < res:
# #             res = L
# #         return
# #     else:
# #         for i in range(n):
# #             DFS(L + 1, money - a[i])
# #
# #
# #
# #
# # if __name__ == '__main__':
# #     start = time.time()  # 시작 시간 저장
# #     n = int(input())
# #     a = list(map(int, input().split()))
# #     money = int(input())
# #
# #     a.sort(reverse=True)
# #     res = 21470000  # 최대값으로 지정해놔야됨
# #     DFS(0, money)
# #     print(res)
# #
# #     print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


# import sys
# sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    global res
    if L>=res:
        return
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    m=int(input())
    res=2147000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)