# https://leetcode.com/problems/merge-two-binary-trees/solution/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 is None and t2 is None:
            return []
        
        def value(i):
            if i is None:
                return 0
            else:
                return i.val
        
        def combine(t1, t2, t3):
            
            if t1 is None:
                t1 = TreeNode(0)
            if t2 is None:
                t2 = TreeNode(0)
            
            if (t1 and t1.left or t2 and t2.left:
                t3.left = TreeNode(value(t1.left) + value(t2.left))
            if t1 and t1.right or t2 and t2.right:
                t3.right = TreeNode(value(t1.right) + value(t2.right))
                
            if (t1 and t1.left and t1.left.left) or (t2 and t2.left and t2.left.left):
                t3.left = combine(t1.left, t2.left, t3.left)
            if (t1 and t1.right and t1.right.right) or (t2 and t2.right and t2.right.right):
                t3.right = combine(t1.right, t2.right, t3.right)
            
            return t3
                
        
        t3 = TreeNode(value(t1) + value(t2))
        
        return combine(t1, t2, t3)