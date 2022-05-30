class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return str(self.data)

class LinkedList:
    """
    Implementation of a Linked List class
    Methods available: append(), insert(), pop(), reverse_iterative(), reverse_recursive(),
    getting, setting and deleting items
    """
    def __init__(self):
        self.head = None
        self.length = 0
    
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.length += 1
            return None

        tail = self.head
        while tail.next_node:
            tail = tail.next_node
        tail.next_node = Node(data)
        self.length += 1
        return None
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"LinkedList index must be of type int, not {type(index).__name__}")

        if index < 0: #not handling negative indexing for now
            raise IndexError(f"Index {index} is out of range")
        if index >= self.length:
            raise IndexError(f"Index {index} is out of range")
            
        node_ = self.head
        for i in range(index):
            node_ = node_.next_node
        return node_.data

    def __setitem__(self, index, data):
        if not isinstance(index, int):
            raise TypeError(f"LinkedList index must be of type int, not {type(index).__name__}")

        if index < 0: #not handling negative indexing for now
            raise IndexError(f"Index {index} is out of range")
        if index >= self.length:
            raise IndexError(f"Index {index} is out of range")

        node_ = self.head
        for i in range(index):
            node_ = node_.next_node

        node_.data = data

        return None

    def __delitem__(self, index):
        self[index-1].next_node = self[index].next_node
        self.length -= 1
        return None

    def insert(self, index, data):
        if self.head is None:
            self.head = Node(data)
            self.length += 1
            return None

        if index >= self.length:
            node_ = self.head
            while node_.next_node:
                node_ = node_.next_node
            node_.next_node = Node(data)
            self.length += 1
            return None

        node_ = self[index]
        node_previous = self[index-1]
        node_previous.next_node = Node(data, next_node=node_)
        self.length+=1
        return None
    
    def pop(self, index):
        previous_node = self[index-1]
        next_node = self[index+1] if self[index].next_node else None
        node_data = self[index].data
        previous_node.next_node = next_node
        #del self[index]
        self.length -= 1
        return node_data

    def reverse_iterative(self):
        if self.length <= 1:
            return self
        
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
        
        return None

    def reverse_recursive(self, node_:Node=None):
        if len(self) <= 1:
            return self
        if node_ is None:
            node_ = self.head
        if node_.next_node is None:
            self.head = node_
            return None
        self.reverse_recursive(node_=node_.next_node)
        next_node = node_.next_node
        next_node.next_node = node_
        node_.next_node = None

    def __len__(self):
        return self.length

    def __repr__(self):
        if self.head is None:
            return "[]"
        repr_str = ""
        current_node = self.head
        while current_node:
            repr_str += f"{current_node.data}, "
            current_node = current_node.next_node
        return f"[{repr_str[:-2]}]"
