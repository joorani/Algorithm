'''

7.18(월)

'''

def solution(s):
    english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(10):
        s = s.replace(english[i], str(i))

    return int(s)


s = "one4seveneight"
print(solution(s))
