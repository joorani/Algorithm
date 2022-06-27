'''
#재귀 함수와 스택
재귀: 반복문의 대체제로 볼 수 있다.
재귀함수는 stack을 이용한다.
stack에는 매개변수, 지역변수, 복귀주소 가 저장된다.
'''


def DFS(x):
    if x > 0:
        DFS(x-1)
        print(x, end=' ')

if __name__ == "__main__":
    n = int(input())
    DFS(n)
