class Node:
    def __init__(self, key):
        self.val = key
        self.children = []
root = Node(3)
root.children.append(Node(4))
root.children.append(Node(1))
root.children.append(Node(9))
root.children[0].children.append(Node(5))
root.children[0].children[0].children.append(Node(8))
root.children[0].children[0].children.append(Node(6))
root.children[2].children.append(Node(2))
root.children[2].children.append(Node(7))
