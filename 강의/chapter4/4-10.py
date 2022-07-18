'''
6.23(목)
역수열(그리디)

8
5 3 4 0 2 1 1 0

'''
# 입력받기
n = int(input())
a = list(map(int, input().split()))
# a.reverse()

res = []
#거꾸로 확인

for i in range(n):
    res.insert(a[n-1-i], n-i)
#insert를 이용해서 풀면 시간 복잡도가 O(N)임

# print(res)

'''
강사풀이
  정렬된 자료를 처리한다고 생각. 
1번째 방법. 0자리를 만날 때마다 앞에 마련해야 할 자리수에서 1을 빼가면서 자리 마련
2번째 방법. cnt 변수를 만들고 자리를 발견할 때마다 cnt += 1 , cnt수가 마련해야 할 자리수와 
같아지면 seq 배열에 삽입
'''

seq = [0]*n

for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            print(seq)
            break
        elif seq[j] == 0: #0자리를 만나면 하나씩 빼준다.
            a[i] -= 1

for x in seq:
    print(x, end= ' ')
