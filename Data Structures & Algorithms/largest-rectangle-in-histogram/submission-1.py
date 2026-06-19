class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        maxArea = 0

        for index, height in enumerate(heights):
            start = index

            while stk and height < stk[-1][0]:
                h, prev = stk.pop()

                w = index - prev
                a = h * w

                maxArea = max(maxArea, a)
                start = prev

            stk.append((height, start))
            
        while stk:
            h, prev = stk.pop()
            w = n - prev
            maxArea = max(maxArea, h * w)

        return maxArea