# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
input = 20
#에라토스테네스 체로 푸는 방법 ( 배수를 지운다)

def find_prime_list_under_number(number):
    a = [i for i in range(2, number+1)] #2,3, 4, 5, 6, 7 ...
    for i in a:
        if i == 0:
            continue
        for j in range(j+j, i+1)
            result = find_prime_list_under_number(input)
print(result)

