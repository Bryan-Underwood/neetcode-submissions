
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        #count of all possible letters
        count = [0] * 26

        for r in range(len(s)):
            #since all numbers are uppercase we can use ascii to find the index of each char
            count[ord(s[r]) - 65] += 1

            #if there are more than k exceptions than move the window
            while (r - l + 1) - max(count) > k:
                count[ord(s[l]) - 65] -= 1
                l += 1

            longest = max(longest, (r - l + 1))

        return longest
