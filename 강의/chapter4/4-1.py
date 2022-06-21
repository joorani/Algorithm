'''
6.21(화)
이분검색
시간 복잡도
O(logN)


8 32
23 87 65 12 57 32 99 81

#이진탐색 - 재귀로
def binarySearch(array, target, left, right):
    middle_idx = (left + right)//2
    middle = array[middle_idx]
    if target == middle:
        return
    elif middle > target:
        binarySearch(array, target, left, middle_idx-1)
    elif middle < target:
        binarySearch(array, target, middle_idx+1, right)
    else:
        return False
'''

n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort() #오름차순 정렬

left = 0
right = n-1
while left <= right:
    middle_idx = (left+right)//2
    if m == array[middle_idx]:
        print(middle_idx+1)
        break
    elif m < array[middle_idx]:
        right = middle_idx-1
    else:
        left = middle_idx+1

