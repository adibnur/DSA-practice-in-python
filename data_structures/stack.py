class element:
    def __init__(self, data, previous_element=None):
        self.data = data
        self.previous_element = previous_element

class stack:
    """
    Implementation of stack data class with push(), pop(), top() and IsEmpty() methods
    """
    def __init__(self):
        self._top = None

    @property
    def IsEmpty(self):
        if self._top is None:
            return True
        
        return False

    def push(self, data):
        previous = self._top
        self._top = element(data=data, previous_element=previous)
        return None

    def pop(self):
        if self.IsEmpty:
            return None
        
        pop_value = self._top.data
        self._top = self._top.previous_element
        
        return pop_value

    @property
    def top(self):
        if self.IsEmpty:
            return None

        return self._top.data

    def __repr__(self):
        repr_str = ""
        element = self._top
        while not element is None:
            repr_str = f"{element.data}, {repr_str}"
            element = element.previous_element
        return f"stack: [{repr_str[:-2]}]"
