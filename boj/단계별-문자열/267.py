#boj 2675번

t = int(input())
for i in range(t):
    R, word = input().split()

    for w in word:
        print(w * int(R), end="")
    print() #줄넘김