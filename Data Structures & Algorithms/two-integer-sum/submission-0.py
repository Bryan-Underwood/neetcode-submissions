class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #store seen values in hashmap
        hashmap = {}

        #loop though nums looking for a complement in the hashmap
        for i, v in enumerate(nums):
            #check if program has seen the match num yet
            diff = target - v
            if diff in hashmap:
                return [hashmap[diff], i]

            #map index i to its value in the hashmap
            hashmap[v] = i
                       