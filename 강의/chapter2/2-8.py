# '''
# 뒤집은 소수
# '''
#
# #소수인지 확인하는 함수
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True
#
# #뒤집는 함수
# def reverse(x):
#     x = str(x)
#     if x[-1:] == 0:
#         x = x[:-1] # 0~맨 뒷자리 전까지만
#     return int(x[::-1]) #역순으로 복사해서 int로 반환
#
n = int(input())
numbers = list(map(int, input().split()))


# #뒤집는 함수
def reverse_1(x):
    res = 0
    while x >0:
        t = x % 10
        res = res*10+t
        x = x//10

    return res


for num in numbers:
    reversedNum = reverse_1(num)
    if isPrime(reversedNum):
        print(reversedNum, end =' ')