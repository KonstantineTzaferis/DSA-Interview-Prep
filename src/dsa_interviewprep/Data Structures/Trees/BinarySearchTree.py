from typing import Optional 

class TreeNode: 
    def __init__(self, val) -> None: 
        self.val = val 
        self.left: Optional[TreeNode] = None 
        self.right: Optional[TreeNode] = None 


class BinarySearchTree: 
    def __init__(self) -> None: 
        self.root: Optional[TreeNode] = None

    def search(self, root: Optional[TreeNode], target) -> bool: 
        if not root: 
            return False 

        if root.val == target: 
            return True
        elif root.val > target: 
            return self.search(root.left, target)
        else: 
            return self.search(root.right, target)

    def insert_iterative(self, val) -> None:
        new_node = TreeNode(val)

        if not self.root:
            self.root = new_node
            return

        curr = self.root

        while curr:
            if val > curr.val:
                if curr.right is None:
                    curr.right = new_node
                    return

                curr = curr.right

            elif val < curr.val:
                if curr.left is None:
                    curr.left = new_node
                    return

                curr = curr.left

            else:
                return

    def insert_recursive(self, root: Optional[TreeNode], val) -> TreeNode|None: 
            if root is None: 
                return TreeNode(val)
    
            if val > root.val: 
                root.right = self.insert_recursive(root.right, val)
            elif val < root.val: 
                root.left = self.insert_recursive(root.left, val)
            else: 
                return root 

    def remove_node_iterative(self, target) -> int|None: 
        curr: Optional[TreeNode] = self.root 
        prev: Optional[TreeNode] = None

        while curr: 
            if target < curr.val: 
                prev = curr 
                curr = curr.left 
            elif target > curr.val: 
                prev = curr 
                curr = curr.right 
            else: 
                break # We have found the target 

        # We have no root of the tree(Empty Tree)
        if curr is None: 
            return 

        # First Case: We have no children(leaf Node)
        if curr.left is None and curr.right is None: 
            if prev is None: 
                self.root = None 

            elif prev.left is curr: 
                prev.left = None 

            else: 
                prev.right = None

            # This stops the function (we have deleted the node)
            return  

        #------------------------------------------------
        # CASE 2: THE CURR HAS 1 CHILDREN (LEFT OR RIGHT)
        #------------------------------------------------
        if (curr.right and not curr.left) or (not curr.right and curr.left): 
            if curr.left: 
                child = curr.left 
            else: 
                child = curr.right 

            # Deleting the root 
            if prev is None: 
                self.root = child 

            # Now we actually put the node into the right or left of the prev
            elif prev.left is curr: 
                prev.left = child 
            else: 
                prev.right = child 

        #-----------------------------------------------
        # CASE 3: THE CURR NODE HAS EXACTLY TWO CHILDREN
        #-----------------------------------------------
        successor_parent = curr 
        successor = curr.right 

        while successor.left: 
            successor_parent = successor
            successor = successor.left

        curr.val = successor.val 

        if successor_parent is curr: 
            curr.right = successor.right 
        else: 
            successor_parent.left = successor.right           

    def find_minimum(self, root: TreeNode) -> TreeNode: 
        """The minimum of the binary search tree will always be on the left side of the tree. 
           Can also work with subtrees.

        Returns:
            Treenode: Node of the tree
        """
        curr = root

        while curr and curr.left: 
            curr = curr.left 

        return curr 

        

        

        
        

        
            
        
        
        
            

        
        

        