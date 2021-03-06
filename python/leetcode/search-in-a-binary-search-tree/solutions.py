# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def nextBST(node):
            if not node:
                return None
            if node.val == val:
                return node
            else:
                if val > node.val:
                    found = nextBST(node.right)
                elif val < node.val:
                    found = nextBST(node.left)
                return found
            return None
        
        return nextBST(root)