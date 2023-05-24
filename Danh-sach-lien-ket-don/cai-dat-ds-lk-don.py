# Định nghĩa lớp Node để tạo nút cho danh sách liên kết đơn
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Định nghĩa lớp LinkedList để tạo danh sách liên kết đơn
class LinkedList:
    def __init__(self):
        self.head = None

    # Thêm nút mới vào đầu danh sách
    def add_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Thêm nút mới vào cuối danh sách
    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    # Xóa một nút khỏi danh sách
    def delete_node(self, key):
        curr_node = self.head
        # Xử lý trường hợp nút cần xóa là nút đầu tiên
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        # Xử lý trường hợp nút cần xóa không phải là nút đầu tiên
        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None

    # In ra danh sách liên kết đơn
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
# Tạo một đối tượng danh sách liên kết đơn mới
my_list = LinkedList()

# Thêm các nút mới vào danh sách
my_list.add_at_end(1)
my_list.add_at_front(2)
my_list.add_at_end(3)
my_list.add_at_front(4)

# In ra danh sách liên kết đơn
my_list.print_list() # Output: 4 2 1 3

# Xóa một nút khỏi danh sách
my_list.delete_node(2)

# In ra danh sách liên kết đơn sau khi xóa nút
my_list.print_list() # Output: 4 1 3
