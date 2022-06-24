'''
후위식 연산

* 후위식 연산 방법
1. 왼쪽부터 순차적으로 읽으면서 연산자를 찾는다.
2. 찾은 연산자 기준으로 앞 두 개의 피연산자를 연산한다.
3. 연산 진행하고 나면 연산된 값을 기준 후위연산식에 같이 적는다.
4. 1번부터 다시 반복

352+*9-
'''

a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else: #연산자가 나오는 경우
        b = int(stack.pop())
        a = int(stack.pop())
        if x == '+':
            tmp = a+b
        elif x == '-':
            tmp = a-b
        elif x == "*":
            tmp = a * b
        elif x == '/':
            tmp = a / b
        stack.append(tmp)

print(stack.pop())
