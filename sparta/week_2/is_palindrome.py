# 재귀함수연습- 회문
input = "tomato"

#for문으로 풀기
# def is_palindrome1(string):
#     n = len(string)
#
#     for i in range(n):
#         if string[i] != string[n-1-i]:
#             return False
#
#     return True

#재귀함수로 풀기
def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

print(is_palindrome(input))