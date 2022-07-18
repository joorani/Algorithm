# '''
# 6.23(목)
#
# 가장 큰 수(스택)
#
# 내 앞에 있는 수가 나보다 작으면 안된다.
#
# python에서 리스트 이용하면 스택으로 사용가능하다.
#
# 5276823 3
# '''
#
#
num, m = map(int, input().split())
s_list = list(map(int, str(num)))
stack = []
print(s_list)

for x in s_list:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
    #m이 남은경우 처리
if m != 0:
    print(stack[-m])
    stack = stack[:-m] #뒤에서 부터 m개를 버린다.

res = ''.join(map(str, stack)) #list 붙여주기
print(res)
