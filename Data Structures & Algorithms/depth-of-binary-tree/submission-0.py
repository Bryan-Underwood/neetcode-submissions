# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, count):

            #base case
            if not root:
                return count

            #find the longest path of the right and left path and return the max
            return max(helper(root.left, count + 1), helper(root.right, count + 1))

        #start at the top of the tree
        return helper(root, 0)