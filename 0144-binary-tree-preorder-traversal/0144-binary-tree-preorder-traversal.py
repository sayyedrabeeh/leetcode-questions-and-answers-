# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = []
        def preorder(node,s):
            if node:
                s.append(node.val)
                preorder(node.left,s)
                preorder(node.right,s)
        preorder(root,s)
        return s