# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        def traverse(node):
            if node:
                trail.append(node.val)
                if node.children:
                    for n in reversed(range(0, len(node.children))):
                        traverse(node.children[n])
    
        trail = []
        traverse(root)
        return trail[::-1]
        