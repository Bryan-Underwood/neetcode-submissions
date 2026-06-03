class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        maxx = 0

        while l < r:

            h = min(heights[l], heights[r])
            water = h * (r - l)
            maxx = max(maxx, water)

            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1

        return maxx
