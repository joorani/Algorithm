
def solution(grade):
        for i in range(len(grade)):
            if i == len(grade) - 1 :
                return tmp - sum(grade)
            if grade[i] > grade[i+1]:
                grade[i] -= 1
                solution(grade)


if __name__ == '__main__':
    grade = list(map(int, input().split()))
    tmp = sum(grade)
    print(solution(grade))
