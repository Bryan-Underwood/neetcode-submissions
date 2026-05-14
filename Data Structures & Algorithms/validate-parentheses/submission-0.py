class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { ')' : '(', ']' : '[', '}' : '{', }

        stack = []

        for b in s:
            if b not in hashmap:
                stack.append(b)

            else:
                if not stack:
                    return False

                popped = stack.pop()
                if popped != hashmap[b]:
                    return False

        return not stack