#boj 9012 [stack] 괄호

#1. 비어있을 떄 넣어줌. ( 이면 push
#2. ) 이면 top이랑 비교해서 ()되면 pop
#3. stack 비어있는데 ) 들어오면 NO
#4. len(stack) > 0 : ( 남아있는 경우

t = int(input())

for i in range(t):
    ps = input()

    stk = []
    for p in ps:
        if p == '(':
            stk.append(p)
        else:
            if len(stk) == 0:
                print('NO')
                break
            else:
                stk.pop()

    if len(stk) == 0:
        print("YES")
    else:
        print("NO")


