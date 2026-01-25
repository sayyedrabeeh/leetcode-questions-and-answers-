# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
        def preoder(root,c):
            
            if root is None:
              return  False
            c += root.val 
            if root.left is None and root.right is None:
                return  c == targetSum
            return preoder(root.left,c) or preoder(root.right,c)
  
        return  preoder(root,0)

