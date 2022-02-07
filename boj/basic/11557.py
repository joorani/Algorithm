T = int(input())  # 테스트 케이스 횟수

# 딕셔너리사용해서 값 넣기
def win():
    answer = []
    for _ in range(T):
        n = int(input())
        data = dict()
        for j in range(n):
            k, v = input().split()
            data[k] = int(v)

        lst = sorted(data.values())  # value 값만 뽑아서 정렬된 리스트로 만듬

        for k in data.keys():
            if data[k] == lst[-1]:
                answer.append(k)

    return answer

for i in win():
    print(i)
