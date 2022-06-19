# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력
import time

start_time = time.time()
n = int(input())
lst = list(map(int, str(input())))

sum = 0
for i in lst:
    sum += i
end_time = time.time()
print(sum)
print(f"time = {end_time - start_time}" )
sum()