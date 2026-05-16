import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #invert list to turn min heap into max heap
        stones = [-s for s in stones]
        
        #create the heap
        heapq.heapify(stones)

        #while there are stones left
        while(len(stones)) > 1:

            #take the largest and second largest off the heap
            biggest = heapq.heappop(stones)
            second = heapq.heappop(stones)

            #if the stones are not equal then find difference
            if second > biggest:
                heapq.heappush(stones, biggest - second)

        #adds a safegaurd if no stones are left
        stones.append(0)


        return abs(stones[0])