n = int(input())
n_list = list(map(int, input().split()))

sorted_list = sorted(n_list)

print(sorted_list[0], sorted_list[-1], end=" ")