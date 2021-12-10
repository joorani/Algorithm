# 재귀함수
# 재귀함수를 사용할 때는 반드시 탈출 조건이 있는 지 확인할 것!
# 재귀함수는 자기 자신을 호출하므로써 코드를 간결하고 명확하게 작성할 수 있게 한다.

def count_down(number):
    if number < 0:       #탈출조건
        return
    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!

count_down(60)