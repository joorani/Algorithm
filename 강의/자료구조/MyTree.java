/*

preorder (Root, Left, Right)
Inorder (Left, Root, Right)
postorder (Left, Right, Root)

 */
//이진트리
class Node {
    int data;
    Node left;
    Node right;
}

class Tree {
    public Node root;

    public void setRoot(Node node) {
        this.root = node;
    }

    public Node getRoot() {
        return root;
    }

    public Node MakeNode(int data, Node left, Node right) {
        Node node = new Node();
        node.data = data;
        node.left = left;
        node.right = right;
        return node;
    }

    public void inorder(Node node) {
        if (node != null) {
            inorder(node.left);
            System.out.println(node.data);
            inorder(node.right);
        }
    }

    public void preorder(Node node) {
        if (node != null) {
            System.out.println(node.data);
            preorder(node.left);
            preorder(node.right);
        }
    }
    public void postorder(Node node) {
        if (node != null) {
            preorder(node.left);
            preorder(node.right);
            System.out.println(node.data);
        }
    }

}

public class MyTree {
    public static void main(String[] args) {
        Tree t = new Tree();
    }
}
