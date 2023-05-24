class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        print("Đã thêm nút giá trị", data, "vào đầu danh sách")

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        print("Đã thêm nút giá trị", data, "vào cuối danh sách")

    def add_after(self, prev_node, data):
        if prev_node is None:
            print("Nút phía trước không tồn tại")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node
        print("Đã thêm nút giá trị", data, "vào sau nút", prev_node.data)

    def remove_node(self, node):
        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = node.next
            if self.head is not None:
                self.head.prev = None
            node.next = None
            node.prev = None
            print("Đã xóa nút có giá trị", node.data)
            return
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        node.next = None
        node.prev = None
        print("Đã xóa nút có giá trị", node.data)

if __name__ == '__main__':
    dllist = DoublyLinkedList()

    dllist.add_at_end(1)
    dllist.add_at_end(2)
    dllist.add_at_end(3)
    dllist.add_at_end(4)
    dllist.add_at_end(5)

    dllist.print_list()  # In danh sách liên kết kép
