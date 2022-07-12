'''
7.11(월)
동적계획법

네트워크 선 자르기(Top-Down : 재귀, 메모이제이션)

'''
def DFS(len):
    # 메모이제이션
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return len # 1또는 2 리턴
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]


if __name__ == '__main__':
    n=int(input())
    dy=[0]*(n+1) #메모이제이션 위해서 값 저장할 배열하나 생성
    print(DFS(n))
