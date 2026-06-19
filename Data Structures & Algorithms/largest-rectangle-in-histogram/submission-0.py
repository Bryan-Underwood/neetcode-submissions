class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        maxArea = 0

        for index, height in enumerate(heights):
            start = index

            while stk and height < stk[-1][0]:
                h, current = stk.pop()

                w = index - current
                a = h * w

                maxArea = max(maxArea, a)
                start = current
                
            stk.append((height, start))
            
        while stk:
            h, current = stk.pop()
            w = n - current
            maxArea = max(maxArea, h * w)

        return maxArea