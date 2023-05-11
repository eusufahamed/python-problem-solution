class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print('linked list is empty!')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                print(n.ref)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

# node1 = Node(10)
# print(node1)

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.print_LL()