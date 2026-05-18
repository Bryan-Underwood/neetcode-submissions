# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #global largest variable
        largest_diameter = [0]

        #helper function to find the hight
        def height(root):
            #Base case
            if not root:
                return 0

            #find left and right heights
            left_height = height(root.left)
            right_height = height(root.right)
            #add them to find diameter of subtree
            diameter = left_height + right_height

            #check if it is larger than the largest seen already
            largest_diameter[0] = max(largest_diameter[0], diameter)

            #return the max height
            return 1 + max(left_height, right_height)
    
        height(root)
        return largest_diameter[0]

        
