#최대한 많이 나누기

n = 1260
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
  count += n // coin #몫
  n = n % coin

print(count)
