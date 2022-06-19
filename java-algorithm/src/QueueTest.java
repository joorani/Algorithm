//add, remove, peek, isEmpty
import java.util.NoSuchElementException;

class Queue<T> {

    class Node<T> {
        private T data;
        private Node<T> next;

        public Node(T data) {
            this.data = data;
        }
    }

    //queue는 앞뒤 값의 주소를 알고 있어야 된다.
    private Node<T> first;
    private Node<T> last;

    //값 추가
    public void add(T item) {

        Node<T> t = new Node<>(item);

        //마지막 노드가 있다면 새로 생성한 노트를 붙인다.
        if (last != null) {
            last.next = t;
        }
        last = t;
        if (first == null) {
            first = last;
        }
    }

    //삭제
    public T remove() {
        if (first == null) {
            throw new NoSuchElementException();
        }

        //first의 다음 값이 first가 되어야 되기 때문에 백업 후 first로 변경
        T data = first.data;
        first = first.next;

        if (first == null) {
            last = null;
        }
        return data;
    }

    public T peek() {
        if (first == null) {
            throw new NoSuchElementException();
        }
        return first.data;
    }

    public boolean isEmpty() {
        return first == null;
    }

}

public class QueueTest {
    public static void main(String[] args) {

        Queue<Integer> q = new Queue<>();
        q.add(1);
        q.add(2);
        q.add(3);
        q.add(4);
        System.out.println(q.remove());
        System.out.println(q.remove());
        System.out.println(q.peek());
        System.out.println(q.remove());
        System.out.println(q.isEmpty());
        System.out.println(q.remove());
        System.out.println(q.isEmpty());
    }
}
