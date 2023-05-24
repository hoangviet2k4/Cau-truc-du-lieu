class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None
class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coeff, power):
        new_node = Node(coeff, power)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def add(self, p):
        current1 = self.head
        current2 = p.head
        result = Polynomial()
        while current1 is not None and current2 is not None:
            if current1.power > current2.power:
                result.insert(current1.coeff, current1.power)
                current1 = current1.next
            elif current1.power < current2.power:
                result.insert(current2.coeff, current2.power)
                current2 = current2.next
            else:
                sum_coeff = current1.coeff + current2.coeff
                if sum_coeff != 0:
                    result.insert(sum_coeff, current1.power)
                current1 = current1.next
                current2 = current2.next
        while current1 is not None:
            result.insert(current1.coeff, current1.power)
            current1 = current1.next
        while current2 is not None:
            result.insert(current2.coeff, current2.power)
            current2 = current2.next
        return result

    def display(self):
        current = self.head
        while current is not None:
            print(current.coeff, "x^", current.power, end=" ")
            current = current.next
p1 = Polynomial()
p1.insert(3, 2)
p1.insert(5, 3)
p1.insert(-2, 1)
p1.insert(1, 0)
p1.display()
print('\n')
p2 = Polynomial()
p2.insert(1, 1)
p2.insert(-5, 3)
p2.insert(2, 2)
p2.display()
print('\n')
p3 = p1.add(p2)
p3.display()
