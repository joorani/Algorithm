'''
6.22(수)
회의실 배정 (그리디)

* 그리디 알고리즘이란?
-가장 좋은 것을 선택
- 보통 그리디 알고리즘은 정렬을 동반한 문제이다.

5
1 4
2 3
3 5
4 6
5 7

# 문제풀이 방법
1. 회의가 끝나는 시간으로 오름차순 정렬한다.
2. 다음 회의의 시작시간과 이전 회의의 끝나는 시간이 크거나 같은지 확인한다.
'''

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e)) #튜플 자료형

#끝나는 시간으로 오름차순 정렬
meeting.sort(key=lambda x: (x[1], x[0]) )
print(meeting)

# 끝나는 시간과 이후 회의 시작시간이 같은지 확인
endTime = 0
cnt = 0
for s, e in meeting:
    if s >= endTime:
        endTime = e
        cnt += 1

print(cnt)

