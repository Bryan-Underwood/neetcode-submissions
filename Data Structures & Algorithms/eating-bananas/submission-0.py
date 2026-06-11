class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
    
        while l < r:
            hours = 0
            mid = (l + r) // 2

            for p in piles:
                hours += (p + mid - 1) // mid

            if hours <= h:
                r = mid
                
            else:
                l = mid + 1

        return l
