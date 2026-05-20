from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #store number of seen int
        freq = defaultdict(int)
        arr = []

        #increment counter every time an int appears
        for num in nums:
            freq[num] += 1

        #append each value to an array
        for key, value in freq.items():
            arr.append([key, value])
        
        #sort the array by the frequency of each pair
        arr.sort(key=lambda x: x[1])

        #pull k values from the end of the sorted list
        arr = arr[-k: ]

        #return the first element in a pair
        return [item[0] for item in arr]