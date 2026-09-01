from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        n = len(nums)
        bucket = [0] * (n+1)

        for num, freq in count.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]

            else:
                bucket[freq].append(num)


        ret = []
        for i in range(n, -1, -1):
            if bucket[i] != 0:
                ret.extend(bucket[i]) 
            if len(ret) == k:
                break

        return ret