## Nhập một dãy số nguyên từ bàn phím, và cho biết số lần xuất hiện của từng số trong dãy số
class Node:
    # Chức năng khởi tạo các nút
    def __init__(self, data):
        self.data = data #gán dữ liệu
        self.next = None #khởi tạo tiếp theo là null
# Lớp linked list chứa đối tượng Node
class LinkedList:
    # Hàm khởi tạo
    def __init__(self):
        self.head = None
    # Dùng để thêm một node mới vào ds/liên kết đơn
    def add_node(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next

            last_node.next = new_node
    # hàm này in danh sách liên kết
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    # Hàm này được sử dụng để đếm số lần xuất hiện của mỗi phần tử trong ds/liên kết đơn
    def count_occurrences(self):
        counts = {}
        temp = self.head

        while temp:
            if temp.data in counts:
                counts[temp.data] += 1
            else:
                counts[temp.data] = 1

            temp = temp.next

        return counts

# Nhập dãy số nguyên từ bàn phím
input_list = input("Nhập dãy số nguyên, cách nhau bởi khoảng trắng: ").split()
input_list = [int(i) for i in input_list]

# Tạo một danh sách liên kết đơn và đếm số lần xuất hiện của từng số
linked_list = LinkedList()
for num in input_list:
    linked_list.add_node(num)

counts = linked_list.count_occurrences()

# In ra số lần xuất hiện của từng số
print("Số lần xuất hiện của từng số:")
for num, count in counts.items():
    print("{}: {}".format(num, count))
