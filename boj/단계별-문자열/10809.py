#알파벳 찾기

s_list = list(input())

result = [-1] * 26

for s in s_list:
    s_idx = s_list.index(s)
    result_idx = ord(s)-ord('a')
    result[result_idx] = s_idx

for i in result:
    print(i)

