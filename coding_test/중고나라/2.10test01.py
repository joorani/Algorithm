#n은 1015 이하의 자연수입니다.

def solution(n):
    answer = 0
    #중복을 제거한 리스트로 만든다.
    n_list = list(set(map(int, str(n))))
    for i in n_list:
        for j in range(i+1, )
        if n % i == 0:
            answer += 1
    return answer

