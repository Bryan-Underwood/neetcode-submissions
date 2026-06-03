class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            #sorted list
            #if target value is greater than 0 no numbers after can add to it
            if nums[i] > 0:
                break

            #skip value if it is a duplicate
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            #create a low and high pointer at the start and end of the list
            lo, hi = i+1, n-1

            #while the pointers have not met
            while lo < hi:
                #check sum of all three values
                summ = nums[i] + nums[lo] + nums[hi]

                #if the summ is zero append to ans and move both pointers together
                if summ == 0:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1

                    #skip over duplicate values
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1

                elif summ < 0:
                    lo += 1

                else:
                    hi -= 1

        return ans
                 