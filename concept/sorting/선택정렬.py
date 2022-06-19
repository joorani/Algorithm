#선택정렬
# 시간 복잡도 0(n^2)
import time

start_time = time.time()
end_time = time.time()

array = []

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]