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
    
    def __len__(self):
        if self.head is None:
            return 0
        node_ = self.head
        length = 1
        while node_.next_node:
            length += 1
            node_ = node_.next_node
        return length

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return None

        tail = self.head
        while tail.next_node:
            tail = tail.next_node
        tail.next_node = Node(data)
        return None
    
    def __getitem__(self, index):
        if not isinstance(index, int) and not isinstance(index, slice):
            raise TypeError(f"LinkedList index must be of type int or slice, not {type(index).__name__}")

        if isinstance(index, int):
            if index < 0: #not handling negative indexing for now
                raise IndexError(f"Index {index} is out of range")
            if index >= len(self):
                raise IndexError(f"Index {index} is out of range")
                
            node_ = self.head
            for i in range(index):
                node_ = node_.next_node
            return node_.data
        
        # index is slice
        start = index.start if index.start is not None else 0
        stop = index.stop if index.stop is not None else len(self)
        step = index.step if index.step else 1
        if start < 0 or stop < 0: #not handling negative indexing for now
            raise IndexError(f"Index {start} : {stop} is out of range")
        if start >= len(self)+1 or stop >= len(self)+1:
            raise IndexError(f"Index {start} : {stop} is out of range")
        
        new_ll = LinkedList()
        for i in range(start, stop, step):
            new_ll.append(data=self[i])
        
        return new_ll

    def __setitem__(self, index, data):
        if not isinstance(index, int):
            raise TypeError(f"LinkedList index must be of type int, not {type(index).__name__}")

        if index < 0: #not handling negative indexing for now
            raise IndexError(f"Index {index} is out of range")
        if index >= len(self):
            raise IndexError(f"Index {index} is out of range")

        node_ = self.head
        for i in range(index):
            node_ = node_.next_node

        node_.data = data

        return None

    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"LinkedList index must be of type int, not {type(index).__name__}")

        if index < 0: #not handling negative indexing for now
            raise IndexError(f"Index {index} is out of range")
        if index >= len(self):
            raise IndexError(f"Index {index} is out of range")

        if index == 0:
            self.head = self.head.next_node
            return None

        node_ = self.head
        for i in range(index-1):
            node_ = node_.next_node

        next_node = node_.next_node.next_node
        node_.next_node = next_node

        return None

    def insert(self, index, data):
        if self.head is None:
            self.head = Node(data)
            return None

        if index >= len(self):
            node_ = self.head
            while node_.next_node:
                node_ = node_.next_node
            node_.next_node = Node(data)
            return None

        if index == 0:
            next_node = self.head
            self.head = Node(data, next_node)
            return None

        node_ = self.head
        for i in range(index-1):
            node_ = node_.next_node
        
        next_node = node_.next_node
        node_.next_node = Node(data, next_node)
        
        return None
    
    def pop(self, index):
        node_data = self[index]
        del self[index]

        return node_data

    def reverse_iterative(self):
        if len(self) <= 1:
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

    def __repr__(self):
        if self.head is None:
            return "[]"
        repr_str = ""
        current_node = self.head
        while current_node:
            repr_str += f"{current_node.data}, "
            current_node = current_node.next_node
        return f"[{repr_str[:-2]}]"