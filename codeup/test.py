#6081
# s= input()
# for i in range(1, 16):
#     print(s, '*', format(i, 'X'), '=', format(int(s, 16)*i, 'X'), sep="")

#6082
# n = int(input())
# for i in range(1, n+1):
#     if i %10 == 3 or i %10 == 6 or i %10 == 9:
#         print('X', end=" ")
#     else:
#         print(i, end=' ')

#6083
'''
r, g, b = map(int, input().split())
cnt = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k )
            cnt+=1
print(cnt)

'''

#6084
'''
h, b, c, s = map(int, input().split())
def calculateMB(h, b, c, s):
    return format((h*b*c*s)/8/1024/1024, ".1f")

print(calculateMB(h,b,c,s)+" MB")
'''

#6085
'''
w, h, b = map(int, input().split())
def result(w, h, b):
    return format((w*h*b)/8/1024/1024, ".2f")
print(result(w,h,b)+ ' MB')
'''
'''
a, m, d, n = map(int, input().split())
cnt = 1
while True:
    if cnt==n:
        print(a)
        break
    a = (a * m)+d
    cnt+=1
'''

'''
a, b, c = map(int, input().split())
day = 1
while day %a != 0 or day%b != 0 or day%c != 0:
    day += 1

print(day)
'''
#6092
'''
n = int(input())
numbers=list(map(int, input().split()))
res = numbers[0]
for num in numbers:
    if num <res:
        res = num
print(res)

'''
#6095
'''
res = [[0] * 20 for _ in range(20)]
n = int(input())
for _ in range(n):
    i, j = map(int, input().split())
    res[i][j] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(res[i][j], end=' ')
    print()
'''

