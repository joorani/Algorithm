# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
input = 20

def find_prime_list_under_number(number):
    result_array = []
    for n in range(2, number+1):
        # n이 소수인지 아닌지 확인
        for i in range(2, n):
            #나누어 떨어지는 수가 있으면 소수가 아님.
            if n % i == 0:
                break
        else:
            result_array.append(n)

    return result_array

result = find_prime_list_under_number(input)
print(result)
