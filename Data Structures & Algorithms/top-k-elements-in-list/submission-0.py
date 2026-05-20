from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        arr = []

        for num in nums:
            freq[num] += 1

        for key, value in freq.items():
            arr.append([key, value])
        
        arr.sort(key=lambda x: x[1])

        arr = arr[-k: ]

        return [item[0] for item in arr]