class element:
    def __init__(self, data, next_element=None):
        self.data = data
        self.next_element = next_element

class Queue:
    """
    Implementation of Queue with methods Enqueue(), Dequeuq(), IsEmpyty and front
    """
    def __init__(self):
        self._head = None
        self._tail = None
    
    @property
    def IsEmpty(self):
        if self._head is None:
            return True
        return False

    def Enqueuq(self, data):
        if self.IsEmpty:
            self._head = element(data=data, next_element=None)
            self._tail = self._head
            return None
        
        self._tail.next_element = element(data=data, next_element=None)
        self._tail = self._tail.next_element
        return None
    
    def Dequeue(self):
        if self.IsEmpty:
            return None
        
        return_element = self._head
        self._head = self._head.next_element

        return return_element.data

    @property
    def front(self):
        if self.IsEmpty:
            return None
        return self._head.data

    def __repr__(self):
        repr_str = ""
        element__ = self._head
        while element__:
            repr_str += f"{element__.data}, "
            element__ = element__.next_element
        return f"Queue: [{repr_str[:-2]}]"
