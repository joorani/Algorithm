
N = int(input())
result = 0

#1 ~ N까지 모든 수 확인
for i in range(1, N+1):
    lst = list(map(int, str(i)))
    c = i + sum(lst)
    if c == N:
        result = i
        break

print(result)