'''
자릿수의 합
1. 문자열로 변환 후 분리하는 방법
2. 10으로 나누어 자릿수 분리하기
3. map 함수를 활용하여 원소값 더하기
'''


# 각 자연수의 자릿수의 합을 구하는 함수
def digit_sum_1(x):
  sum = 0
  for i in str(x):
    sum += int(i)
  return sum


def digit_sum_2(x):
  sum = 0
  while(x!=0):
    sum += x%10
    x = x//10
  return sum

def digit_sum_3(x):
  return sum(map(int, str(x)))

print(digit_sum_2(125))
print(digit_sum_3(123))

n = int(input())
numbers = list(map(int, input().split()))

# maxSum = 0
# for num in numbers:
#   tmp = digit_sum_1(num)
#   if tmp > maxSum:
#     maxSum = tmp
#     result = num
#
# print(result)
