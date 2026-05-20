from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        heap = []

        for key, freq in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, key))

            else:
                heapq.heappushpop(heap, (freq, key))

        return [h[1] for h in heap]

        #heap based solution
        #Time: NlogK
        #Space: N