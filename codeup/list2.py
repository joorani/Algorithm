n = int(input())
n_list = list(map(int, input().split()))

#거꾸로 n_list 출력
for i in range(len(n_list)):
    print(n_list[len(n_list)-1-i], end=' ')