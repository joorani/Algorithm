# 백준 2484번 - 주사위 네 개
# 같은 눈 체크 어떻게 할 지가 포인트 -> 정렬한 후 set으로 공통요소 제거하기

def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return 50000 + (lst[0] * 5000)
    if len(set(lst)) == 2: #[1,1,3,3] 또는 [3, 3, 6, 3] 두 가지 경우가 있을 수 있다.
        if lst[1] == lst[2]: #3개가 같은 경우
            return 10000 + (lst[1] * 1000)
        else: #2, 2개 같은 경우 [1, 1, 3, 3]
            return 2000 + (lst[1] + lst[2]) * 500
    for i in range(3): #나머지 경우들은 0,1과 1,2와 2,3이 같은 경우 확인
        if lst[i] == lst[i+1]:
            return 1000 + (lst[i] * 100)
    return lst[-1] * 100 #정렬된 상태이므로 가장 마지막 값이 가장 큰 값


N = int(input())
print(max(money() for i in range(N))) #list comprehension으로 깔끔하게

