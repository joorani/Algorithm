'''
교육과정 설계

*문제풀이
1.필수과목을 queue에 넣는다.
2. 주어진 수업설계를 돌면서 필수과목에 포함되는 과목인지 확인한다.
3. 포함되는 과목이라면 필수과목 popleft 한 값과 같은 지 확인한다.
4. 같지 않다면 순서가 잘못된 것이기 때문에 no를 리턴하고 종료한다.
5. 수업설계를 다 돌고난 후 queue가 비어있는지 확인한다.\
6. queue가 비어있지 않다면 no 를 리턴한다.


CBA
3
CBDAGE
FGCDAB
CTSBDE
'''
from collections import deque

e = input() #필수과목을 queue에 담음
n = int(input())
for i in range(n):
    result = True
    essential = deque(e)
    classes = input() #수업계획
    for x in classes:
        if x in essential: #필수과목인지 확인 -> 필수과목이면 순서확인
            if x != essential.popleft():
                result = False
                break
    else:
        if len(essential) != 0:
            result = False
    print(f'#{i+1} YES' if result else f'#{i+1} NO')



