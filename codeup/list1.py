n = int(input())
time_list = list(map(int, input().split()))

#리스트를 돌면서 1~23번에 몇 번씩 불리는지 확인

result_list = [0] * 23

for i in time_list:
    result_list[i-1] += 1

for i in result_list:
    print(i, end=' ')