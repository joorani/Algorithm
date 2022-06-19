#2가지 방식으로 구현한 팩토리얼

#1. 반복문으로 구현
def factorial_iterative(n):
    result = 1
    #1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result = result * i
    return result


#2. 재귀적으로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
