class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures

        n = len(temp)
        #create return list
        ans = [0] * n

        stk = []

        #keeps track of temp and index through the list
        for i, t in enumerate(temp):
            #if a temp higher than what is on the stack is found
            while stk and stk[-1][0] < t:
                #get the values off the stack
                stk_t, stk_i = stk.pop()
                #place the distance of the higher temp in the ans array
                ans[stk_i] = i - stk_i
            
            stk.append((t, i))
        return ans
