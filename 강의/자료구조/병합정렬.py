'''

병합정렬
- 후위순회 방식

'''

def Dsort(lt, rt):
    if lt<rt:
        mid = (lt+rt)//2
        Dsort(lt, mid)
        Dsort(mid+1, rt)
        #합치는 과정
        p1 = lt
        p2 = mid+1
        tmp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1
        #남아 있는 거 넣어어함
        if p1<=mid:
            tmp = tmp + arr[p1:mid+1] #mid까지 싹 넣기
        if p2<=rt: tmp=tmp+arr[p2:rt+1]
        #tmp값을 원래 값에 복사
        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]


if __name__ == '__main__':
    arr = [23, 11, 45, 35, 15, 67, 33, 21]
    print("Before sort : ", end=' ')
    print(arr)
    Dsort(0, 7)
    print()
    print("After sort : ", end=' ')
    print(arr)