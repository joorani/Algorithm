'''
6.23(목)
쇠막대기

'(' 이면 stack에 append
')' 일때 이전이 '(' 이면 pop 하고 stack에 남은 개수 sum
')' 일때 이전이 ')' 이면 pop하고 +1

()(((()())(())()))(())
'''

s = input()

cnt = 0
stack = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(': #레이저인 경우
            cnt += len(stack)
        else: #닫는 괄호인경우
            cnt += 1

print(cnt)
