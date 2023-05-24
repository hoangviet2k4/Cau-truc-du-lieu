class Node:
    def __init__(self, data):
        self.right_child = None
        self.left_child = None
        self.data = data
def duyet_cay_thu_tu_sau(root):
    if root:
        duyet_cay_thu_tu_sau(root.left_child)
        duyet_cay_thu_tu_sau(root.right_child)
        print(root.data, end=" ")
if __name__=="__main__":
 '''
    Giả sử muốn tạo cây như bên dưới
                  3
               /    \   
              4      9    
           /  \      / \
          8   6     2   7
    Ta viết như sau
    '''

# Tạo cây
root = Node(3)
root.left_child = Node(4)
root.left_child.left_child = Node(8)
root.left_child.right_child = Node(6)
root.right_child = Node(9)
root.right_child.left_child = Node(2)
root.right_child.right_child = Node(7)
# Duyệt cây theo thứ sau và in ra các giá trị
print("Duyệt cây theo thứ tự sau:\n")
duyet_cay_thu_tu_sau(root)