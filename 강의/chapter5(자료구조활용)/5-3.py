'''
6.23(목)
후위표기식 만들기

여는 괄호와 닫는 괄호 사이의 연산자는 다른 모든 연산자보다 우선한다.

십진수는 출력하고 연산자마나 스택에 append한다.
연산자별로 조건 나눠서 작성한다.
-곱하기와 나누기, 덧셈과 뺄셈 연산 우선순위가 다르기 때문에 나눠서 확인한다.
여는 괄호 stack append

'''

a = input()
stack = []
res = ''
for x in a:
    #숫자인 경우
    if x.isdecimal():
        res += x
    #연산자, 괄호인 경우
    else:
        if x == '(':
            stack.append(x)
        #더하기, 빼기
        elif x == '+' or x == '-':
           # 비교하고자 하는 값보다 stack에 있는 것이 우선순위가 더 높기 때문에
           # stack에 있는거 다 꺼내야함
           #여는 괄호를 만나면 pop을 멈춘다. 왜냐하면 여는 괄호를 만났다는 것은
           # x가 괄호안의 연산자라는 뜻이다. 그러므로 여는 괄호 이전까지만 stack에서 꺼낸다.
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        #곱하기, 나누기
        elif x == '*' or x == '/':
            # stack에 곱하기 또는 나누기가 있는 경우는 stack안에 있는 것을 먼저 사용해야함
            # stack에 있는 만큼 먼저 사용해야 되기 때문에 반복문을 돌린다.
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        #닫는 괄호 -> 여는 괄호까지 stack꺼
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop() # 여는 괄호 없애기

while stack:
    res += stack.pop()

print(res)
