'''
이진트리순회 DFS
depth first search

전위순회 : 대표적, 가장 많음
중위순회 : 잘 사용 안 함
후위순회 : 병합정렬

'''
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v*2) #왼쪽
        DFS(v*2+1) #오른쪽
        print(v, end= ' ')

if __name__ == '__main__':
    DFS(1)