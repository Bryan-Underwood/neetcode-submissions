class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) - 1

        l, r = 0, n
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:

            if leftMax >= rightMax:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
            
            else:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                

        return res