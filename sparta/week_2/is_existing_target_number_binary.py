# 이진탐색
# 이진탐색은 정렬이 되어있는 배열에서만 사용가능하다.

finding_target = 4
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_binary(target, array):
        start = array[0]
        end = array[len(array)-1]
        mid = (start + end) // 2

        while start <= end: #시작값이 끝값보다 작거나 같을 때까지만 반복
            if(mid == target):
                return True
            elif(mid < target):
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end) // 2

        return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)