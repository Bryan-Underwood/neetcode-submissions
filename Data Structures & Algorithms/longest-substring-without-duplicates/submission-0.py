class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = 0
        maxSub = 0


        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            length = (r - l) + 1
            maxSub = max(maxSub, length)
            seen.add(s[r])

        return maxSub          