class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a

        l, r = 0, len(a)-1

        while True:
            midA =  (l+r) // 2 #a
            midB = half - midA - 2 #b

            aLeft = a[midA] if midA >= 0 else float("-infinity")
            aRight = a[midA + 1] if (midA + 1) < len(a) else float("infinity")

            bLeft = b[midB] if midB >= 0 else float("-infinity")
            bRight = b[midB + 1] if (midB + 1) < len(b) else float("infinity")

            #partition is correct
            if aLeft <= bRight and bLeft <= aRight:

                #odd
                if total % 2:
                   return min(aRight, bRight)

                #even
                return ((max(aLeft, bLeft)) + min(aRight, bRight)) / 2

            elif aLeft > bRight:
                r = midA - 1

            else:
                l = midA + 1
