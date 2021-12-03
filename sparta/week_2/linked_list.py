# 링크드 리스트 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data) #head에 시작하는 Node 연결

    def append(self, data): #가장 끝에 있는 노드에 새로운 Node 추가.
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
            print("cur is ", cur.data)
        cur.next = Node(data)

    def print_all(self):
        cur = self.head;
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index: #node -> node가 1번 , index번 만큼 이동해야함.
            node = node.next
            count += 1
        return node

    def add_node(self, index, value): #index 번째 추가
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        node = self.get_node(index -1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def remove_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        node = self.get_node(index -1)
        node.next = node.next.next




linkedList = LinkedList(1)
linkedList.append(10)
linkedList.append(8)
linkedList.append(4)
# print(linkedList.head.data)
linkedList.add_node(0, 2)
linkedList.print_all()
print("=================")
linkedList.remove_node(0)
linkedList.print_all()

