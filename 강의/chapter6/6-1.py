
'''
6.25(토)
재귀함수를 이용한 이진수 출력

'''


def recursive(x):
    if x == 0:
        return
    else:
        # print(x%2, end='') #거꾸로 해야함.
        recursive(x//2)
        print(x%2, end='')

if __name__ == '__main__':

    n = int(input())
    recursive(n)

