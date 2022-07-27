from .queue import Queue

def IsBinarySearchTree(root_node, low=float("-inf"), high=float("inf")):
    """
    Function that checks whether a given binary tree is a binary search tree or not
    parameters:
    ----------
        root_node : root node of binary tree to check
    return:
    ------
        <True> if given tree is a binary search tree
        <False> otherwise
    """
    if root_node is None:
        return True
    
    return (
        low <= root_node.data <= high and 
        IsBinarySearchTree(root_node=root_node.lchild, low=low, high=root_node.data) and
        IsBinarySearchTree(root_node=root_node.rchild, low=root_node.data, high=high) 
    )

class BTNode:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild
    
    def is_leaf(self):
        if self.lchild is None and self.rchild is None:
            return True
        return False

    def __repr__(self):
        return f"{self.data}"

class BinarySearchTree:
    """
    all children in left sub-tree are less than or equal to parent
    all children in right sub-tree are strictly greater than parent
    """
    def __init__(self):
        self.root = None
    
    def insert(self, data, node_=None):
        if self.root is None:
            self.root = BTNode(data=data)
            return None
        if node_ is None:
            node_ = self.root
        
        if data <= node_.data:
            if node_.lchild is None:
                node_.lchild = BTNode(data=data)
            else:
                self.insert(data=data, node_=node_.lchild)
        else:
            if node_.rchild is None:
                node_.rchild = BTNode(data=data)
            else:
                self.insert(data=data, node_=node_.rchild)

    @staticmethod
    def search(data, node_=None):
        """
        Search if a value is present in the BST. Return True if found, else False
        """
        if node_ is None:
            return False
        
        if node_.data == data:
            return True

        if data <= node_.data:
            if node_.lchild is None:
                return False
            return BinarySearchTree.search(data=data, node_=node_.lchild)
        else:
            if node_.rchild is None:
                return False
            return BinarySearchTree.search(data=data, node_=node_.rchild)

    @staticmethod
    def max(node_:BTNode=None):
        if node_ is None:
            raise ValueError("Using max on an empty Binary Search Tree")
        
        while node_.rchild:
            node_ = node_.rchild
        
        return node_.data

    @staticmethod
    def min(node_:BTNode=None):
        if node_ is None:
            raise ValueError("Using min on an empty Binary Search Tree")
        
        while node_.lchild:
            node_ = node_.lchild
        
        return node_.data

    @staticmethod
    def height(node_=None): 
        if node_ is None:
            return -1

        left_height = BinarySearchTree.height(node_=node_.lchild)
        right_height = BinarySearchTree.height(node_=node_.rchild)

        return max(left_height, right_height) + 1

    def node_depth(self, node_:BTNode):
        if self.root is None:
            raise ValueError("Binary Search Tree is empty")
        
        level = 0
        level_nodes = [self.root]
        while level_nodes:
            for n in level_nodes:
                if node_ is n:
                    return level
            
            level_nodes_new = []
            for n in level_nodes:
                if n.lchild is not None:
                    level_nodes_new.append(n.lchild)
                if n.rchild is not None:
                    level_nodes_new.append(n.rchild)
            level_nodes = level_nodes_new
            level += 1

        raise ValueError("Node not found in Binary Search Tree")

    def _print_(self, node_:BTNode, root_height:int=None):
        """
        Prints a BST root to leaves left to right, centre aligned.
        Right child is printed on top, left child at bottom.
        """
        if node_ is None:
            return None
        if root_height is None:
            root_height = self.height(self.root)
        
        self._print_(node_=node_.rchild, root_height=root_height)
        print(f"{' '*(8*self.node_depth(node_))}{node_.data}")
        self._print_(node_=node_.lchild, root_height=root_height)
    
    @staticmethod
    def print_InOrder(node_:BTNode):
        """
        Static Method: Pass root of BST as parameter
        """
        if node_ is None:
            return None
        
        BinarySearchTree.print_InOrder(node_=node_.lchild)
        print(node_.data, end=" ")
        BinarySearchTree.print_InOrder(node_=node_.rchild)
    
    @staticmethod
    def print_PreOrder(node_:BTNode):
        """
        Static Method: Pass root of BST as parameter
        """
        if node_ is None:
            return None
        
        print(node_.data, end=" ")
        BinarySearchTree.print_PreOrder(node_=node_.lchild)
        BinarySearchTree.print_PreOrder(node_=node_.rchild)
    
    @staticmethod
    def print_PostOrder(node_:BTNode):
        """
        Static Method: Pass root of BST as parameter
        """
        if node_ is None:
            return None
        
        BinarySearchTree.print_PostOrder(node_=node_.lchild)
        BinarySearchTree.print_PostOrder(node_=node_.rchild)
        print(node_.data, end=" ") 
    
    def print_LevelOrder(self):
        if self.root is None:
            return None

        node_queue = Queue()
        node_ = self.root
        node_queue.Enqueuq(node_)
        while not node_queue.IsEmpty:
            node_item = node_queue.Dequeue()
            print(f"{node_item}", end=" ")
            if node_item.lchild is not None:
                node_queue.Enqueuq(node_item.lchild)
            if node_item.rchild is not None:
                node_queue.Enqueuq(node_item.rchild)

    @staticmethod
    def util_min_branch_node(node_:BTNode, parent_:BTNode=None):
        while node_.lchild:
            parent_ = node_
            node_ = node_.lchild
        
        return node_, parent_
    
    @staticmethod
    def util_max_branch_node(node_:BTNode, parent_:BTNode=None):
        while node_.rchild:
            parent_ = node_
            node_ = node_.rchild

        return node_, parent_
    
    @staticmethod
    def util_swap_leaf_for_del(node_to_keep:BTNode, parent_:BTNode=None):
        if node_to_keep.is_leaf():
            if node_to_keep is parent_.lchild:
                    parent_.lchild = None
            else:
                parent_.rchild = None
            return node_to_keep.data

        elif node_to_keep.rchild:
            data_to_keep = node_to_keep.data
            replacement, rep_parent = BinarySearchTree.util_min_branch_node(node_=node_to_keep.rchild, parent_=node_to_keep)
            node_to_keep.data = BinarySearchTree.util_swap_leaf_for_del(node_to_keep=replacement, parent_=rep_parent)
        else:
            data_to_keep = node_to_keep.data
            replacement, _ = BinarySearchTree.util_max_branch_node(node_=node_to_keep.lchild, parent_=node_to_keep)
            node_to_keep.data = BinarySearchTree.util_swap_leaf_for_del(node_to_keep=replacement, parent_=rep_parent)
        
        return data_to_keep

    def delete(self, data, node_:BTNode=None, parent_:BTNode=None):
        if not BinarySearchTree.search(data=data, node_=self.root):
            raise ValueError(f"element '{data}' not found in tree")

        if self.root.data == data and self.root.is_leaf():
            self.root = None
            return
        
        node_ = self.root if node_ is None else node_
        while node_.data != data:
            parent_ = node_
            if data <= node_.data:
                node_ = node_.lchild
            else:
                node_ = node_.rchild
        
        if node_.is_leaf(): # node to delete is a leaf node
            if node_ is parent_.lchild:
                parent_.lchild = None
            else:
                parent_.rchild = None
            
            return

        else:
            BinarySearchTree.util_swap_leaf_for_del(node_to_keep=node_)
