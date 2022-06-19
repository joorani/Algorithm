# 숫자를 뒤집어서 비교하는 문제

a, b = input().split()

reverse_a = a[::-1]
reverse_b = b[::-1]

if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)