## Nhập một dãy số nguyên từ bàn phím, và sắp xếp chúng theo thứ tự tăng dần
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

def insertion_sort_linked_list(head):
    if head is None:
        return head

    sorted_list = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next

        if sorted_list is None or sorted_list.data >= current_node.data:
            current_node.next = sorted_list
            sorted_list = current_node
        else:
            search_node = sorted_list
            while search_node.next is not None and search_node.next.data < current_node.data:
                search_node = search_node.next

            current_node.next = search_node.next
            search_node.next = current_node

        current_node = next_node

    return sorted_list

# Nhập dãy số nguyên từ bàn phím
input_list = input("Nhập dãy số nguyên, cách nhau bởi khoảng trắng: ").split()
input_list = [int(i) for i in input_list]

# Sắp xếp dãy số nguyên bằng insertion sort bằng cách tạo một danh sách liên kết đơn
linked_list = LinkedList()
for num in input_list:
    linked_list.add_node(num)

sorted_list = insertion_sort_linked_list(linked_list.head)

# In ra dãy số đã sắp xếp
print("Dãy số đã sắp xếp theo thứ tự tăng dần:")
linked_list.head = sorted_list
linked_list.print_list()
