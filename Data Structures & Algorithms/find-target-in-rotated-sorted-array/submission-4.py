class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while left != right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid

        minIndex = left

        #create bounds for another binary search using the min
        if minIndex == 0:
            left, right = 0, len(nums) - 1

        elif target >= nums[0] and target <= nums[minIndex-1]:
            left, right = 0, minIndex - 1

        else:
            left, right = minIndex, len(nums) - 1

        while left <= right:

            m = (left + right) // 2

            if nums[m] == target:
                return m
            
            elif nums[m] < target:
                left = m + 1

            else:
                right = m - 1

        return -1    
           