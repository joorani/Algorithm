public class LinkedList {
    Node header;

    static class Node {
        int data;
        Node next = null;
    }

    LinkedList() {
        header = new Node();
    }

    /*
    * 추가
    */
    void append(int d) {
        Node end = new Node();
        end.data = d;
        Node n = header;
        while (n.next != null) {
            n = n.next;
        }
        n.next = end;
    }
    /*
    삭제
    */
    void delete(int d) {
        Node n = header;
        while (n.next != null) {
            if (n.next.data == d) {
                n.next = n.next.next;
            } else {
                n = n.next;
            }
        }
    }

    /*
    출력
    */
    void retrive() {
        Node n = header.next; //n의 다음 데이터부터 출력
        while (n.next != null) {
            System.out.print(n.data+ "->");
            n = n.next;
        }
        System.out.print(n.data);
    }

    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.append(1);
        ll.append(2);
        ll.append(3);
        ll.append(4);
        ll.delete(1); //첫번째 node도 제거 가능함.
        ll.retrive();
    }
}
