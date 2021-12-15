# 링크드 리스트의 끝에서 K번째 값을 반환하시오.
# [6] -> [7] -> [8] # 이런 링크드 리스트가 입력되었을 때,
#                   # 끝에서 2번째 값은 7을 반환해야 합니다!
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # n = 노드의 길이 - k , n번 돈 노드 반환.
        #노드의 길이 구하기
        length = 1
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length += 1
        end_length = length - k
        # end_length만큼 list 돌기
        cur = self.head
        print(end_length)
        for i in range(end_length):
            cur = cur.next
        return cur

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)