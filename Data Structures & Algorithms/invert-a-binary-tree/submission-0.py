# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):

            #Base case, return none if empty node
            if not node:
                return node


            else:
                #swap left and right children
                node.left, node.right = node.right, node.left

                #invert left side
                invert(node.left)
                #invert right side
                invert(node.right)


            return node

        return invert(root)