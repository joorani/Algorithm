'''
7.7(목)
동전 분배하기(DFS)

7
8
9
11
12
23
15
17
'''
def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set() #세 합이 다 다르다는 걸 확인하기 위해서
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha

    else:
        for i in range(3):
            money[i] += coins[L]
            DFS(L+1)
            #빽한 상황
            money[i] -= coins[L]


if __name__ == '__main__':
    n = int(input())
    coins = []
    for i in range(n):
        coins.append(int(input()))
    res = sum(coins)
    money = [0] * 3
    DFS(0)
    print(res)
