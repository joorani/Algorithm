'''
6.24(금)

단어 찾기(해쉬)
python에서 dictionary 이용
5
big
good
sky
blue
mouse
sky
good
mouse
big
'''

n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1

for i in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break
