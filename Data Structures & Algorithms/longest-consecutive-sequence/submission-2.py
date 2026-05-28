class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #create a set containing one of every value in nums
        s = set(nums)
        #return the longest substring
        res = 0
        #loop throught the array looking for starter values
        for num in s:
            length =  0
            #A value is a starter if it doesnt have a previous valid value
            if num - 1 in s:
                continue
            
            else:
                starter = num

            #find how many vlaues are consecutivly after the starting value
            while starter in s:
                length += 1
                starter += 1

            #Check if this substring is the longest seen so far
            res = max(res, length)

        return res